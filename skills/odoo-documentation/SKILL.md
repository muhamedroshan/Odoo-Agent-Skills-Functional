---
name: odoo-documentation
description: Produce and maintain the complete Markdown documentation set for an Odoo implementation - requirements, questions and decisions, fit-gap matrix, technical limitations, demo DB configuration log, project phases, detailed workflow explanations (why and how), step-by-step review guide and customization specifications - in the client's confirmed language(s).
---

# Odoo Documentation

Templates live in `templates/`. Copy them to `clients/<client>/docs/` at Stage 0 and keep them updated at every stage.

| File | Filled at stage | Purpose |
|---|---|---|
| `00_index.md` | 0 | Project summary, version/edition/hosting, links, document status |
| `01_requirements.md` | 1 | Atomic requirements with priority |
| `02_open_questions_and_decisions.md` | 2 | Questions, answers, decision log |
| `03_fit_gap_matrix.md` | 3 | Category, why/how, effort per requirement |
| `04_technical_limitations.md` | 3 | Limitations, impact, alternatives |
| `05_demo_db_configuration_log.md` | 5 | Every configuration step, reproducible |
| `06_project_phases.md` | 6 | Phase plan and dependencies |
| `07_workflow_explanation.md` | 7 | Each business flow: why it's designed this way, how it works step by step |
| `08_review_guide.md` | 7 | Test scenarios to review the demo, with sign-off |
| `09_customization_specs.md` | 7 | Functional and technical spec for each CUS item |

## Writing rules
- **Language**: use the language(s) confirmed at Stage 0. For bilingual documents, put the second language directly under each section heading (or in a parallel file `*.ar.md`, etc.). Ask which layout the user prefers.
- Every statement must trace back to a REQ, DEC or Q ID. Do not write anything that isn't backed by one.
- **Why and How in every workflow section**:
  - *Why*: the business goal, the client decision behind it, and why the standard Odoo approach was chosen (or why not).
  - *How*: numbered user steps with menu paths, what happens automatically (accounting entries, stock moves), the roles involved, and a mermaid diagram.
- **Review guide scenarios** must be executable by a non-technical reviewer: preconditions, login user, steps, expected result, actual result, Pass/Fail, comments.
- Mark estimates as *indicative*. Mark assumptions as **none**: if you find yourself assuming, go back and ask.
- Bump the version and date in `00_index.md` whenever a document changes. Keep a change log there.
