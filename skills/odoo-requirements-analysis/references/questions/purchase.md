# Purchase: Clarification Questions

| # | Question | Why it matters | Default |
|---|---|---|---|
| P1 | Are RFQs sent to several vendors? Call for tenders / blanket orders? | `purchase_requisition` | Single RFQ |
| P2 | PO approval levels (amount thresholds, approvers)? | Standard 2-step approval vs custom multi-level | No approval |
| P3 | Vendor pricelists and lead times maintained per product? | Vendor pricelists, replenishment | – |
| P4 | Bill control: on ordered or received quantities? Is 3-way matching required? | Bill control policy | Received qty |
| P5 | Automatic replenishment (min/max, MTO)? | Reordering rules, routes | Manual |
| P6 | Purchase requests from employees before the RFQ? | Custom, or Approvals (Enterprise) | None |
| P7 | Import purchases: landed costs (freight, duty)? | `stock_landed_costs` | None |
| P8 | Purchasing in foreign currencies? | Multi-currency | Company currency |
| P9 | Dropshipping? | Route configuration | No |
