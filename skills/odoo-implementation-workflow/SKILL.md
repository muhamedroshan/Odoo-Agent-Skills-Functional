---
name: odoo-implementation-workflow
description: Orchestrator for an end-to-end Odoo implementation or pre-sales engagement. Takes client requirements through intake, mandatory clarification (never assume), fit-gap categorization, Must/Nice prioritization, demo database build, phased roadmap (custom development last), full documentation and review guides. Use when a user gives client requirements or asks to plan, analyze or demo an Odoo project.
---

# Odoo Implementation Workflow (Orchestrator)

This skill drives the other skills **in a fixed order with gates**. Never skip a gate.

```
0 Setup → 1 Intake → 2 Clarify ⟲ → 3 Fit-Gap → 4 Approval → 5 Demo DB → 6 Phasing → 7 Docs → 8 Review
```

## Golden rules
1. **Do not assume anything.** If a fact is not stated by the user or the client, it is an *open question*. Write it down and ask.
2. **Be as standard as possible.** Prefer Standard over Configuration, Configuration over Studio, and Studio over Custom code. Justify every step up that ladder.
3. **No silent changes.** Every change on the server is logged, documented and tied to a requirement ID.
4. **Custom development always goes in the last phase.**
5. **Explain why and how** for every decision, so a reviewer can follow it.

## Stage 0: Setup
- Ask: client name, **Odoo version** (16/17/18/19), **edition and hosting** (Community / Enterprise / Odoo.sh / Odoo Online). You must get explicit confirmation even if you can detect it.
- Ask the **document language(s)**, e.g. English only, or English + Arabic.
- Create the workspace: copy `skills/odoo-documentation/templates/*` to `clients/<client_slug>/docs/`. Set `ODOO_CLIENT_DIR=clients/<client_slug>`.
- Connect using **odoo-connect** (use the empty database if given, otherwise ask for the master password).

## Stage 1: Intake (skill `odoo-requirements-analysis`)
Split the raw requirements into atomic `REQ-###` items in `01_requirements.md`. Keep the client's original wording.

## Stage 2: Clarify (loop, **blocking gate**)
- Go through the question banks in `odoo-requirements-analysis/references/questions/` for every area involved.
- Put every unknown in `02_open_questions_and_decisions.md` with: Why it matters, Options, Impact, and Blocking (Y/N).
- **Ask the user in batches** (at most 10 questions, grouped by area). Then STOP and wait for answers.
- Record answers as `DEC-###` decisions. Repeat until no blocking questions are left.
- Ask whether each requirement is **Must Have** or **Nice to Have**. You may propose a priority, but the user must confirm it.

## Stage 3: Fit-Gap (skill `odoo-fit-gap`)
Classify every requirement (Standard / Configuration / Studio / Customization / Technical Limitation) and estimate effort.

## Stage 4: Approval gate
Show the user a summary of the fit-gap matrix and the planned demo scope. **Do not build the demo until the user approves.**

## Stage 5: Demo DB (skill `odoo-demo-db-builder`)
Build only the Standard and Configuration items (plus Studio items, if Enterprise and approved). Log each step in `05_demo_db_configuration_log.md`.

## Stage 6: Phasing (skill `odoo-project-phasing`)
Produce `06_project_phases.md`, with customization and integrations in the final phase.

## Stage 7: Documentation (skill `odoo-documentation`)
Complete all documents: workflow explanations (why and how), the limitations register, customization specs and the review guide.

## Stage 8: Review
Walk the user through `08_review_guide.md`. Capture their feedback as new questions or decisions, and loop back to the affected stage.

## Progress tracking
Keep `clients/<client>/STATUS.md` updated: current stage, open blocking questions, last action and next step. This lets any agent (Claude Code, Antigravity or Codex) resume the work.
