# Manufacturing: Clarification Questions

| # | Question | Why it matters | Default |
|---|---|---|---|
| M1 | Manufacturing type: make-to-stock, make-to-order, kits, subcontracting? | Routes, BoM type | MTS |
| M2 | Multi-level BoMs? By-products? BoM versions/ECOs? | `mrp`, Enterprise `mrp_plm` | Single level |
| M3 | Work centres and operations (routings) with time tracking? | Work orders, costing | No routing |
| M4 | Shop-floor tablet usage? | Shop Floor (Enterprise) | No |
| M5 | Quality checks at which steps? | Enterprise `quality_control` | None |
| M6 | MRP planning: MPS, reordering rules? | Enterprise `mrp_mps` | Reordering rules |
| M7 | Production costing: include labour and overhead? | Work-centre cost setup | Material only |
| M8 | Maintenance of equipment? | `maintenance` | No |
| M9 | Lot/serial tracking of components and finished goods? | Traceability | None |
