# Registration & payment

[← Wiki home](../README.md)

## Phase 1 priority

**Phase 1** includes the **public homepage** and **registration / course enrollment**.

Phase 1 registration breaks into:

| Part | Document | Status |
|------|----------|--------|
| **Public homepage** | [Public homepage](public-homepage.md), [About](about-school.md) | Confirmed — phase 1 |
| **A. User & family profiles** | [Registration — user fields](registration-user-fields.md) | [`WebSiteUserFields.xlsx`](WebSiteUserFields.xlsx) |
| **B. Course enrollment & payment** | This page (cart, classes, discounts, gateway) | Requirements confirmed |

Implement profile fields per [user fields](registration-user-fields.md) and the enrollment/payment requirements below.

## Backend configuration

| Frontend (dynamic) | Configure in admin |
|--------------------|-------------------|
| Cart line prices & discounts | **Admin → Pricing → Tuition rules** · **Admin → Pricing → Discount rules** |
| Course offerings & capacity | **Admin → Academic year → Courses** · **Admin → Enrollment → Capacity** |
| Payment (Stripe / Square) | **Admin → Settings → Payment gateways** |
| Paid / unpaid status | **Admin → Enrollment → Payments** |

Full map: **[Frontend ↔ backend configuration map](frontend-backend-config.md#registration--checkout)**.

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Enrollment and payment

![Enrollment and payment](assets/diagrams/payment-cart.svg)

### Discount types

![Discount types](assets/diagrams/payment-discounts.svg)

### Who can checkout

![Who can checkout](assets/diagrams/payment-checkout.svg)


## Overview

Parents register students for **specific classes** and pay tuition/fees through an integrated checkout flow. There is **no** subscription to use the platform itself.

Payment status drives **roster eligibility**: students should appear as enrolled in class rosters only when the business rules say they are paid (or explicitly waived by admin). Unpaid carts do not hold seats indefinitely unless the school configures a hold window (TBD).

## User flow

```
Register / verify mobile ──► Complete profile (Self) ──► Add Spouse / Child
    ──► Select student(s) ──► Browse classes ──► Cart ──► Discounts ──► Pay ──► Receipt
```

See [Registration — user fields](registration-user-fields.md) for steps before class selection. Enrollment and checkout live in the **[Parent portal](parent-portal.md)**.

## Class selection

- Browse offerings aligned with [school structure](school-structure.md) (grade, class section, schedule)
- Use student **Date of Birth** and **Current Grade at Regular School** to suggest or restrict levels (rules TBD)
- Enforce prerequisites or capacity limits if school defines them (TBD)
- One cart may include multiple students and multiple classes
- Catalog browse may happen **before** login; cart and checkout require a signed-in primary owner (or continuation of registration wizard)

### Placement and capacity

| Rule | Behavior |
|------|----------|
| **DOB + regular-school grade** | Suggest or filter class levels; hard blocks only if school configures them |
| **Capacity** | When class is full, show waitlist or “full” per admin setting |
| **Prerequisites** | Optional; block add-to-cart or warn at review (TBD) |
| **Excluded discount courses** | Listed in [tuition policies](tuition-policies.md); full price at checkout |

## Discounts

| Type | Status |
|------|--------|
| Early bird | Confirmed (concept) |
| Sibling | Confirmed (concept) |
| Multi-class | Confirmed (concept) |

*Exact rules, amounts, and date windows — define with school business office.*

Discount evaluation order (recommended): compute **line price** (including early bird by date) → apply **at most one** qualifying policy discount per course unless school updates stacking → show breakdown on review screen. Legacy policy: discounts **do not combine** — see [tuition-policies.md](tuition-policies.md).

### Workflow — checkout (primary owner)

1. Select student(s) and add classes to cart from catalog or parent portal.
2. Review line items: course name, schedule summary, base fee, early bird adjustment, applied policy discount.
3. Confirm total; redirect to payment gateway (Stripe or Square).
4. On success: mark enrollment **paid**, send receipt, show confirmation with class list.
5. On failure: keep cart intact; show retry; do not create duplicate charges for the same cart session.

### Workflow — admin payment oversight

1. Admin opens **Enrollment → Payments** for the active season.
2. Filters unpaid, partial, or disputed families; exports roster/payment report.
3. Records offline payment (check/cash) or issues refund per school process; roster updates accordingly.

### Acceptance criteria

- Cart supports multiple students and multiple classes in one checkout session.
- Prices and early-bird deadlines match **Admin → Courses → Pricing** and **Pricing → Tuition rules** without code changes.
- Configured discounts appear as separate lines on the review step; excluded courses never receive policy discounts.
- Only the **primary owner** can submit payment; spouse sees cart state if permitted but cannot complete pay.
- Successful card payment sets status to **paid**, generates a receipt (email and/or download), and updates admin enrollment views.
- Failed or abandoned payment does not mark students as paid on the roster.
- Admin can mark paid offline and export enrollment/payment reports for the season.

### Edge cases

- **Cart abandoned overnight** — early-bird eligibility recalculates at payment time based on current date rules.
- **Class becomes full while in cart** — block checkout for that line or offer waitlist; message names the class.
- **Partial payment** — if school allows installments (TBD), track **partial** status and block roster until satisfied.
- **Duplicate enrollment** — same student + same class in cart twice should be prevented.
- **Refund after pay** — admin adjusts status to refunded and removes or freezes roster seat per policy.
- **Discount rule change mid-checkout** — recalculate on review/submit; show notice if total changed.
- **Gateway timeout** — idempotent retry; admin reconciles via payment dashboard if charge succeeded but UI failed.
- **Primary owner transfer** — only new primary owner can pay open carts after admin reassignment.

## Payment integration

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-PAY-01 | Integrate payment gateway (**Stripe**, **Square**, or similar). | Confirmed |
| REQ-PAY-02 | Track payment status: paid / unpaid / partial. | Confirmed |
| REQ-PAY-03 | Generate or email **receipts** on successful payment. | Confirmed |
| REQ-PAY-04 | Only **primary owner** completes checkout (billing). | Implied |
| REQ-PAY-05 | Admin dashboard for enrollment and payment tracking. | Confirmed |
| REQ-PAY-06 | Admin can manage rosters tied to payment status. | Confirmed |
| REQ-PAY-07 | Phase 1 includes end-to-end **registration + enrollment + payment**. | Confirmed |

## Admin capabilities

- View all enrollments by class and student
- Export roster / payment reports
- Manual adjustments (waivers, refunds) — process TBD
- Mark students paid offline if needed (check/cash) — recommended
- Reconcile gateway payouts with internal payment reports (export format TBD)

### Receipt content (minimum)

| Field | Included |
|-------|----------|
| Family / payer name | Yes |
| Payment date and transaction reference | Yes |
| Per-class lines with student name | Yes |
| Discount breakdown | Yes |
| School contact for billing questions | Yes |

## Open items

| Topic | Notes |
|-------|--------|
| Course catalog fields | Class ID, fee, capacity, schedule — vendor sheet TBD |
| Refund policy | Business rules + UI |
| Waitlist | When class is full |
| Installment plans | Confirm with school |
| Tax / fee line items | Confirm with school |

## Related documents

- [Parent portal](parent-portal.md)
- [Registration — user fields](registration-user-fields.md)
- [Accounts & enrollment](accounts.md)
- [Platform structure](platform.md)
- [Admin portal](admin-portal.md)
