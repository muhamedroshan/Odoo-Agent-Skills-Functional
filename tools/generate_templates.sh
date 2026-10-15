#!/usr/bin/env bash
# Generates the documentation templates (run once by the maintainer; output is committed).
set -euo pipefail
T="$(dirname "$0")/../skills/odoo-documentation/templates"
mkdir -p "$T"

cat > "$T/00_index.md" <<'EOF'
# {{CLIENT}}: Odoo Implementation Documentation

| Item | Value |
|---|---|
| Client | {{CLIENT}} |
| Odoo version | {{16/17/18/19}} (confirmed by: …, date: …) |
| Edition | {{Community / Enterprise}} (confirmed) |
| Hosting | {{On-premise / Odoo.sh / Odoo Online}} (confirmed) |
| Demo database | {{URL}} / {{DB}} |
| Document language(s) | {{e.g. English, Arabic}} |
| Current stage | {{0–8}} (see STATUS.md) |

## Documents
| # | Document | Status | Version | Updated |
|---|---|---|---|---|
| 01 | [Requirements](01_requirements.md) | Draft | 0.1 | |
| 02 | [Questions & Decisions](02_open_questions_and_decisions.md) | Draft | 0.1 | |
| 03 | [Fit-Gap Matrix](03_fit_gap_matrix.md) | Draft | 0.1 | |
| 04 | [Technical Limitations](04_technical_limitations.md) | Draft | 0.1 | |
| 05 | [Demo DB Configuration Log](05_demo_db_configuration_log.md) | Draft | 0.1 | |
| 06 | [Project Phases](06_project_phases.md) | Draft | 0.1 | |
| 07 | [Workflow Explanation](07_workflow_explanation.md) | Draft | 0.1 | |
| 08 | [Review Guide](08_review_guide.md) | Draft | 0.1 | |
| 09 | [Customization Specs](09_customization_specs.md) | Draft | 0.1 | |

## Change Log
| Date | Version | Change | By |
|---|---|---|---|
EOF

cat > "$T/01_requirements.md" <<'EOF'
# 01 – Requirements

Priority: **Must Have** = go-live blocker; **Nice to Have** = has a workaround. *Proposed* means not yet confirmed by the client.

| ID | Area | Client wording (verbatim) | Interpreted requirement | Source | Priority | Confirmed by | Status |
|---|---|---|---|---|---|---|---|
| REQ-001 | | | | | Must / Nice / *Proposed* | | Open |

## Summary
| Area | Must Have | Nice to Have | Total |
|---|---|---|---|
EOF

cat > "$T/02_open_questions_and_decisions.md" <<'EOF'
# 02 – Open Questions & Decision Log

> Policy: nothing is assumed. Every unknown is a question. Every answer becomes a decision.

## Open Questions
| Q-ID | Area | Question | Why it matters | Options / Odoo standard | Blocking | Asked on | Status |
|---|---|---|---|---|---|---|---|
| Q-001 | | | | | Y/N | | Open |

## Decisions
| DEC-ID | Q-ID | Decision | Rationale | Decided by | Date | Status (Proposed/Confirmed) |
|---|---|---|---|---|---|---|
| DEC-001 | Q-001 | | | | | |
EOF

cat > "$T/03_fit_gap_matrix.md" <<'EOF'
# 03 – Fit-Gap Matrix

Legend: STD Standard · CFG Configuration · STU Studio/Low-code (Enterprise) · CUS Customization · LIM Technical Limitation.
Effort is **indicative**, shown as a range in hours (h) or days (d).

| REQ | Requirement | Priority | Category | Module(s) | Why | How | Effort | Risk | Phase |
|---|---|---|---|---|---|---|---|---|---|

## Summary
| Category | Must Have | Nice to Have | Effort range |
|---|---|---|---|
| STD | | | |
| CFG | | | |
| STU | | | |
| CUS | | | |
| LIM | | | n/a |
| **Overheads** (testing ~20%, PM ~10–15%, training, migration) | | | |
| **Total** | | | |
EOF

cat > "$T/04_technical_limitations.md" <<'EOF'
# 04 – Technical Limitations Register

| LIM-ID | REQ | Limitation | Root cause (edition / hosting / core design) | Business impact | Alternatives offered | Client decision (DEC) |
|---|---|---|---|---|---|---|
| LIM-001 | | | | | 1. … 2. … | |
EOF

cat > "$T/05_demo_db_configuration_log.md" <<'EOF'
# 05 – Demo Database Configuration Log

