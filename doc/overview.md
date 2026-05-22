# Project overview

[← Wiki home](../README.md)

## Mission

Sharon Chinese School (MA Sharon Chinese Language School) needs a **modern public website** and an integrated **LMS** so that:

- Prospective and current families can find information and complete registration online
- Parents manage students, class enrollment, and payments in one place
- Teachers run classes with materials, assignments, and communication similar to Google Classroom
- Administrators manage courses, schedules, staff, volunteers, and school-wide announcements

The platform replaces a fragmented experience (static site + offline registration) with one **family account** model, clear class placement, and portals tuned to each role.

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Who we are building for

![Who we are building for](assets/diagrams/overview-stakeholders.svg)

### Build order (phase 1 first)

![Build order (phase 1 first)](assets/diagrams/overview-phases.svg)

### Legacy site to new platform

![Legacy site to new platform](assets/diagrams/overview-legacy-new.svg)


## Problem with the legacy site

The current site at [www.sharoncs.org](https://www.sharoncs.org/) is dated and difficult to navigate. It exposes announcements, news, teaching activity, and a gallery, but lacks integrated registration, parent accounts, and classroom tools.

**Observed pain points:**

| Area | Legacy behavior | Target behavior |
|------|-----------------|-----------------|
| Discovery | Information scattered across menus | Clear homepage, About, and registration CTAs |
| Registration | Manual / offline steps | Self-service with cart and online payment |
| Family data | Duplicate or inconsistent records | One account, Family Identifier, linked students |
| Classroom | No unified hub | Per-course LMS pages for materials and assignments |

## Stakeholders

| Role | Responsibility | Platform touchpoints |
|------|----------------|----------------------|
| **School committee** | Product decisions, answers to vendor questions | Scope, pricing rules, registration fields |
| **Parents & students** | Primary end users for registration and learning | Parent portal, student portal, public site |
| **Teachers, TAs, volunteers** | Classroom and operational workflows | Teacher portal, class rosters, announcements |
| **Administrators** | Yearly course setup, schedules, rosters, payments | Admin portal, payment reports, master schedule |
| **The Web Design LLC** | Design and implementation ([thewebdesignllc.com](https://thewebdesignllc.com/)) | Delivery per requirements in this wiki |

**Committee review cadence:** Major flows (registration, payment, roster) should be demoed on **mobile width** and with **keyboard-only** navigation before sign-off, because most parents register from phones.

## Implementation priority

| Phase | Focus | Documentation |
|-------|--------|----------------|
| **1 (now)** | **Public homepage** (hero, mission, events, announcements), About/contact, **registration**, parent portal, enrollment, payment | [Public homepage](public-homepage.md), [About](about-school.md), [Registration flow](registration-flow.md), [Parent portal](parent-portal.md) |
| **2+** | Student/teacher LMS depth, materials, assignments, full admin tooling | [Student](student-portal.md), [Teacher](teacher-portal.md), [Admin](admin-portal.md) portals |

**Phase 1 exit:** A new family can complete account creation, add students, enroll in at least one class, pay, and see confirmation in the parent portal without admin intervention on the happy path.

**Phase 2 exit:** Teachers can run a full class cycle (materials, assignments, submissions, feedback) and students see an accurate schedule and course hub.

## Scope

### In scope

- Single-school platform (not multi-tenant SaaS)
- Public marketing / information pages (modern UX)
- Parent self-service registration and student profiles
- Class enrollment and payment
- LMS features supporting **in-person** instruction
- Role-based access control with flexible roles (e.g. parent + teacher, student + TA)
- Multiple authentication methods and account linking

### Out of scope (initial)

- Subscription billing for platform access
- Multi-school tenancy
- Full replacement of Google Classroom (optional hybrid / future delivery modes)

### Future / optional

- Grade-level announcement targeting
- Limited access for non-primary parents on an account
- Hybrid course delivery (`google_classroom`, `hybrid` delivery modes)
- Multi-factor authentication (planned, not day-one)

## Detailed behavior (cross-cutting)

| Topic | Expected behavior |
|-------|-------------------|
| **Academic year** | Admin defines the active year; registration and rosters are year-scoped |
| **Waitlists** | If a class is full, behavior follows [Registration & payment](registration-payment.md) (waitlist vs block — confirm in UAT) |
| **Refunds / transfers** | Admin-mediated; not assumed to be fully self-service in v1 |
| **Language** | UI and parent-facing copy in English; student content may include Chinese per teacher |
| **Audit** | Admin changes to rosters, payments, and accounts should be traceable |

## Edge cases

| Scenario | Handling |
|----------|----------|
| Parent already has legacy paper forms on file | Admin links or merges into new account; duplicate students flagged |
| Two households, one child (shared custody) | One student record on **one** account; second household may need admin process (see [Accounts](accounts.md)) |
| Parent is also teacher | Single login; RBAC shows both parent and teacher tools |
| Registration window closed | Public site shows message; admin can override for late enrollments |
| Payment failure mid-checkout | Cart retained; user can retry without re-entering all profile data |

## Mobile and accessibility

- **Public site:** Responsive layout; hero and registration links visible without horizontal scroll on common phone widths.
- **Forms:** Large tap targets; phone + SMS path must work on mobile browsers.
- **Portals:** Parent dashboard and enrollment cart usable on phone; critical actions (pay, add student) not desktop-only.
- **Accessibility:** Meaningful page titles, heading order, form errors announced to assistive tech; PDFs uploaded by teachers should not be the only way to convey urgent school-wide alerts (HTML announcement preferred).

## Success criteria

1. Families can register, add students, select classes, apply discounts, and pay without admin intervention for the common path.
2. Teachers can publish materials, assign work, collect PDF/image submissions, and grade with feedback.
3. Students see an accurate daily schedule and per-course learning hub controlled by the teacher.
4. Admins can define the academic year structure, assign teachers, manage substitutes and one-off reschedules, and track payments.
5. The public site is accessible, mobile-friendly, and easier to maintain than the legacy site.

**Measurable checks for criterion 1:** End-to-end test account completes registration in one session; receipt/email confirmation; student appears on class roster within defined SLA (e.g. immediate or post-webhook — specify in payment doc).

## Related documents

- [Parent portal](parent-portal.md)
- [Registration — user fields](registration-user-fields.md)
- [Registration & payment](registration-payment.md)
- [Platform structure](platform.md)
- [Vendor Q&A log](vendor-qa.md)
