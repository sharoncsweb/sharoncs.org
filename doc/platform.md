# Platform structure

[← Wiki home](../README.md)

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### One school, one platform

![One school, one platform](assets/diagrams/platform-one-school.svg)

### Platform layers

![Platform layers](assets/diagrams/platform-layers.svg)

### How tuition is collected

![How tuition is collected](assets/diagrams/platform-payment.svg)


## Requirements

| ID | Requirement | Acceptance criteria | Status |
|----|-------------|---------------------|--------|
| REQ-PLAT-01 | Platform is built for **Sharon Chinese School only** (single tenant). | No school picker at login; all data scoped to one org; branding and config are school-specific. | Confirmed |
| REQ-PLAT-02 | Platform is **not** sold as SaaS to multiple schools in v1. | Architecture may use tenant-like tables internally, but only one tenant is provisioned and documented. | Confirmed |
| REQ-PLAT-03 | No subscription fee to **access** the platform. | Parents never see a “platform membership” line item; accounts are not paywalled for login. | Confirmed |
| REQ-PLAT-04 | Parents **pay for selected courses** during registration (tuition/fees), not platform access. | Checkout line items map to courses/fees; payment records tie to enrollment, not SaaS billing. | Confirmed |

## Model

```
┌─────────────────────────────────────────────────────────┐
│              Sharon Chinese School (tenant)              │
├─────────────────────────────────────────────────────────┤
│  Public site          │  Authenticated LMS + portals   │
│  (marketing, info)    │  Parent / Student / Teacher /  │
│                       │  Staff / Admin portals         │
├───────────────────────┴─────────────────────────────────┤
│  Registration & payments │  Schedules │  Courses       │
└─────────────────────────────────────────────────────────┘
```

## Layered responsibilities

| Layer | What it does | Who configures |
|-------|----------------|----------------|
| **Public site** | Marketing, school info, public announcements, registration entry | Admin / content editors |
| **Identity** | Accounts, users, students, login methods | Parents (self-service) + admin assist |
| **Commerce** | Cart, discounts, payment capture, receipts | Parents pay; admin sets fees |
| **Scheduling** | Academic year, grades, classes, rooms, times | Admin |
| **LMS** | Materials, assignments, submissions, grades | Teachers per course |
| **Comms** | School-wide and class announcements | Admin, staff, teachers |

## Responsibilities split

| Concern | Owner in platform |
|---------|-------------------|
| Family accounts, students, enrollment | Platform |
| Tuition / class payments | Platform (Stripe, Square, or similar) |
| Yearly course catalog & master schedule | Admin |
| Day-to-day class content & grading | Teachers (Google Classroom–like UX) |
| School-wide news & announcements | Admin & staff |
| Class-level announcements | Teachers & TAs |

## Operational workflows

### Yearly reset (admin)

1. Clone or create new **academic year** catalog (grades and class sections).
2. Open registration window dates on public site and parent portal.
3. Assign teachers and rooms to each class section.
4. After registration closes, reconcile rosters and payment reports.

### Day-of-school (teacher + parent)

1. Teacher posts class announcement or assignment in course hub.
2. Student or parent sees update on schedule/course view (per portal permissions).
3. Admin handles one-off **room/time change** on master schedule; dependents see updated calendar.

## Edge cases

| Case | Expected handling |
|------|-------------------|
| Payment provider downtime | User sees clear error; no silent “paid” state; retry when provider recovers |
| Partial enrollment (one child paid, one unpaid) | Cart/checkout per rules in [Registration & payment](registration-payment.md); roster only for paid seats if that is school policy |
| Staff user without parent role | Access admin/teacher tools only; no family billing unless also linked as parent |
| Export for bookkeeping | Admin can export payment/enrollment summaries for the active year |

## Mobile and accessibility

- Public and authenticated shells share responsive breakpoints; navigation collapses to a menu on narrow viewports.
- Payment flows use provider-hosted or mobile-optimized components where PCI requires it.
- Color and typography on public pages should meet contrast guidelines for outdoor/bright-screen mobile use during pickup line registration.

## Optional future: hybrid delivery

Courses may support a `delivery_mode` field:

| Mode | Platform handles | External (e.g. Google Classroom) |
|------|------------------|----------------------------------|
| `internal` | Full LMS | — |
| `google_classroom` | Registration, accounts, scheduling, announcements | Assignments, materials, grading (TBD) |
| `hybrid` | Mix | Mix |

*v1 target: primarily `internal` with in-person instruction.*

When `google_classroom` is enabled later, parents still use one account for registration and schedule; links to external classroom are explicit so support staff can troubleshoot.

## Related documents

- [Overview](overview.md)
- [Registration & payment](registration-payment.md)
- [Courses & learning](courses.md)
