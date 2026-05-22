# Registration flow (complete guide)

[← Wiki home](../README.md)

**Audience:** The Web Design LLC and school committee.  
**Purpose:** Single end-to-end reference for **phase 1** — public homepage entry, family signup, profiles, class enrollment, and payment.

**Related detail pages:** [User fields](registration-user-fields.md) · [Payment & cart](registration-payment.md) · [Parent portal](parent-portal.md) · [Accounts model](accounts.md) · [Field spreadsheet](WebSiteUserFields.xlsx)

---

## Phase 1 scope

| In scope | Out of scope |
|----------|----------------|
| **Public homepage** (hero, mission, events, announcements) | Full LMS (assignments, etc.) — later phases |
| About, contact, public course catalog (browse) | Gallery, news archive (optional phase 2) |
| Parent **self-registration** | Platform subscription fee |
| Family account + student profiles | Admin-created accounts (except assist) |
| Class selection, cart, discounts, pay | |
| Primary owner pays tuition | |

See [Public homepage](public-homepage.md) and [Public site content](public-site-content.md).

---

## End-to-end flow (summary)

```
Public site (Register) → Sign in / Sign up
  → Sign up (Google / Microsoft / email / phone+SMS)
  → Parent profile (Self) → Family ID created
  → Add Spouse and/or Children (optional)
  → Enroll each child in classes → Cart → Discounts → Pay
  → Confirmation → Parent portal (ongoing)
```

![Complete registration flow](assets/diagrams/registration-flow-complete.svg)

---

## Step 1 — Entry from public site

| Item | Detail |
|------|--------|
| **Where** | Public homepage — [hero / mission / CTA](public-homepage.md) (Register, Sign in, View courses) |
| **Who** | New or returning parent |
| **Outcome** | Directed to registration or login |

Returning users **Sign in** with Google OAuth, Microsoft OAuth, email + password, or phone + SMS (see [Authentication](authentication.md)).

---

## Step 2 — Create account (choose login method)

| # | Option | Flow |
|---|--------|------|
| 2a | **Google OAuth** | OAuth consent → profile completion if needed |
| 2b | **Microsoft OAuth** | OAuth consent → profile completion if needed |
| 2c | **Email + password** | Email → verify email (recommended) → password |
| 2d | **Phone + SMS** | Mobile → SMS OTP → password (optional) |

All paths merge into the same **user** record. User may link additional methods later in settings.

**Requirements:** REQ-AUTH-01, REQ-REG-02, REQ-REG-02b, REQ-REG-03 · See [Authentication](authentication.md).

---

## Step 3 — Parent profile (“Self”)

The registering parent completes their own profile and becomes the **primary owner** of a new **family account**.

| # | Data (English) | Required? |
|---|----------------|-----------|
| 3.1 | Nickname | TBD |
| 3.2 | English first / last name, Chinese name | TBD |
| 3.3 | Gender | TBD |
| 3.4 | WeChat ID, Email | TBD |
| 3.5 | Address, City, State, ZIP | TBD |
| 3.6 | School assigned role(s) | Usually **Parent** |

**System:** Assigns **Family Identifier** (unique family / billing ID).

Full field list: [Registration — user fields](registration-user-fields.md) and `WebSiteUserFields.xlsx`.

![Signup steps](assets/diagrams/registration-signup-steps.svg)

---

## Step 4 — Add family members (optional)

Same account; relationship drives entity type.

| Relationship | Entity | Typical data |
|--------------|--------|--------------|
| **Self** | Already done in step 3 | — |
| **Spouse** | Second parent user | Profile + contact (same field set as parent) |
| **Child** | Student record | Names, gender, date of birth, current regular school, current grade |

| # | Rule |
|---|------|
| 4.1 | Each **child** belongs to **one** family account only |
| 4.2 | **Spouse** does not replace primary owner unless school reassigns |
| 4.3 | Assign **Student** role on child if they will use student portal |

![Family structure](assets/diagrams/accounts-family.svg)

---

## Step 5 — Enroll in classes

Done in the **[Parent portal](parent-portal.md)** (or continuation of registration wizard).

| # | Screen / action | Detail |
|---|-----------------|--------|
| 5.1 | Select student | Which child to enroll |
| 5.2 | Browse catalog | Classes by grade / subject; use DOB + regular-school grade for placement hints |
| 5.3 | Add to cart | Multiple students and multiple classes allowed |
| 5.4 | Apply discounts | Early bird, sibling, multi-class (rules TBD with school) |
| 5.5 | Review cart | Fees per class, discount lines, total |

![Enrollment and payment](assets/diagrams/payment-cart.svg)

---

## Step 6 — Payment & confirmation

| # | Screen / action | Detail |
|---|-----------------|--------|
| 6.1 | Checkout | **Primary owner only** completes payment |
| 6.2 | Pay | Stripe, Square, or similar |
| 6.3 | Confirmation | Success message, enrollment summary |
| 6.4 | Receipt | Email or download; payment status **paid** on account |

**Requirements:** REQ-PAY-01 through REQ-PAY-07 · See [Registration & payment](registration-payment.md).

![Who can checkout](assets/diagrams/payment-checkout.svg)

---

## Step 7 — After registration

| User | What they get |
|------|----------------|
| **Primary parent** | Parent portal: all children, billing, enrollment history |
| **Spouse** | Parent portal (view/manage per permissions; pay only if policy changes) |
| **Student** | Student portal when credentials exist (class schedule, homework) |
| **Admin** | Roster updated; payment and enrollment visible in admin tools |

---

## Alternate path — admin-assisted registration

| When | Flow |
|------|------|
| Parent cannot complete online | Admin creates or fixes account, student, enrollment |
| Policy | **Not** the primary path; audit who created/changed records |

See REQ-ACC-03 in [Accounts & enrollment](accounts.md).

---

## Requirements checklist (phase 1)

| ID | Requirement |
|----|-------------|
| REQ-ACC-01 | Parents self-register |
| REQ-ACC-02 | Parents create and manage student profiles |
| REQ-ACC-04 | One primary owner per family account |
| REQ-REG-01 – 09 | Profile fields and phase 1 priority |
| REQ-PAY-01 – 07 | Cart, discounts, gateway, receipts, admin tracking |

---

## Open items (confirm with school)

| Topic | Question |
|-------|----------|
| Required fields | Mandatory on first visit vs complete later? |
| Student login | Own credentials for young students, or parent-only view? |
| Discount rules | Amounts, dates, stacking |
| Class catalog | Capacity, waitlist, prerequisites |
| Registration wizard | One continuous flow vs separate “profile” then “enroll” screens |

---

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Complete flow

![Complete registration flow](assets/diagrams/registration-flow-complete.svg)

### Profile vs enrollment

![Registration sequence](assets/diagrams/accounts-registration-flow.svg)

---

## Document map

| Need | Read |
|------|------|
| Every form field | [registration-user-fields.md](registration-user-fields.md), [WebSiteUserFields.xlsx](WebSiteUserFields.xlsx) |
| Cart, discounts, payments | [registration-payment.md](registration-payment.md) |
| Discount/refund rules | [tuition-policies.md](tuition-policies.md) |
| Browse courses (public) | [public-site-content.md](public-site-content.md) |
| Mission & trust pages | [about-school.md](about-school.md) |
| Account / family rules | [accounts.md](accounts.md) |
| Parent UI after signup | [parent-portal.md](parent-portal.md) |
| Login methods | [authentication.md](authentication.md) |
