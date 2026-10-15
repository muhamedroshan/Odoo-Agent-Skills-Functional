# Accounting: Clarification Questions
Always review this area. Never set up accounting without confirmed answers.

| # | Question | Why it matters | Odoo standard / default |
|---|---|---|---|
| A1 | Which country's fiscal localization applies to each company? | Sets the chart of accounts, taxes and legal reports | Localization package for the company's country |
| A2 | Use Odoo's standard chart of accounts, or import the client's existing one? | Mapping effort, reporting continuity | Standard localization chart |
| A3 | Fiscal year start and end dates? Is there a fiscal period lock policy? | Year-end closing, lock dates | 1 Jan – 31 Dec |
| A4 | Company currency, and which foreign currencies? Where do exchange rates come from, and how often are they updated? | Multi-currency, revaluation | Single currency |
| A5 | Tax regime (VAT/GST rates, exempt or zero-rated, reverse charge)? Tax registration numbers? | Tax setup, legal invoices | Localization taxes |
| A6 | Are prices tax-included or tax-excluded (B2B vs B2C)? | Tax computation, pricelists | Tax-excluded |
| A7 | Payment terms used for customers and vendors? | Due dates, follow-ups | Immediate payment |
| A8 | Bank accounts, and how are statements obtained (bank sync, CSV/CAMT/OFX import, manual)? | Reconciliation | Manual / import |
| A9 | Cash basis or accrual taxes? | Tax reports | Accrual |
| A10 | Analytic accounting needed (cost centres, projects, departments)? Analytic plans? | Analytic setup | Off |
| A11 | Opening balances: as of which date, at what level of detail (trial balance, open invoices, stock valuation)? | Data migration scope | n/a |
| A12 | Customer credit limits and payment follow-up levels? | Follow-up configuration | Off |
| A13 | Invoice layout/legal mentions, numbering sequence requirements? | Compliance, branding | Standard sequence |
| A14 | Stock valuation: periodic or perpetual (automated)? Costing method (Standard/AVCO/FIFO)? | Accounting entries from inventory | Periodic, Standard price |
| A15 | Who approves vendor bills and payments? Is there a multi-level approval? | Workflow, possible customization | No approval |
| A16 | Multi-company? Inter-company transactions? Consolidation? | Structure, Enterprise features | Single company |
| A17 | Fixed assets, deferred revenue/expenses, budgets needed? | Enterprise modules (`account_asset`, budgets) | Not installed |
| A18 | E-invoicing or regulatory submission obligations (e.g. ZATCA, FTA, Peppol)? | Localization modules, Enterprise/IAP | Depends on country |
| A19 | Edition check: full accounting (Enterprise `account_accountant`) or Invoicing only (Community)? | Bank reconciliation UI, reports | Edition-dependent |
