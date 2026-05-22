# Project overview

[← Wiki home](../README.md)

## Mission

Sharon Chinese School (MA Sharon Chinese Language School) needs a **modern public website** and an integrated **LMS** so that:

- Prospective and current families can find information and complete registration online
- Parents manage students, class enrollment, and payments in one place
- Teachers run classes with materials, assignments, and communication similar to Google Classroom
- Administrators manage courses, schedules, staff, volunteers, and school-wide announcements

## Diagrams

### 🏫 Who we are building for

```mermaid
flowchart TB
  subgraph school["🏫 莎伦中文学校 Sharon Chinese School"]
    P["👨‍👩‍👧 家长 Parent\n帮家庭注册缴费"]
    S["👦👧 学生 Student\n7–13 岁 · 学中文"]
    T["👩‍🏫 老师 Teacher\n教课 · 批改作业"]
    A["📋 管理员 Admin\n排课 · 收款"]
  end
  P -->|"管理"| S
  T -->|"教"| S
  A -->|"安排课程"| T
  P -->|"选课付款"| A
```

### 📅 Build order (phase 1 first)

```mermaid
flowchart LR
  P1["🥇 Phase 1\n家长门户 + 注册缴费"] --> P2["🥈 Phase 2\n学生/老师 LMS"]
  P2 --> P3["🥉 持续改进\n通知 · 更多功能"]
  style P1 fill:#fff3cd
```

### 😅 Old site → ✨ New platform

```mermaid
flowchart LR
  OLD["😵 旧网站\n难找 · 难注册"] --> NEW["✨ 新平台\n清晰 · 一家一户账号"]
  NEW --> LMS["📚 LMS\n作业 · 课表 · 公告"]
```

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
| **1 (now)** | **Public homepage** (hero, mission, events, announcements), About/contact, **registration**, parent portal, enrollment, payment | [Public homepage](public-homepage.md), [About](about-school.md), [Registration flow](registration-flow.md), [Parent portal](parent-portal.md) |
| **2+** | Student/teacher LMS depth, materials, assignments, full admin tooling | [Student](student-portal.md), [Teacher](teacher-portal.md), [Admin](admin-portal.md) portals |

The vendor requested detailed registration fields; the school provided **`WebSiteUserFields.xlsx`** (see wiki).

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

## Success criteria

1. Families can register, add students, select classes, apply discounts, and pay without admin intervention for the common path.
2. Teachers can publish materials, assign work, collect PDF/image submissions, and grade with feedback.
3. Students see an accurate daily schedule and per-course learning hub controlled by the teacher.
4. Admins can define the academic year structure, assign teachers, manage substitutes and one-off reschedules, and track payments.
5. The public site is accessible, mobile-friendly, and easier to maintain than the legacy site.

## Related documents

- [Parent portal](parent-portal.md)
- [Registration — user fields](registration-user-fields.md)
- [Registration & payment](registration-payment.md)
- [Platform structure](platform.md)
- [Vendor Q&A log](vendor-qa.md)
