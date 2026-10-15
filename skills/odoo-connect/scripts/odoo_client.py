#!/usr/bin/env python3
"""
odoo_client.py - Dependency-free Odoo client for AI agent skills.

Supports Odoo 16, 17, 18 (XML-RPC) and 19+ (JSON-2 API with API key, XML-RPC fallback).
Credentials are read ONLY from environment variables or a .env file:

    ODOO_URL, ODOO_DB, ODOO_USER, ODOO_API_KEY (or ODOO_PASSWORD), ODOO_MASTER_PWD (optional)
    ODOO_CLIENT_DIR  (optional, where logs/actions.jsonl is written; default ./clients/_default)

Every write operation (create/write/unlink/install/create-db/call) is appended to
<ODOO_CLIENT_DIR>/logs/actions.jsonl so all changes are traceable and reviewable.

CLI examples:
    python odoo_client.py version
    python odoo_client.py list-dbs
    python odoo_client.py create-db --name demo_acme --lang en_US --country ae [--demo]
    python odoo_client.py check
    python odoo_client.py installed
    python odoo_client.py install sale_management account stock [--dry-run]
    python odoo_client.py search-read res.partner --domain '[["is_company","=",true]]' --fields name,email --limit 5
    python odoo_client.py create res.partner '{"name": "Demo Customer"}' [--dry-run]
    python odoo_client.py write res.company 1 '{"name": "ACME"}' [--dry-run]
    python odoo_client.py call res.config.settings execute --ids 5 [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
import urllib.request
import xmlrpc.client
from pathlib import Path

WRITE_METHODS = {"create", "write", "unlink", "copy", "button_immediate_install",
                 "button_immediate_uninstall", "execute", "set_values"}


# --------------------------------------------------------------------------- env
def load_env(path: str = ".env") -> None:
    """Minimal .env loader (does not override existing env vars)."""
    for candidate in (Path(path), Path.cwd() / ".env"):
        if candidate.is_file():
            for line in candidate.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
            break


def env(name: str, required: bool = True, default: str | None = None) -> str | None:
    val = os.environ.get(name, default)
    if required and not val:
        sys.exit(f"[odoo_client] Missing environment variable {name}. "
                 f"Ask the user for it and put it in .env (never hard-code it).")
    return val


# --------------------------------------------------------------------------- client
class OdooClient:
    def __init__(self, url: str, db: str | None, user: str | None, secret: str | None,
                 dry_run: bool = False, log_dir: str | None = None):
        self.url = url.rstrip("/")
        self.db, self.user, self.secret = db, user, secret
        self.dry_run = dry_run
        self.uid: int | None = None
        self.log_dir = Path(log_dir or os.environ.get("ODOO_CLIENT_DIR", "clients/_default")) / "logs"
        self._version: dict | None = None

    # ---- helpers
    def _log(self, action: str, payload: dict, result=None) -> None:
        self.log_dir.mkdir(parents=True, exist_ok=True)
        entry = {"ts": _dt.datetime.now().isoformat(timespec="seconds"), "db": self.db,
                 "action": action, "dry_run": self.dry_run, "payload": payload,
                 "result": result if isinstance(result, (int, str, list, dict, bool, type(None))) else str(result)}
        with open(self.log_dir / "actions.jsonl", "a") as fh:
            fh.write(json.dumps(entry, default=str) + "\n")

    def _proxy(self, endpoint: str):
        return xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/{endpoint}", allow_none=True)

    # ---- server info
    def version(self) -> dict:
        if self._version is None:
            self._version = self._proxy("common").version()
        return self._version

    def major(self) -> int:
        info = self.version().get("server_version_info", [0])
        try:
            return int(str(info[0]).split("~")[-1].split("saas~")[-1].split(".")[0])
        except (ValueError, IndexError):
            return 0

    def edition(self) -> str:
        """'enterprise' if the web_enterprise module is installed, else 'community'."""
        try:
            n = self.execute("ir.module.module", "search_count",
                             [[["name", "=", "web_enterprise"], ["state", "=", "installed"]]])
            return "enterprise" if n else "community"
        except Exception:
            return "unknown"

    def use_json2(self) -> bool:
        return self.major() >= 19 and os.environ.get("ODOO_FORCE_XMLRPC") != "1"

    # ---- database service
    def list_dbs(self) -> list:
        try:
            return self._proxy("db").list()
        except xmlrpc.client.Fault as e:
            return [f"<database listing disabled: {e.faultString[:80]}>"]

    def create_db(self, master_pwd: str, name: str, demo: bool = False, lang: str = "en_US",
                  admin_password: str = "admin", login: str = "admin", country: str | None = None) -> bool:
        payload = {"name": name, "demo": demo, "lang": lang, "login": login, "country": country}
        if self.dry_run:
            self._log("create_db", payload, "DRY-RUN")
            return True
        res = self._proxy("db").create_database(master_pwd, name, demo, lang, admin_password,
                                                 login, country or False)
        self._log("create_db", payload, res)
        return res

    # ---- auth & execution
    def login(self) -> int:
        if self.use_json2():
            # JSON-2 is stateless (bearer key); resolve uid for reporting.
            users = self.execute("res.users", "search_read", [[["login", "=", self.user]]], {"fields": ["id"], "limit": 1})
            self.uid = users[0]["id"] if users else 0
            return self.uid
        self.uid = self._proxy("common").authenticate(self.db, self.user, self.secret, {})
        if not self.uid:
            sys.exit("[odoo_client] Authentication failed: check ODOO_DB / ODOO_USER / ODOO_API_KEY.")
        return self.uid

    def _json2(self, model: str, method: str, args: list, kwargs: dict):
        body: dict = dict(kwargs)
        # Map common positional args to JSON-2 named params
        if args:
            if method in ("search", "search_read", "search_count"):
                body.setdefault("domain", args[0])
            elif method == "create":
                body.setdefault("vals_list", args[0] if isinstance(args[0], list) else [args[0]])
            elif method in ("write",):
                body.setdefault("ids", args[0]); body.setdefault("vals", args[1])
            elif method in ("read", "unlink") or isinstance(args[0], list):
                body.setdefault("ids", args[0])
                if method == "read" and len(args) > 1:
                    body.setdefault("fields", args[1])
        req = urllib.request.Request(
            f"{self.url}/json/2/{model}/{method}", data=json.dumps(body).encode(), method="POST",
            headers={"Content-Type": "application/json", "Authorization": f"bearer {self.secret}",
                     "X-Odoo-Database": self.db or ""})
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode() or "null")

    def execute(self, model: str, method: str, args: list | None = None, kwargs: dict | None = None):
        args, kwargs = args or [], kwargs or {}
        is_write = method in WRITE_METHODS or method.startswith(("action_", "button_"))
        if is_write and self.dry_run:
            self._log(f"{model}.{method}", {"args": args, "kwargs": kwargs}, "DRY-RUN")
            return None
        if self.use_json2():
            res = self._json2(model, method, args, kwargs)
        else:
            if self.uid is None:
                self.login()
            res = self._proxy("object").execute_kw(self.db, self.uid, self.secret, model, method, args, kwargs)
        if is_write:
            self._log(f"{model}.{method}", {"args": args, "kwargs": kwargs}, res)
        return res

    # ---- convenience
    def search_read(self, model, domain=None, fields=None, limit=0, order=None):
        kw = {"fields": fields or []}
        if limit: kw["limit"] = limit
        if order: kw["order"] = order
        return self.execute(model, "search_read", [domain or []], kw)

    def installed_modules(self) -> list:
        return self.search_read("ir.module.module", [["state", "=", "installed"]],
                                ["name", "shortdesc"], order="name")

    def install_modules(self, names: list[str]) -> list:
        mods = self.search_read("ir.module.module", [["name", "in", names]], ["id", "name", "state"])
        found = {m["name"] for m in mods}
        missing = sorted(set(names) - found)
        if missing:
            print(f"[odoo_client] WARNING modules not available on server: {missing} "
                  f"(may be Enterprise-only or not in addons path -> record as limitation/question)")
        todo = [m["id"] for m in mods if m["state"] != "installed"]
        if todo:
            self.execute("ir.module.module", "button_immediate_install", [todo])
        return [m["name"] for m in mods if m["state"] != "installed"]


# --------------------------------------------------------------------------- CLI
def build_client(args) -> OdooClient:
    load_env()
    return OdooClient(env("ODOO_URL"), env("ODOO_DB", required=False), env("ODOO_USER", required=False),
                      os.environ.get("ODOO_API_KEY") or os.environ.get("ODOO_PASSWORD"),
                      dry_run=getattr(args, "dry_run", False))


def main(argv=None):
    p = argparse.ArgumentParser(description="Odoo RPC client for agent skills")
    p.add_argument("--dry-run", action="store_true", help="log write operations without executing")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("version"); sub.add_parser("list-dbs"); sub.add_parser("check"); sub.add_parser("installed")
    c = sub.add_parser("create-db")
    c.add_argument("--name", required=True); c.add_argument("--lang", default="en_US")
    c.add_argument("--country"); c.add_argument("--demo", action="store_true")
    c.add_argument("--login", default="admin"); c.add_argument("--admin-password", default=None)
    i = sub.add_parser("install"); i.add_argument("modules", nargs="+")
    s = sub.add_parser("search-read"); s.add_argument("model"); s.add_argument("--domain", default="[]")
    s.add_argument("--fields", default=""); s.add_argument("--limit", type=int, default=0)
    cr = sub.add_parser("create"); cr.add_argument("model"); cr.add_argument("vals")
    w = sub.add_parser("write"); w.add_argument("model"); w.add_argument("ids"); w.add_argument("vals")
    ca = sub.add_parser("call"); ca.add_argument("model"); ca.add_argument("method")
    ca.add_argument("--ids", default=""); ca.add_argument("--args", default="[]"); ca.add_argument("--kwargs", default="{}")
    args = p.parse_args(argv)
    cl = build_client(args)
    out = None

    if args.cmd == "version":
        out = cl.version()
    elif args.cmd == "list-dbs":
        out = cl.list_dbs()
    elif args.cmd == "create-db":
        master = env("ODOO_MASTER_PWD")
        pwd = args.admin_password or env("ODOO_API_KEY", required=False) or env("ODOO_PASSWORD")
        out = cl.create_db(master, args.name, args.demo, args.lang, pwd, args.login, args.country)
    elif args.cmd == "check":
        v = cl.version(); cl.login()
        out = {"url": cl.url, "db": cl.db, "uid": cl.uid, "server_version": v.get("server_version"),
               "major": cl.major(), "api": "json-2" if cl.use_json2() else "xml-rpc", "edition": cl.edition(),
               "companies": cl.search_read("res.company", [], ["name", "currency_id", "country_id"]),
               "installed_apps": [m["name"] for m in cl.search_read(
                   "ir.module.module", [["state", "=", "installed"], ["application", "=", True]], ["name"])]}
    elif args.cmd == "installed":
        out = cl.installed_modules()
    elif args.cmd == "install":
        out = {"installing": cl.install_modules(args.modules), "dry_run": cl.dry_run}
    elif args.cmd == "search-read":
        out = cl.search_read(args.model, json.loads(args.domain),
                             [f for f in args.fields.split(",") if f], args.limit)
    elif args.cmd == "create":
        out = cl.execute(args.model, "create", [json.loads(args.vals)])
    elif args.cmd == "write":
        ids = [int(x) for x in args.ids.split(",")]
        out = cl.execute(args.model, "write", [ids, json.loads(args.vals)])
    elif args.cmd == "call":
        a = json.loads(args.args)
        if args.ids:
            a = [[int(x) for x in args.ids.split(",")]] + a
        out = cl.execute(args.model, args.method, a, json.loads(args.kwargs))
    print(json.dumps(out, indent=2, default=str))


if __name__ == "__main__":
    main()
