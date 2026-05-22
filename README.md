# Sharon Chinese School — Website & LMS Wiki

Welcome to the requirements wiki for the new **Sharon Chinese School** website and learning platform.

| | |
|---|---|
| **Live site (legacy)** | [www.sharoncs.org](https://www.sharoncs.org/) |
| **Development partner** | [The Web Design LLC](https://thewebdesignllc.com/) |
| **Repository** | [github.com/sharoncsweb/sharoncs.org](https://github.com/sharoncsweb/sharoncs.org) |

---

## Purpose

Replace the aging public website with a modern, easy-to-use experience and add a **single-school Learning Management System (LMS)** so families can register, pay, and stay connected while teachers and staff run classes day to day.

This wiki documents product and technical requirements. Detailed specs live under [`doc/`](doc/). Each page includes **flat-design SVG diagrams** (English labels) for the vendor and school team.

### Platform map

![Platform map](doc/assets/diagrams/README-platform-map.svg)

---

## Implementation phases

Build in order: **phase 1 first**, then student/teacher LMS, then ongoing improvements. Full context: [Project overview](doc/overview.md).

![Implementation phases](doc/assets/diagrams/overview-phases.svg)

### Phase 1 (now) — Public site + registration

Launch a professional public site and end-to-end family signup.

| Area | Deliverables | Specs |
|------|--------------|-------|
| **Public website** | Homepage (hero, mission, events, announcements), About, contact, tuition policies, browse course catalog | [Public homepage](doc/public-homepage.md) · [About](doc/about-school.md) · [Contact & calendar](doc/contact-and-calendar.md) · [Public site content](doc/public-site-content.md) |
| **Registration** | Parent self-registration, family profiles, class cart, discounts, payment | [Registration flow](doc/registration-flow.md) · [User fields](doc/registration-user-fields.md) · [Enrollment & payment](doc/registration-payment.md) |
| **Parent portal** | Manage family, enroll students, pay tuition | [Parent portal](doc/parent-portal.md) |

### Phase 2 — Student & teacher LMS

Classroom tools after families can register and pay.

| Area | Deliverables | Specs |
|------|--------------|-------|
| **Student portal** | Schedule, per-course hub, homework submission | [Student portal](doc/student-portal.md) |
| **Teacher portal** | Materials, assignments, exams, grading | [Teacher portal](doc/teacher-portal.md) |
| **Admin portal** | Academic year setup, rosters, substitutes, volunteers, payments oversight | [Admin portal](doc/admin-portal.md) |
| **Learning & comms** | Course lifecycle, school structure, announcements feed | [Courses](doc/courses.md) · [School structure](doc/school-structure.md) · [Announcements](doc/announcements.md) |

Soon after phase 1 (still public site): school calendar, registration instructions, news — see [Public site content](doc/public-site-content.md) (P1 items).

### Phase 3 — Ongoing improvements

Enhancements and legacy content migration as the school prioritizes.

| Area | Examples | Specs |
|------|----------|-------|
| **Legacy public pages** | Gallery, news archive, resources, teaching showcase, donations, youth programs | [Legacy content migration](doc/legacy-content-migration.md) · [Public site content](doc/public-site-content.md) (P2) |
| **Platform** | Richer notifications, MFA, grade-level announcement targeting, optional hybrid delivery | [Authentication](doc/authentication.md) · [Overview — future](doc/overview.md#future--optional) |

---

## At a glance

| Area | Summary |
|------|---------|
| **Phases** | **1:** public site + registration · **2:** student/teacher/admin LMS · **3:** legacy pages + platform enhancements |
| **Platform** | One school only (Sharon Chinese School); no SaaS / subscription to use the platform |
| **Users** | Parents self-register; manage students; admins can assist when needed |
| **Learning** | In-person classes first; LMS for materials, assignments, schedules, communication |
| **Payments** | Parents enroll students in classes and pay (cart, discounts, Stripe/Square) |
| **Roles** | RBAC with Parent, Student, Teacher, TA, Staff, Admin; multiple roles per person |
| **Auth** | Google OAuth, Microsoft OAuth, email + password, phone + SMS ([Authentication](doc/authentication.md)) |

---

## Wiki contents

### Foundation

| Document | Description |
|----------|-------------|
| [Frontend ↔ backend configuration map](doc/frontend-backend-config.md) | Links dynamic UI (courses, announcements, prices, schedules) to admin config |
| [Project overview](doc/overview.md) | Goals, stakeholders, legacy site, scope |
| [Platform structure](doc/platform.md) | Single-tenant model, funding, high-level architecture |
| [Glossary](doc/glossary.md) | Terms: Account, User, Student, Staff, TA, etc. |

### Data & access

| Document | Description |
|----------|-------------|
| [Accounts & enrollment](doc/accounts.md) | Account / User / Student model; registration flows |
| [Roles & permissions (RBAC)](doc/rbac.md) | Default roles, permissions, custom roles, TA rules |
| [Authentication](doc/authentication.md) | Login methods, linking, security, admin controls |

### Academic structure

| Document | Description |
|----------|-------------|
| [School structure](doc/school-structure.md) | Grades, classes, sections, rosters |
| [Courses & learning](doc/courses.md) | Course lifecycle, content, Google Classroom–style model |
| [Announcements & activity feed](doc/announcements.md) | Who can post; visibility levels |

### Portals

| Document | Description |
|----------|-------------|
| [Parent portal](doc/parent-portal.md) | Family account, enrollment, payments, student oversight |
| [Student portal](doc/student-portal.md) | Schedule, course pages, tasks, progress |
| [Teacher portal](doc/teacher-portal.md) | Materials, assignments, exams, grading |
| [Admin & management portal](doc/admin-portal.md) | Staff, schedules, substitutes, volunteers |

### Public site & registration (phase 1)

| Document | Description |
|----------|-------------|
| [Registration flow](doc/registration-flow.md) | End-to-end vendor guide (homepage → pay) |
| [Public homepage](doc/public-homepage.md) | Hero, mission, events, announcements |
| [About the school](doc/about-school.md) | Mission, nonprofit identity, youth programs |
| [Contact & calendar](doc/contact-and-calendar.md) | Contact info, school calendar |
| [Tuition policies](doc/tuition-policies.md) | Fees, discounts, refunds |
| [Public site content](doc/public-site-content.md) | Page map and P0/P1/P2 priorities |
| [Registration — user fields](doc/registration-user-fields.md) | Signup profile fields (English), family model, roles |
| [Registration & payment](doc/registration-payment.md) | Enrollment flow, cart, discounts, gateways |
| [WebSiteUserFields.xlsx](doc/WebSiteUserFields.xlsx) | Field spreadsheet |
| [Legacy content migration](doc/legacy-content-migration.md) | Move content from old site (phase 2–3) |

### Vendor collaboration

| Document | Description |
|----------|-------------|
| [Vendor Q&A log](doc/vendor-qa.md) | Questions from The Web Design LLC and school answers |

---

## Contributing to this wiki

1. Edit markdown under `doc/` for component-level detail.
2. Keep **README** as the navigation hub (add links when you add pages).
3. Use clear headings, tables, and requirement IDs where helpful (e.g. `REQ-AUTH-01`).
4. Open a pull request or commit to `main` so the vendor and school committee stay aligned.

---

## Status

| Item | State |
|------|--------|
| Requirements wiki | In progress |
| Application code | Not started in this repo |
| Legacy site | Still live at [www.sharoncs.org](https://www.sharoncs.org/) |

*Last updated: 2026-05-22 (implementation phases on homepage)*