Database: {{DB}} · URL: {{URL}} · Built on: {{date}} · Raw audit trail: `logs/actions.jsonl`

| # | REQ / DEC | What was done | UI path (how to see it) | Technical (model / field / value) | Why | Done by | Verified |
|---|---|---|---|---|---|---|---|
| 1 | – | Database created / existing empty DB used | Settings › General | – | Stage 5 start | agent | |

## Installed modules
| Module | Reason (REQ) |
|---|---|

## Demo data created
| Model | Records | Prefix / reference |
|---|---|---|
EOF

cat > "$T/06_project_phases.md" <<'EOF'
# 06 – Project Phases

> Rule: all custom development (CUS) and integrations are in the **last phase**.

```mermaid
flowchart LR
  P1["Phase 1 Foundation"] --> P2["Phase 2 Operations"] --> P3["Phase 3 Enhancements"] --> P4["Phase 4 Development"]
```

## Phase 1 – Foundation
- **Scope (REQs):**
- **Why first:**
- **Prerequisites:**
- **Deliverables:**
- **Acceptance criteria (review scenarios):**
- **Effort (indicative):**
- **Risks & mitigation:**
- **Client key users needed:**
- **Exit gate:** client sign-off

## Phase 2 – Operations
(same structure)

## Phase 3 – Enhancements (Nice to Have, Studio)
(same structure)

## Phase 4 – Development & Integrations
(same structure; link each item to 09_customization_specs.md)

## Interim workarounds for Must Have CUS items
| REQ | Workaround until Phase 4 | Accepted by (DEC) |
|---|---|---|
EOF

cat > "$T/07_workflow_explanation.md" <<'EOF'
# 07 – Business Workflow Explanation

Write one section per business flow (e.g. Order-to-Cash, Procure-to-Pay, Record-to-Report, Manufacturing, Hire-to-Retire).

## WF-01 – {{Flow name}}
**Related:** REQ-…, DEC-…

### Why (design rationale)
- Business goal:
- Client decisions driving the design:
- Why the standard Odoo approach was chosen (or why it was extended):

### How (step by step)
| Step | Role | Action (menu path) | What Odoo does automatically (accounting / stock / notifications) |
|---|---|---|---|
| 1 | | | |

```mermaid
flowchart LR
  A[Step 1] --> B[Step 2]
```

### Configuration it depends on
Links to rows in 05_demo_db_configuration_log.md.

### Gaps in this flow
CUS/LIM items, when they will be addressed (phase), and the interim workaround.
EOF

cat > "$T/08_review_guide.md" <<'EOF'
# 08 – Demo Review Guide

**How to use this guide:** log in to the demo database with the user listed in each scenario. Follow the steps exactly. Compare what you see with the *Expected result*. Mark Pass or Fail and add comments. Every Fail or comment is turned into a question or decision and fixed or planned.

Demo URL: {{URL}} · Database: {{DB}} · Users: see the table below (demo passwords are shared separately)

| Login | Role | Used in scenarios |
|---|---|---|

## RS-01 – {{Scenario name}} (WF-01, REQ-…)
- **Preconditions:**
- **Login as:**

| # | Step (menu path / action) | Expected result | Actual result | Pass/Fail | Comment |
|---|---|---|---|---|---|
| 1 | | | | | |

**Reviewer:** ______ **Date:** ______ **Sign-off:** ☐

## Known gaps (not shown in demo)
| REQ | Category | Planned phase | Note |
|---|---|---|---|

## Overall sign-off
| Area | Reviewer | Result | Date |
|---|---|---|---|
EOF

cat > "$T/09_customization_specs.md" <<'EOF'
# 09 – Customization Specifications (Phase 4)

## CUS-01 – {{Title}} (REQ-…, Priority: Must/Nice)
### Functional
- Problem / business need:
- Why the standard is insufficient (what was evaluated: settings, Studio, OCA/App Store):
- Expected behaviour (user story + acceptance criteria):
- Affected users/roles:

### Technical
- Module name: `{{client}}_{{feature}}` · Depends on:
- Models / fields:
- Views / menus / reports:
- Business logic / hooks (override points):
- Security (groups, record rules):
- Upgrade/migration considerations (16→19):
- Test plan (unit + functional):

### Estimate (indicative)
| Task | Effort |
|---|---|
| Analysis & spec | |
| Development | |
| Testing | |
| Total | |
EOF
echo "Templates written to $T"
