# Project overview

[← Wiki home](../README.md)

## Mission

Sharon Chinese School (MA Sharon Chinese Language School) needs a **modern public website** and an integrated **LMS** so that:

- Prospective and current families can find information and complete registration online
- Parents manage students, class enrollment, and payments in one place
- Teachers run classes with materials, assignments, and communication similar to Google Classroom
- Administrators manage courses, schedules, staff, volunteers, and school-wide announcements
- The **public homepage** is professional and modern, with a hero section and school events/announcements posted by authorized staff

## Diagrams

**Characters:** Parent · Student (ages 7–13) · Teacher · Admin · School

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

## Stakeholders

| Role | Responsibility |
|------|----------------|
| **School committee / Kyna** | Product decisions, answers to vendor questions |
| **Parents & students** | Primary end users for registration and learning |
| **Teachers, TAs, volunteers** | Classroom and operational workflows |
| **Administrators** | Yearly course setup, schedules, rosters, payments |
| **The Web Design LLC** | Design and implementation ([thewebdesignllc.com](https://thewebdesignllc.com/)) |

## Implementation priority

Agreed with **The Web Design LLC** (May 2026):

| Phase | Focus | Documentation |
|-------|--------|----------------|
| **1 (now)** | Registration, **parent portal**, course enrollment, payment | [Parent portal](parent-portal.md), [User fields](registration-user-fields.md), [Registration & payment](registration-payment.md) |
| **2+** | Student/teacher LMS depth, materials, assignments, full admin tooling | [Student](student-portal.md), [Teacher](teacher-portal.md), [Admin](admin-portal.md) portals |

The vendor requested detailed registration fields; the school provided **`WebSiteUserFields.xlsx`** (see wiki).

## Scope

### In scope

- Single-school platform (not multi-tenant SaaS)
- **Public homepage & landing page** — professional hero, events, announcements ([spec](public-homepage.md))
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

## Success criteria

1. Families can register, add students, select classes, apply discounts, and pay without admin intervention for the common path.
2. Teachers can publish materials, assign work, collect PDF/image submissions, and grade with feedback.
3. Students see an accurate daily schedule and per-course learning hub controlled by the teacher.
4. Admins can define the academic year structure, assign teachers, manage substitutes and one-off reschedules, and track payments.
5. The public site is accessible, mobile-friendly, and easier to maintain than the legacy site.

## Related documents

- [Public homepage](public-homepage.md)
- [Parent portal](parent-portal.md)
- [Registration — user fields](registration-user-fields.md)
- [Registration & payment](registration-payment.md)
- [Platform structure](platform.md)
- [Vendor Q&A log](vendor-qa.md)
