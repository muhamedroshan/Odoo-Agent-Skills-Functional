---
name: odoo-connect
description: Connect to an Odoo server (versions 16-19, Community/Enterprise, on-premise/Odoo.sh/Odoo Online) via XML-RPC or the JSON-2 API, check version/edition/installed apps, list or create databases, install modules and read/write records with a dry-run mode and an audit log. Use whenever an agent must talk to a live Odoo instance.
---

# Odoo Connect

Connects the agent to Odoo safely and traceably. Script: `scripts/odoo_client.py` (Python 3.8+, standard library only).

## Rules
1. **Never hard-code or print credentials.** Read them from `.env` (see `.env.example` in the repo root). If any are missing, **ask the user**.
2. **Confirm the hosting type with the user** before anything else: Community on-premise, Enterprise on-premise, Odoo.sh, or Odoo Online (SaaS). Do not infer it from the URL alone. It changes what is possible:
   | Hosting | Custom modules | DB creation over RPC | Studio |
   |---|---|---|---|
   | Community on-prem | Yes | Yes (master password) | No |
   | Enterprise on-prem | Yes | Yes (master password) | Yes |
   | Odoo.sh | Yes (via Git) | No (use the Odoo.sh UI or branches) | Yes |
   | Odoo Online | **No** | No (use odoo.com) | Yes |
3. Run every write with `--dry-run` first when you're unsure, and show the user what will change.
4. Every write is logged to `clients/<client>/logs/actions.jsonl`. Set `ODOO_CLIENT_DIR=clients/<client>` first.

## Choosing a database (in this order)
1. If the user gave you an **existing empty database**, use it. Check it with `check` and confirm that only base modules are installed.
2. Otherwise, **ask the user for the master password** and a database name, then run `create-db`. Ask whether to load Odoo demo data (the default is no, because we seed client-specific data).
3. If the database manager is disabled (`list_db = False`) or the hosting is Odoo.sh/Online, ask the user to create the database manually and give you the credentials.

## Choosing a transport
| Version | Transport | Auth |
|---|---|---|
| 16, 17, 18 | XML-RPC `/xmlrpc/2/*` | login + password or API key |
| 19+ | JSON-2 `/json/2/<model>/<method>` | API key (bearer) + `X-Odoo-Database` |

The script picks the transport automatically from the server version. Set `ODOO_FORCE_XMLRPC=1` to override.

## Commands
```bash
S=skills/odoo-connect/scripts/odoo_client.py
python $S version                       # no auth needed
python $S list-dbs
python $S create-db --name demo_acme --lang en_US --country ae
python $S check                         # version, edition, API, companies, installed apps
python $S installed
python $S --dry-run install sale_management account stock
python $S install sale_management account stock
python $S search-read res.partner --domain '[["customer_rank",">",0]]' --fields name,email --limit 5
python $S create product.template '{"name":"Demo Chair","list_price":120}'
python $S write res.company 1 '{"name":"ACME LLC"}'
python $S call res.config.settings execute --ids 7
```

## Using it from Python
```python
import sys; sys.path.insert(0, "skills/odoo-connect/scripts")
from odoo_client import OdooClient, load_env; import os
load_env(); c = OdooClient(os.environ["ODOO_URL"], os.environ["ODOO_DB"], os.environ["ODOO_USER"], os.environ["ODOO_API_KEY"])
c.login(); print(c.major(), c.edition())
```

## Changing settings (`res.config.settings`)
Create a settings record and then execute it:
`call res.config.settings create --args '[{"group_multi_currency": true}]'` → returns an id → `call res.config.settings execute --ids <id>`.

## Troubleshooting
- `Access Denied`: wrong database, login or key. On 19+, the API key must belong to the user.
- A module is reported "not available": it is Enterprise-only or missing from the addons path. Log it as a **question or limitation**; do not work around it silently.
- On Odoo Online, XML-RPC requires an API key and is limited by plan. Confirm with the user.
