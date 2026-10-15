---
name: odoo-requirements-analysis
description: Turn raw client requirements into numbered, atomic Odoo requirements, generate clarification questions per business area (accounting, sales, purchase, inventory, manufacturing, HR, POS, website, projects, access rights, integrations, data migration) and confirm Must Have vs Nice to Have priorities with the user. Never assumes; every unknown becomes a question.
---

# Odoo Requirements Analysis

## Step 1: Atomize
For every statement the client makes, create one row in `docs/01_requirements.md`:

| ID | Area | Client wording (verbatim) | Interpreted requirement | Source | Priority | Status |
|---|---|---|---|---|---|---|
| REQ-001 | Sales | "we give discounts by customer" | Customer-specific pricing | Email 2026-10-14 | *TBC* | Open |

- One requirement = one testable behaviour. Split compound sentences.
- The *Interpreted requirement* column must not add facts. Anything interpreted becomes a question.

## Step 2: Generate questions
For each area mentioned (and for the **mandatory areas**: Company/Localization, Accounting and Users/Access, which are always reviewed), read the matching bank in `references/questions/`:

- `company_localization.md`, `accounting.md`, `sales_crm.md`, `purchase.md`, `inventory.md`, `manufacturing.md`, `hr_payroll.md`, `pos_ecommerce.md`, `project_services.md`, `users_access.md`, `integrations_migration.md`

Only ask questions that are **relevant and not already answered**. Log each one in `02_open_questions_and_decisions.md`:

| Q-ID | Area | Question | Why it matters | Options / Odoo default | Blocking | Answer | DEC-ID |

## Step 3: Ask (never assume)
- Present the questions to the user grouped by area, at most 10 per batch, blocking questions first.
- For each question, say what the Odoo standard behaviour is, so the user can simply answer "standard is fine".
- **STOP and wait.** Do not continue with a guessed default. If the user says "you decide", write your recommendation as a decision marked `Proposed`, and get an explicit OK.

## Step 4: Prioritize
Ask the user to confirm each requirement as:
- **Must Have**: go-live is impossible or not accepted without it (legal, core operations, client's stated deal-breakers).
- **Nice to Have**: improves efficiency or reporting; there is a manual or standard workaround.

You may propose a priority with a reason, but mark it `Proposed` until the user confirms.

## Output checklist
- [ ] Every client statement maps to at least one REQ.
- [ ] Every REQ has a confirmed priority.
- [ ] No blocking question is open.
- [ ] Decisions are dated and attributed (who answered).
