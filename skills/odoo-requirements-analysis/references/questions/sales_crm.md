# Sales & CRM: Clarification Questions

| # | Question | Why it matters | Default |
|---|---|---|---|
| S1 | Is a CRM pipeline needed (leads → opportunities)? Pipeline stages? Sales teams? | Install `crm`, team setup | No CRM |
| S2 | Quotation approval or discount limits? Who approves? | Standard discount lock vs Studio/custom | No approval |
| S3 | Pricing: fixed list, per customer, per quantity, per date, per currency? | Pricelists (CFG) | Single price |
| S4 | Discounts at line level, global, or promotions/coupons? | `sale_loyalty`, settings | Line discount off |
| S5 | Product variants (size, colour…)? Configurable products? | Attributes setup | No variants |
| S6 | Quotation templates, optional products, online signature/payment? | `sale_management`, portal | Off |
| S7 | Invoicing policy: on ordered quantities or delivered quantities? Down payments? | Invoice flow | Ordered quantities |
| S8 | Delivery charges? Which carriers? | `delivery` + carrier connectors | None |
| S9 | Commissions for salespeople or agents? | Enterprise `sale_commission` or custom | None |
| S10 | Required documents and layout (quotation, pro-forma, order confirmation)? | Reports | Standard |
| S11 | Subscriptions / recurring billing? | Enterprise `sale_subscription` | No |
| S12 | Credit limit blocking on sales orders? | Accounting setting vs custom | Warning only |
