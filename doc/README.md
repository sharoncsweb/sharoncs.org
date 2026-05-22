# Documentation index

This folder contains detailed requirements for each component of the Sharon Chinese School website and LMS.

**Start here:** [Wiki home (README)](../README.md)

Each page has **2–3 flat SVG diagrams** with English labels and simple character art (students typically ages 7–13).

## How to use this wiki

| Audience | Suggested reading order |
|----------|-------------------------|
| **School committee** | [Overview](overview.md) → [Platform](platform.md) → [Registration & payment](registration-payment.md) → topic pages as decisions arise |
| **Vendor / implementation** | [Overview](overview.md) → [Accounts](accounts.md) → [School structure](school-structure.md) → portal and RBAC pages before build |
| **QA / UAT** | Requirements tables (ID + **Acceptance criteria**) on each page; cross-check against [Registration — user fields](registration-user-fields.md) |

Pages are written for **joint review**: school committee confirms business rules; vendor implements behavior, edge cases, and non-functional expectations (mobile, accessibility) called out on each page.

### Conventions

- **REQ-*** identifiers are stable; do not renumber existing IDs when editing.
- **Confirmed** = agreed for the current phase; **Future** / **Implied** = not blocking Phase 1 unless noted.
- Diagrams illustrate flows; **requirements tables** are authoritative for acceptance.
- English is the specification language for implementation and test cases.

### Non-functional expectations (cross-cutting)

Where a page does not repeat them, assume:

- **Mobile-first** layouts for parent and student flows (registration, cart, schedules).
- **WCAG-oriented** public pages: sufficient contrast, keyboard focus, form labels tied to inputs, error text associated with fields.
- **Session security**: authenticated actions require a valid login; sensitive changes (payment, adding users) respect primary-owner rules in [Accounts](accounts.md).

## Pages

| Page | Topic |
|------|--------|
| [frontend-backend-config.md](frontend-backend-config.md) | Dynamic frontend content → admin configuration |
| [overview.md](overview.md) | Project goals, stakeholders, scope |
| [glossary.md](glossary.md) | Term definitions |
| [platform.md](platform.md) | Single-tenant platform model |
| [accounts.md](accounts.md) | Account, user, student, enrollment |
| [school-structure.md](school-structure.md) | Grades, classes, rosters |
| [courses.md](courses.md) | Course lifecycle and content |
| [parent-portal.md](parent-portal.md) | Parent / guardian UX |
| [student-portal.md](student-portal.md) | Student UX |
| [teacher-portal.md](teacher-portal.md) | Teacher UX |
| [admin-portal.md](admin-portal.md) | Admin and staff UX |
| [announcements.md](announcements.md) | Feeds and visibility |
| [rbac.md](rbac.md) | Roles and permissions |
| [authentication.md](authentication.md) | Login and security |
| [registration-user-fields.md](registration-user-fields.md) | **Phase 1** signup profile fields (English) |
| [registration-payment.md](registration-payment.md) | Enrollment, cart, and payments |
| [WebSiteUserFields.xlsx](WebSiteUserFields.xlsx) | Registration field spreadsheet |
| [vendor-qa.md](vendor-qa.md) | Vendor questions and school answers |

## Phase 1 document bundle

For registration season, prioritize:

1. [Overview](overview.md) — scope and success criteria  
2. [Accounts](accounts.md) + [Registration — user fields](registration-user-fields.md) + [Registration & payment](registration-payment.md)  
3. [School structure](school-structure.md) + [Parent portal](parent-portal.md)  
4. [Authentication](authentication.md) + [RBAC](rbac.md)

Phase 2 LMS depth is documented but may ship after the family registration path is stable in production.
