# Odoo Agent Skills (Functional)

A skill pack that lets **Claude Code, Antigravity and Codex** run an Odoo requirement analysis and demo workflow:

> Connect to Odoo → analyze client requirements → **ask, never assume** → fit-gap (Standard / Configuration / Studio / Customization / Limitation, Must vs Nice) → build a standard demo DB → phase the project (development last) → document everything with review guides.

## Why this design
- **One source, three agents.** All three agents read the same `SKILL.md` format. Only the folder they look in differs, and `install.sh` links the skills into each one.
- **Gated workflow.** The agent cannot build the demo or plan phases while blocking questions are open. This prevents assumption-driven configuration, especially in accounting.
- **Traceability.** Every server change is logged twice: a human-readable configuration log (with menu paths) and a machine-readable `actions.jsonl`. Every document line refers to a requirement (REQ), question (Q) or decision (DEC).
- **Standard first, development last.** This keeps cost, risk and upgrade effort low. Custom work is planned only after the client has seen what standard Odoo can do.

## Install
```bash
./install.sh                         # interactive: asks for the agent(s) and the scope
./install.sh --agent all --scope project --target ~/clients/acme
./install.sh --agent claude --scope user --copy
```
| Agent | Project scope | User scope | Instruction file |
|---|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `CLAUDE.md` → `AGENTS.md` |
| Antigravity | `.agent/skills/` | `~/.gemini/antigravity/skills/` | `GEMINI.md` → `AGENTS.md` |
| Codex | `.agents/skills/` | `~/.codex/skills/` | `AGENTS.md` |

Then run `cp .env.example .env` and fill in the Odoo URL, database, user and API key. Add the master password only if the agent should create databases.

Requirements: Python 3.8+ (standard library only) and network access to the Odoo server.

## Usage
Tell your agent, for example:
> "Use the odoo-implementation-workflow skill. Here are ACME's requirements: … Our server is in .env."

The agent will then:
1. Ask for the version (16–19), edition and hosting, and the document language(s). It always asks, even when it can detect them.
2. Connect, using the empty database you gave it, or ask for the master password to create one.
3. Split the requirements into `REQ-###` items and ask clarification questions in batches (accounting is always covered).
4. Confirm Must Have / Nice to Have with you.
5. Produce the fit-gap matrix with why, how and an indicative effort, and wait for your approval.
6. Build the demo database from standard and configuration items only, logging every step.
7. Produce the phase plan, with custom development and integrations last.
8. Write the workflow explanations and the review guide, then walk you through the review.

## Skills
| Skill | Purpose |
|---|---|
| [odoo-implementation-workflow](skills/odoo-implementation-workflow/SKILL.md) | Orchestrator with stage gates |
| [odoo-connect](skills/odoo-connect/SKILL.md) | XML-RPC (16–18) / JSON-2 (19+) client, database creation, installs, audit log |
| [odoo-requirements-analysis](skills/odoo-requirements-analysis/SKILL.md) | Requirements, question banks for 11 areas, priorities |
| [odoo-fit-gap](skills/odoo-fit-gap/SKILL.md) | Categorization, edition/hosting rules, effort sizing |
| [odoo-demo-db-builder](skills/odoo-demo-db-builder/SKILL.md) | Standard demo build with configuration log |
| [odoo-project-phasing](skills/odoo-project-phasing/SKILL.md) | Phases 1–4, development last |
| [odoo-documentation](skills/odoo-documentation/SKILL.md) | 10 Markdown templates and writing rules |

## Output per client
```
clients/<client>/
├── STATUS.md                      # current stage, blockers, next step (lets any agent resume)
├── logs/actions.jsonl             # raw audit trail of server writes
└── docs/00_index.md … 09_customization_specs.md
```

## How to review the agent's work
| What to review | Where | What to check |
|---|---|---|
| Nothing was assumed | `02_open_questions_and_decisions.md` | Every configuration choice has a DEC with "Confirmed" status |
| Categorization | `03_fit_gap_matrix.md` | The *Why* column cites real standard features. No CUS item where CFG would do |
| Limitations | `04_technical_limitations.md` | Root cause and alternatives are stated |
| Demo build | `05_demo_db_configuration_log.md` + the demo itself | Follow the UI paths and confirm each setting exists. Compare with `actions.jsonl` |
| Plan | `06_project_phases.md` | All CUS items are in the last phase; Must Have CUS items have workarounds |
| Business fit | `07_workflow_explanation.md` + `08_review_guide.md` | Run every scenario and sign off |

## Maintenance
- `tools/generate_templates.sh` regenerates the documentation templates.
- `python tools/lint_skills.py` validates the SKILL.md frontmatter.
