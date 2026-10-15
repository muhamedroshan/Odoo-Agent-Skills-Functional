---
name: odoo-project-phasing
description: Segment an Odoo implementation into phases using fit-gap category, Must/Nice priority and dependencies - foundation and standard Must Haves first, configuration and Nice to Haves next, all custom development and integrations last - with scope, prerequisites, deliverables, acceptance criteria, effort and risks per phase.
---

# Odoo Project Phasing

## Phase rules
| Phase | Contents | Why this order |
|---|---|---|
| **Phase 1: Foundation** | Company, localization, accounting setup, users/access, master data, STD/CFG **Must Haves** of the core flows | Every other module posts to accounting and relies on master data |
| **Phase 2: Operations** | Remaining STD/CFG Must Haves (inventory routes, purchase, manufacturing, POS…), data migration of opening balances | Builds on the foundation; this is the earliest possible go-live |
| **Phase 3: Enhancements** | STD/CFG **Nice to Haves**, Studio items, reports and dashboards | Low-risk value adds once users are stable on the standard |
| **Phase 4: Development (always last)** | Every **CUS** item and every integration, Must Have or not | Needs specs, development, code review and testing cycles. Doing standard first often shrinks or removes the custom work |

Special cases. **Ask the user** about these. Do not decide them yourself:
- A **Must Have CUS** item that blocks go-live: still plan it in Phase 4, but propose an interim workaround for Phases 1–3 or a go-live after Phase 4. The user chooses.
- LIM items are not phased. They go in the limitations register with their agreed alternative.

## Dependency ordering
Within a phase, order the items by dependency: Accounting → Products/Partners → Purchase/Sales → Inventory → Manufacturing → Reporting. Draw a mermaid flowchart of the dependencies.

## For each phase, document
- Scope (the REQ list), prerequisites, deliverables
- Acceptance criteria (they link to the review guide scenarios)
- Effort (the sum of fit-gap ranges plus overheads), labelled *indicative*
- Risks and mitigations, and which client roles must take part (key users)
- An exit gate: client sign-off before the next phase starts

Output: `docs/06_project_phases.md`.
