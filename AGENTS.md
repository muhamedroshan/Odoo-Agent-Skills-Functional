# AGENTS.md: Odoo Implementation Agent Rules

These rules apply to every agent (Claude Code, Antigravity, Codex) working in this repository or in a client project where these skills are installed.

## Start here
For any Odoo requirement analysis, demo or planning request, load the **`odoo-implementation-workflow`** skill and follow its stages in order:
`Setup → Intake → Clarify → Fit-Gap → Approval → Demo DB → Phasing → Docs → Review`.

## Non-negotiable rules
1. **Never assume.** Unknown facts (accounting, taxes, flows, users, hosting, languages…) are questions. Ask the user and wait for the answer.
2. **Confirm the edition and hosting** (Community / Enterprise / Odoo.sh / Odoo Online) and the **version** (16–19) explicitly, even if you can detect them.
3. **Ask the document language(s)** before writing any client document.
4. **Database:** use the empty database the user provided. If there isn't one, ask for the master password to create one.
5. **Standard first:** STD > CFG > Studio > Custom. Justify every escalation.
6. **Must Have / Nice to Have** priorities must be confirmed by the user.
7. **Custom development and integrations always go in the last phase.**
8. **Document everything** in `clients/<client>/docs/` and keep `clients/<client>/STATUS.md` current, so another agent can resume.
9. **Secrets:** read credentials from `.env` only. Never print or commit them.
10. Use `--dry-run` for risky writes and show the user what will change.

## Skills
| Skill | Use for |
|---|---|
| odoo-implementation-workflow | Orchestration and stage gates |
| odoo-connect | RPC connection, database creation, installs, reads and writes |
| odoo-requirements-analysis | Requirements, clarification questions, priorities |
| odoo-fit-gap | Categorization, why/how, effort |
| odoo-demo-db-builder | Building the demo database |
| odoo-project-phasing | Phase plan |
| odoo-documentation | Templates and writing rules |
