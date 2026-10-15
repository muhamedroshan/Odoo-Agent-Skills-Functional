---
name: odoo-demo-db-builder
description: Build a client demo database in Odoo strictly from approved Standard/Configuration (and Studio if Enterprise) fit-gap items - install apps, set company and localization, configure settings per confirmed decisions, seed realistic demo master data and sample transactions, and log every step for review. Uses odoo-connect. Never fakes customizations.
---

# Odoo Demo DB Builder

**Before you start:** the fit-gap matrix must be approved (orchestrator Stage 4) and there must be no blocking questions. If either is false, STOP.

## Procedure
1. **Database**: if the user gave an empty database, use it. Otherwise, ask for the master password and database name, then `create-db` (demo data off unless the user asks for it). Ask for the language and country. Do not guess them.
2. **Company**: name, address, VAT/TRN, currency, logo, and the fiscal year (all from decisions). If there are several companies, create each one only if the user confirmed it.
3. **Install apps**: install only the modules listed in the fit-gap. Do it one functional group at a time, and check the result with `installed`.
4. **Accounting first** (everything else depends on it): the fiscal localization package / chart of accounts, taxes, currencies, journals, payment terms and bank accounts, all as decided. **Never pick a chart of accounts or tax setup without a DEC-ID.**
5. **Settings**: change `res.config.settings` per decision (create, then `execute`).
6. **Master data**: warehouses, routes, product categories, UoM, products, customers, vendors, pricelists, employees and users with access groups. Use realistic, client-like names given by or confirmed with the user. Mark the data as demo (e.g. ref prefix `DEMO-`).
7. **Sample flows**: create at least one end-to-end transaction for each main business flow (for example SO → delivery → invoice → payment) so reviewers can see it working.
8. **Verify**: read back the key records and settings. Confirm the flows reach the expected states.

## Logging (mandatory)
For **every** step, append a row to `docs/05_demo_db_configuration_log.md`:

| # | REQ / DEC | What was done | UI path (how to see it) | Technical (model/field/value) | Why | Done by | Verified |
|---|---|---|---|---|---|---|---|
| 12 | REQ-007 / DEC-004 | Enabled pricelists | Sales › Configuration › Settings › Pricelists | res.config.settings.group_product_pricelist = True | Customer-specific prices | agent | ✅ |

The script also writes the raw audit trail to `clients/<client>/logs/actions.jsonl`.

## Things you must not do
- Do not create fake fields or hacks to imitate CUS items. List them in the review guide as "Gap: planned in Phase N".
- Do not install extra apps "just in case".
- Do not use production client data unless the user explicitly provides and approves it.
- Do not change security, outgoing mail or other server-level settings without asking. Prefer disabling outgoing mail in the demo, and ask first.
