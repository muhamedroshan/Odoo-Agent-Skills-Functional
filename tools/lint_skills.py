#!/usr/bin/env python3
"""Validate SKILL.md frontmatter for Claude Code / Antigravity / Codex compatibility."""
import re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent / "skills"
ok = True
for skill in sorted(p for p in root.iterdir() if p.is_dir()):
    f = skill / "SKILL.md"
    if not f.is_file():
        print(f"✘ {skill.name}: missing SKILL.md"); ok = False; continue
    m = re.match(r"^---\n(.*?)\n---\n", f.read_text(), re.S)
    if not m:
        print(f"✘ {skill.name}: missing YAML frontmatter"); ok = False; continue
    meta = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    name, desc = meta.get("name", "").strip(), meta.get("description", "").strip()
    errs = []
    if name != skill.name: errs.append(f"name '{name}' != folder")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name): errs.append("name must be lowercase-hyphen <=64")
    if not desc or len(desc) > 1024: errs.append("description empty or >1024 chars")
    print(("✘ " if errs else "✔ ") + skill.name + (": " + "; ".join(errs) if errs else ""))
    ok &= not errs
sys.exit(0 if ok else 1)
