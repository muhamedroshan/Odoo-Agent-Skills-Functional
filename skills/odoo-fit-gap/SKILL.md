---
name: odoo-fit-gap
description: Classify each Odoo requirement as Standard, Configuration, Studio/Low-code, Customization or Technical Limitation, with justification (why), approach (how), affected modules, effort estimate and workaround. Hosting/edition aware (Community, Enterprise, Odoo.sh, Odoo Online). Use after requirements are clarified and before building a demo or phasing.
---

# Odoo Fit-Gap Analysis

## Categories (use the lowest one that works)
| Code | Category | Definition | Example |
|---|---|---|---|
| STD | **Standard** | Works out of the box once the app is installed | Quotation → Sales Order → Invoice |
| CFG | **Configuration** | Standard features enabled or set up through settings or master data, no code | Pricelists, multi-step delivery routes, approval rules |
| STU | **Studio / Low-code** | Enterprise Studio, automation rules, server actions, report tweaks. **Enterprise only** | Extra field on SO, simple approval automation |
| CUS | **Customization** | Needs a custom Python/XML/JS module | New business object, complex pricing engine, API integration |
| LIM | **Technical Limitation** | Not feasible, not advisable, or blocked by edition or hosting | Custom module on Odoo Online; changing core accounting principles |

Edition and hosting rules:
- Community: STU is not available. Re-classify those items as CUS, or CFG if an automation without Studio is possible (`base_automation` is in Community).
- Odoo Online: every CUS item becomes **LIM**, unless the client accepts moving to Odoo.sh. Ask the user about this.
- Check that the module exists in the edition, e.g. `account_accountant`, `mrp_plm`, `quality`, `helpdesk` and `hr_payroll` are Enterprise. Verify on the server with `odoo_client.py search-read ir.module.module`.

## For each requirement, record
| REQ | Category | Module(s) | Why (justification) | How (approach) | Effort | Risk | Workaround if LIM | Priority | Phase |

- **Why**: which standard feature covers it, or why the standard is insufficient (cite the exact menu or behaviour).
- **How**: the menu path and settings, or for CUS a short technical design (models, fields, views, hooks).
- **Effort** (estimate only, always shown as a range and labelled *indicative*):
  | Size | CFG/STU | CUS |
  |---|---|---|
  | XS | < 1 h | < 4 h |
  | S | 1–4 h | 0.5–2 d |
  | M | 0.5–1 d | 2–5 d |
  | L | 1–3 d | 5–15 d |
  | XL | > 3 d | > 15 d (split it) |
  Add standard overheads separately: testing about 20%, project management about 10–15%, and training and data migration as their own lines.

## Before escalating to CUS, always check
1. Is there a standard setting? (Search Settings and the module's configuration menu.)
2. Can a process change by the client make the standard version work? **Ask the client.** Do not decide for them.
3. Would a report or filter be enough?
4. Is there an Odoo Apps / OCA module? Note it as an option with its licence and maintenance risk. Ask before using it.

## Outputs
- `docs/03_fit_gap_matrix.md` (+ `fit_gap_matrix.csv` with the same columns)
- `docs/04_technical_limitations.md`: every LIM item with its reason, its impact and the alternatives offered
- A summary: counts per category × priority, and total effort ranges.
