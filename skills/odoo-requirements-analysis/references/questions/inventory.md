# Inventory: Clarification Questions

| # | Question | Why it matters | Default |
|---|---|---|---|
| I1 | Number of warehouses and locations? Sub-locations or bins? | Warehouse/location setup | 1 warehouse |
| I2 | Receipt steps (1/2/3) and delivery steps (1/2/3: pick/pack/ship)? | Routes | 1 step |
| I3 | Lot or serial number tracking? Expiry dates? | `product_expiry`, tracking | None |
| I4 | Costing method (Standard/AVCO/FIFO) and valuation (periodic/automated)? (Link to accounting A14) | Valuation entries | Standard / periodic |
| I5 | Removal strategy (FIFO/LIFO/FEFO/closest)? | Putaway/removal | FIFO |
| I6 | Barcode scanning? Which devices? | Enterprise `stock_barcode` | No |
| I7 | Inter-warehouse transfers? Resupply routes? | Routes | None |
| I8 | Cycle counts or annual inventory? | Inventory adjustments | Manual |
| I9 | Consignment stock (owned by others)? | Owner setting | No |
| I10 | Packaging units, weights and volumes needed? | Product packaging | No |
| I11 | Negative stock allowed? | Process rule | Allowed |
| I12 | Opening stock: quantities, values, lots as of which date? | Migration | – |
