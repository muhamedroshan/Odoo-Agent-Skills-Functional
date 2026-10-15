# Integrations & Data Migration: Clarification Questions

| # | Question | Why it matters | Default |
|---|---|---|---|
| X1 | Which external systems must integrate (eCommerce, banks, shipping, government portals, BI, legacy ERP)? | Usually CUS → last phase | None |
| X2 | For each integration: direction, frequency (real-time or batch), data volume, API available? | Design and effort | – |
| X3 | Is there a standard Odoo connector for it in this edition and country? | STD/CFG vs CUS | – |
| X4 | Which data to migrate: customers, vendors, products, open invoices, stock, history? | Migration scope | Masters + open items |
| X5 | Source system and format (Excel, CSV, database access)? Who cleans the data? | Effort, responsibilities | Client cleans |
| X6 | How much history to migrate (years)? Is summarized history acceptable? | Effort; full history is often not advisable (LIM) | Open items only |
| X7 | Cut-over date and parallel run? | Phase planning | – |
| X8 | Reporting/BI needs beyond standard reports? | Spreadsheet dashboards (Enterprise) vs custom | Standard reports |
