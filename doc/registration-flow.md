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

### Phase 1 acceptance criteria (end-to-end)

- A new visitor can start from the public homepage, complete account creation, enroll in one or more classes (as an adult learner, or by adding children as students), pay as primary owner, and land in the parent portal with paid status visible.
- A returning parent can sign in, add classes for an existing student, and pay without re-entering family ID.
- Registration closed season shows clear messaging on homepage and blocks new enrollments while preserving sign-in.
- Admin can complete or fix a family record via assisted registration with audit trail.
- All dynamic steps (catalog, cart, prices, registration window) reflect admin configuration without deploy.

### Edge cases (flow-level)

- **Split wizard vs single flow** — school may require profile completion before catalog; system must not lose cart when user signs out mid-flow.
- **OAuth without mobile on file** — prompt for required fields before enrollment if phone is mandatory for school contact.
- **Zero children at enroll step** — allowed; adult learners can enroll themselves in adult classes without adding any children. The enrollment screen must let a parent-role user select themselves as the enrollee when no children are present.
- **Spouse attempts checkout** — deny with explanation and name of primary owner contact.
- **Class full at pay** — reconcile cart before gateway charge.
- **Browser back after pay** — show confirmation, not double charge.

## Backend configuration

Every dynamic step (homepage, catalog, cart, payment) maps to an admin screen — **[Frontend ↔ backend configuration map](frontend-backend-config.md)**.

---

## End-to-end flow (summary)

```
Public site (Register) → Sign in / Sign up
  → Sign up (Google / Microsoft / email / phone+SMS)
  → Parent profile (Self) → Family ID created
  → Add Spouse and/or Children (optional)
  → Enroll self (adult classes) and/or each child in classes → Cart → Discounts → Pay
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

| Acceptance criteria | Edge cases |
|---------------------|------------|
| Register and Sign in CTAs visible above the fold on mobile and desktop | User bookmarks old `/register` URL — redirect to new flow |
| Logged-in user clicking Register goes to parent portal or enrollment, not duplicate signup | Session expired mid-flow — return to login with cart preserved if possible |

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

| Acceptance criteria | Edge cases |
|---------------------|------------|
| All four login methods create or attach to one user record | Same email used for Google and email/password — offer account linking |
| SMS OTP expires and can be resent with rate limit | International phone format — confirm supported countries with vendor |
| User can link additional login methods later in settings | Child attempts to register as primary — block or route to parent flow (TBD) |

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

| Acceptance criteria | Edge cases |
|---------------------|------------|
| Family Identifier assigned before adding children | User refreshes during step 3 — no duplicate family accounts |
| Registrant becomes primary owner automatically | Admin later changes primary owner — billing follows new owner |
| Required fields enforced per admin profile-field config | Address optional at signup but required before pay — clear messaging |

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

| Acceptance criteria | Edge cases |
|---------------------|------------|
| Each child is a Student on the same family account | Duplicate child name — allow but warn; duplicate student policy TBD |
| Spouse added as User with relationship Spouse, not primary owner | Spouse needs pay rights — only via policy change or admin |
| Student role assigned when child will use student portal | Under-age student login — parent-only until credentials policy set |

---

## Step 5 — Enroll in classes

Done in the **[Parent portal](parent-portal.md)** (or continuation of registration wizard).

| # | Screen / action | Detail |
|---|-----------------|--------|
| 5.1 | Select enrollee | Self (adult classes) or one or more children; if no children on file, defaults to self |
| 5.2 | Browse catalog | Classes by grade / subject; use DOB + regular-school grade for placement hints |
| 5.3 | Add to cart | Multiple students and multiple classes allowed |
| 5.4 | Apply discounts | Early bird, sibling, multi-class (rules TBD with school) |
| 5.5 | Review cart | Fees per class, discount lines, total |

![Enrollment and payment](assets/diagrams/payment-cart.svg)

| Acceptance criteria | Edge cases |
|---------------------|------------|
| Catalog respects registration season open/closed | User adds class then admin closes season — validate at checkout |
| Cart shows fees, discounts, and total before gateway | Sibling discount across two students in one cart — one discount per rules |
| Waitlist or full class handled before pay | Placement suggestion ignored by parent — allow override if school permits |

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

| Acceptance criteria | Edge cases |
|---------------------|------------|
| Only primary owner reaches payment gateway | Payment succeeds but email fails — receipt still in portal |
| Receipt and paid status within one minute of success | Double-click pay — idempotent charge |
| Enrollment summary lists student, class, schedule snippet | Partial refund later — portal shows updated status |

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

| Acceptance criteria | Edge cases |
|---------------------|------------|
| Admin action logged with staff user and timestamp | Admin creates duplicate enrollment — detect and merge |
| Family notified when admin completes enrollment on their behalf | Wrong student assigned to class — admin correction without new payment |

### Workflow — committee UAT (recommended)

1. Browse public homepage and catalog as anonymous user.
2. Register new family with phone path; add two children; enroll each in different classes.
3. Apply early bird and sibling scenarios in separate test accounts.
4. Complete Stripe/Square test payment; verify receipt and admin payment row.
5. Sign in as spouse; confirm cannot pay.
6. Close registration season in admin; confirm public CTA and cart behavior.

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
