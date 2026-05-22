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

### Platform map

![Platform map](doc/assets/diagrams/README-platform-map.svg)

---

## Phase 1 priority (May 2026)

Agreed with **The Web Design LLC**: deliver a **professional public homepage** and **registration / course enrollment** together.

| Track | Deliverables |
|-------|----------------|
| **Public website** | [Homepage](doc/public-homepage.md) (hero, mission, events, announcements) · [About](doc/about-school.md) · [Contact](doc/contact-and-calendar.md) · [Public content map](doc/public-site-content.md) |
| **Registration** | [Registration flow](doc/registration-flow.md) · [User fields](doc/registration-user-fields.md) · [Enrollment & payment](doc/registration-payment.md) · [Tuition policies](doc/tuition-policies.md) |

**Vendor start here:** [Registration flow](doc/registration-flow.md) + [Public homepage](doc/public-homepage.md)

---

## At a glance

| Area | Summary |
|------|---------|
| **Public site** | Mission, About, homepage, course catalog, contact, tuition policies |
| **Phase 1** | Public homepage (mission, events) + registration, parent portal, enrollment, payment |
| **Platform** | One school only (Sharon Chinese School); no SaaS / subscription to use the platform |
| **Users** | Parents self-register; manage students; admins can assist when needed |
| **Learning** | In-person classes first; LMS for materials, assignments, schedules, communication |
| **Payments** | Parents enroll students in classes and pay (cart, discounts, Stripe/Square) |
| **Roles** | RBAC with Parent, Student, Teacher, TA, Staff, Admin; multiple roles per person |
| **Auth** | Google OAuth, Microsoft OAuth, email + password, phone + SMS |

---

## Wiki contents

### Foundation

| Document | Description |
|----------|-------------|
| [Project overview](doc/overview.md) | Goals, stakeholders, legacy site, scope |
| [Platform structure](doc/platform.md) | Single-tenant model, funding, high-level architecture |
| [Glossary](doc/glossary.md) | Terms: Account, User, Student, Staff, TA, etc. |

### Public website (professional nonprofit presence)

| Document | Description |
|----------|-------------|
| [Public homepage](doc/public-homepage.md) | Hero, mission line, events, announcements |
| [About the school](doc/about-school.md) | Mission, history, nonprofit, leadership |
| [Public site content](doc/public-site-content.md) | Course catalog, news, priorities P0–P2 |
| [Contact & school calendar](doc/contact-and-calendar.md) | Contact page, academic calendar |
| [Tuition, discounts & refunds](doc/tuition-policies.md) | Enrollment business rules |
| [Legacy content migration](doc/legacy-content-migration.md) | Checklist from old site |

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

### Registration (phase 1)

| Document | Description |
|----------|-------------|
| **[Registration flow (complete guide)](doc/registration-flow.md)** | **Start here** — end-to-end flow for vendor |
| [Registration — user fields](doc/registration-user-fields.md) | Signup profile fields (CN/EN), family model, roles |
| [Registration & payment](doc/registration-payment.md) | Enrollment flow, cart, discounts, gateways |
| [WebSiteUserFields.xlsx](doc/WebSiteUserFields.xlsx) | Original spreadsheet from Kyna |

### Vendor collaboration

| Document | Description |
|----------|-------------|
| [Vendor Q&A log](doc/vendor-qa.md) | Questions from The Web Design LLC and school answers |

---

## Source documents

Requirements were consolidated from school materials (also kept locally in the parent project `documents/` folder):

- `Sharon_Chinese_School_LMS_Requirements.docx` — consolidated requirements
- `sharon_chinese_school-lms-queries.docx` — vendor questions with answers (Kyna, 2026-03-21)
- `ShaornCS-lms-queries (1).docx` — original vendor question set
- `WebSiteUserFields.xlsx` — registration profile fields (Kyna, May 2026); copy in [`doc/`](doc/WebSiteUserFields.xlsx)

When the wiki and Word docs disagree, **prefer the answered Q&A** (`vendor-qa.md`) and update the wiki.

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

*Last updated: 2026-05-22 (registration field spec added)*
