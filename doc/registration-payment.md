# Registration & payment

[← Wiki home](../README.md)

## Phase 1 priority

After the vendor meeting (May 2026), the school confirmed:

> **Registration and course enrollment are the first delivery priority.**

Phase 1 breaks into two parts:

| Part | Document | Status |
|------|----------|--------|
| **A. User & family profiles** | [Registration — user fields](registration-user-fields.md) | Field list from Kyna (`WebSiteUserFields.xlsx`) |
| **B. Course enrollment & payment** | This page (cart, classes, discounts, gateway) | Requirements confirmed; detailed field spec TBD |

Send vendors **both**: profile fields (Excel + wiki) and the enrollment/payment requirements below.

## Diagrams

### 🛒 选课付款一条龙

```mermaid
flowchart LR
  A["👨‍👩‍👧 选孩子"] --> B["📚 挑班级"]
  B --> C["🛒 购物车"]
  C --> D["🏷️ 折扣"]
  D --> E["💳 付款"]
  E --> F["🧾 收据 ✅"]
  style E fill:#d4edda
```

### 🏷️ 三种常见折扣

```mermaid
flowchart TB
  CART["🛒 购物车"] --> E["🐦 早鸟 Early bird"]
  CART --> S["👫 兄弟姐妹 Sibling"]
  CART --> M["📚 多班 Multi-class"]
```

### 👨‍👩‍👧 谁按下付款键

```mermaid
flowchart TB
  PO["⭐ 主家长\n能付款"] --> CHECKOUT["💳 Checkout"]
  SP["配偶\n一般只看"] -.-> CHECKOUT
  CHECKOUT --> OK["✅ 报名成功\n孩子进班级名单"]
```

---

## Overview

Parents register students for **specific classes** and pay tuition/fees through an integrated checkout flow. There is **no** subscription to use the platform itself.

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
| REQ-PAY-07 | Phase 1 includes end-to-end **registration + enrollment + payment**. | Confirmed (May 2026) |

## Admin capabilities

- View all enrollments by class and student
- Export roster / payment reports
- Manual adjustments (waivers, refunds) — process TBD
- Mark students paid offline if needed (check/cash) — recommended

## Open items

| Topic | Notes |
|-------|--------|
| Course catalog fields | Class ID, fee, capacity, schedule — vendor sheet TBD |
| Refund policy | Business rules + UI |
| Waitlist | When class is full |
| Installment plans | Not in consolidated doc — confirm |
| Tax / fee line items | Confirm with school |

## Related documents

- [Parent portal](parent-portal.md)
- [Registration — user fields](registration-user-fields.md)
- [Accounts & enrollment](accounts.md)
- [Platform structure](platform.md)
- [Admin portal](admin-portal.md)
