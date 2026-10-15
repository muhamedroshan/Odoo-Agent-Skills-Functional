# Users & Access Rights: Clarification Questions
Always review this area.

| # | Question | Why it matters | Default |
|---|---|---|---|
| U1 | List of roles (e.g. sales user, sales manager, accountant, warehouse operator)? | Group mapping | – |
| U2 | Should users see only their own records (e.g. own leads/orders)? | Standard "own documents" groups vs record rules | All documents |
| U3 | Restrictions per company, warehouse or branch? | Multi-company rules; per-warehouse restriction is often CUS | – |
| U4 | Field-level restrictions (e.g. hide cost price)? | Groups on fields: Studio/CUS | – |
| U5 | Two-factor authentication or password policy? | `auth_totp`, `auth_password_policy` | Optional |
| U6 | SSO (Google, Microsoft, LDAP)? | `auth_oauth`, `auth_ldap` | None |
| U7 | Portal users (customers/vendors) and their access? | Portal groups | None |
| U8 | Audit trail requirements? | Chatter tracking; full audit log may be CUS or OCA | Chatter |
