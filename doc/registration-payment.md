# Registration & payment

[← Wiki home](../README.md)

## Overview

Parents register students for **specific classes** and pay tuition/fees through an integrated checkout flow. There is **no** subscription to use the platform itself.

## User flow

```
Select student(s) → Browse classes by grade/category → Add to cart
    → Apply discounts → Pay (Stripe/Square/etc.) → Confirmation & receipt
```

## Class selection

- Browse offerings aligned with [school structure](school-structure.md) (grade, class section, schedule)
- Enforce prerequisites or capacity limits if school defines them (TBD)
- One cart may include multiple students and multiple classes

## Discounts

| Type | Status |
|------|--------|
| Early bird | Confirmed (concept) |
| Sibling | Confirmed (concept) |
| Multi-class | Confirmed (concept) |

*Exact rules, amounts, and date windows — define with school business office.*

## Payment integration

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-PAY-01 | Integrate payment gateway (**Stripe**, **Square**, or similar). | Confirmed |
| REQ-PAY-02 | Track payment status: paid / unpaid / partial. | Confirmed |
| REQ-PAY-03 | Generate or email **receipts** on successful payment. | Confirmed |
| REQ-PAY-04 | Only **primary owner** completes checkout (billing). | Implied |
| REQ-PAY-05 | Admin dashboard for enrollment and payment tracking. | Confirmed |
| REQ-PAY-06 | Admin can manage rosters tied to payment status. | Confirmed |

## Admin capabilities

- View all enrollments by class and student
- Export roster / payment reports
- Manual adjustments (waivers, refunds) — process TBD
- Mark students paid offline if needed (check/cash) — recommended

## Open items

| Topic | Notes |
|-------|--------|
| Refund policy | Business rules + UI |
| Waitlist | When class is full |
| Installment plans | Not in consolidated doc — confirm |
| Tax / fee line items | Confirm with school |

## Related documents

- [Accounts & enrollment](accounts.md)
- [Platform structure](platform.md)
- [Admin portal](admin-portal.md)
