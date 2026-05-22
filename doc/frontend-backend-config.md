# Frontend ↔ backend configuration map

[← Wiki home](../README.md)

Every **dynamic** item on the public site or in a portal is loaded from data staff configure in the **admin (or teacher) backend**. This page links **what users see** to **where it is configured** and to the detailed requirement spec.

**Vendor expectation:** Where practical, give authorized staff a **Configure** or **Manage in admin** link from the frontend preview (staff view) or from in-app help, pointing to the backend screen below.

---

## Summary diagram

![Frontend to backend config](assets/diagrams/frontend-backend-map.svg)

---

## Public website (no login)

| Frontend surface | Dynamic content | Backend configuration (admin) | Requirement spec |
|------------------|-----------------|--------------------------------|------------------|
| [Homepage](public-homepage.md) hero | Headline, mission line, CTAs, hero image | **Admin → Content → Homepage → Hero** | [REQ-HOME-02](public-homepage.md#requirements) |
| [Homepage](public-homepage.md) announcements strip | Short notices, publish dates, visibility | **Admin → Content → Homepage → Announcements** | [REQ-HOME-03](public-homepage.md#requirements), [Announcements](announcements.md) |
| [Homepage](public-homepage.md) events list | Dated activities, location, featured flag | **Admin → Content → Homepage → Events** | [REQ-HOME-03](public-homepage.md#requirements) |
| [About](about-school.md) | Mission, history, leadership, youth program copy | **Admin → Content → Pages → About** (CMS blocks) | [about-school.md](about-school.md) |
| [Contact](contact-and-calendar.md) | Email, phone, addresses, map | **Admin → Settings → School contact** | [REQ-CON-01](contact-and-calendar.md#requirements) |
| [School calendar](contact-and-calendar.md) (public) | Academic year dates, holidays, PDF | **Admin → Content → School calendar** | [REQ-CON-03](contact-and-calendar.md#requirements) |
| [Course catalog](public-site-content.md#public-course-catalog) | Semester, course name, fee, class days, filters | **Admin → Academic year → Courses** (publish to catalog flag) | [REQ-CAT-01](public-site-content.md#public-course-catalog) |
| Catalog **prices** shown | Regular / early-bird price per course | **Admin → Academic year → Courses → Pricing** + **Admin → Pricing → Tuition rules** | [tuition-policies.md](tuition-policies.md), [REQ-CAT-03](public-site-content.md#public-course-catalog) |
| [Tuition & policies](tuition-policies.md) page | Discount rules, refund policy text, excluded courses | **Admin → Pricing → Discounts & refunds** (rules) + **Admin → Content → Pages → Tuition** (copy) | [tuition-policies.md](tuition-policies.md) |
| Registration CTA / window | Open/closed, deadline messaging | **Admin → Registration → Seasons & deadlines** | [registration-flow.md](registration-flow.md) |
| Footer (all public pages) | Contact, location, links | **Admin → Settings → School contact** + **Admin → Content → Navigation / footer** | [REQ-HOME-09](public-homepage.md#requirements) |
| News / gallery (later) | Articles, albums | **Admin → Content → News** · **Admin → Content → Gallery** | [public-site-content.md](public-site-content.md) |

### Homepage announcements {#homepage-announcements}

| Layer | Detail |
|-------|--------|
| **Frontend** | Public homepage announcements list / strip |
| **Backend** | **Admin → Content → Homepage → Announcements** — title, body, start/end date, publish state, optional link |
| **Permissions** | `homepage.post_announcement`, `homepage.publish` — [RBAC](rbac.md) |
| **Related** | Logged-in school-wide feed uses [Announcements](announcements.md) (may mirror or separate records — **TBD** with vendor) |

### Homepage events {#homepage-events}

| Layer | Detail |
|-------|--------|
| **Frontend** | Public homepage events (sorted by date) |
| **Backend** | **Admin → Content → Homepage → Events** — title, description, date/time, location, image, publish state |
| **Permissions** | `homepage.post_event`, `homepage.publish` — [RBAC](rbac.md) |

---

## Registration & checkout

| Frontend surface | Dynamic content | Backend configuration (admin) | Requirement spec |
|------------------|-----------------|--------------------------------|------------------|
| Sign-up forms | Field labels, required/optional | **Admin → Registration → Profile fields** (sync with [user fields](registration-user-fields.md)) | [registration-user-fields.md](registration-user-fields.md) |
| Class picker / cart | Offerings, seats, waitlist | **Admin → Academic year → Courses** + **Admin → Enrollment → Capacity** | [registration-payment.md](registration-payment.md) |
| Cart **line prices** | Course tuition, early bird | **Admin → Academic year → Courses → Pricing** | [tuition-policies.md](tuition-policies.md) |
| Cart **discounts** | Early bird, sibling, multi-class, exclusions | **Admin → Pricing → Discount rules** | [tuition-policies.md](tuition-policies.md), [registration-payment.md](registration-payment.md) |
| Checkout total | Tax, fees (if any), applied discount | **Admin → Pricing → Discount engine** (read-only preview in cart) | [registration-payment.md](registration-payment.md) |
| Payment | Stripe / Square credentials, test/live | **Admin → Settings → Payment gateways** | [registration-payment.md](registration-payment.md) |
| Receipt / enrollment status | Paid, partial, refunded | **Admin → Enrollment → Payments** | [REQ-ADM-05](admin-portal.md#requirements) |

---

## Parent portal

| Frontend surface | Dynamic content | Backend configuration (admin) | Requirement spec |
|------------------|-----------------|--------------------------------|------------------|
| Family / student profiles | Names, roles, relationships | **Parent portal** (self-service) + **Admin → Users → Families** (override) | [registration-user-fields.md](registration-user-fields.md) |
| Enrollable **courses** list | Same as catalog, enrollment window | **Admin → Academic year → Courses** + **Admin → Registration → Seasons** | [parent-portal.md](parent-portal.md) |
| Cart & checkout | Same as registration table above | **Admin → Pricing → …** · **Admin → Settings → Payment gateways** | [registration-payment.md](registration-payment.md) |
| Payment history | Invoices, receipts | **Admin → Enrollment → Payments** (parent read-only) | [parent-portal.md](parent-portal.md) |
| School-wide **announcements** | Feed items visible to parents | **Admin → Communications → School announcements** or teacher/staff post per [announcements.md](announcements.md) | [announcements.md](announcements.md) |
| Child **class announcements** | Per-course posts | **Teacher portal → Course → Announcements** (class scope) | [announcements.md](announcements.md) |

---

## Student portal

| Frontend surface | Dynamic content | Backend configuration (admin) | Requirement spec |
|------------------|-----------------|--------------------------------|------------------|
| **Today / weekly schedule** | Sessions, times, rooms | **Admin → Academic year → Master schedule** (+ session overrides) | [student-portal.md](student-portal.md), [admin-portal.md](admin-portal.md) |
| **Course list** | Enrolled classes | **Admin → Enrollment → Rosters** (derived from enrollment) | [school-structure.md](school-structure.md) |
| Course page: materials, homework | Modules, files, assignments | **Teacher portal → Course → Content** | [courses.md](courses.md) |
| Course page: **announcements** | Class posts | **Teacher portal → Course → Announcements** | [courses.md](courses.md), [announcements.md](announcements.md) |
| Grades / feedback | Scores, comments | **Teacher portal → Course → Grading** | [courses.md](courses.md) |

---

## Teacher portal

| Frontend surface | Dynamic content | Backend configuration (admin / teacher) | Requirement spec |
|------------------|-----------------|------------------------------------------|------------------|
| My **courses** list | Assigned sections | **Admin → Academic year → Courses** (teacher assignment) | [REQ-ADM-01](admin-portal.md#requirements) |
| **Session schedule** for a course | Recurring + one-off changes | **Admin → Master schedule**; **Teacher/Admin → Session → Reschedule / Substitute** | [REQ-ADM-02](admin-portal.md#requirements), [REQ-CRS-04](courses.md#requirements) |
| Course content visibility | What students see | **Teacher portal → Course → Settings** | [REQ-CRS-02](courses.md#requirements) |
| Assignments & exams | Create, due dates, attachments | **Teacher portal → Course → Assignments** | [courses.md](courses.md) |
| Class **announcements** | Posts to enrolled families | **Teacher portal → Course → Announcements** | [announcements.md](announcements.md) |

---

## Admin & staff portal (configuration home)

| Configuration area | What it drives on the frontend | Spec |
|--------------------|--------------------------------|------|
| **Academic year → Grades & classes** | Grade levels, sections (Class A/B) | [school-structure.md](school-structure.md) |
| **Academic year → Courses** | Catalog, enrollment, parent/student course lists, schedule source | [courses.md](courses.md) |
| **Academic year → Master schedule** | Student schedule, session times/rooms | [admin-portal.md](admin-portal.md) |
| **Session → Reschedule / Substitute** | Single-class time or teacher change | [admin-portal.md](admin-portal.md) |
| **Content → Homepage** | Public announcements, events, hero | [public-homepage.md](public-homepage.md) |
| **Content → School calendar** | Public academic calendar | [contact-and-calendar.md](contact-and-calendar.md) |
| **Content → Pages** | About, tuition policy text, static guidelines | [public-site-content.md](public-site-content.md) |
| **Pricing → Tuition rules** | Per-course prices, late registration tiers | [tuition-policies.md](tuition-policies.md) |
| **Pricing → Discount rules** | Cart discounts, excluded courses | [tuition-policies.md](tuition-policies.md) |
| **Registration → Seasons & deadlines** | Registration open/close, early bird dates | [registration-flow.md](registration-flow.md) |
| **Registration → Profile fields** | Sign-up form fields | [registration-user-fields.md](registration-user-fields.md) |
| **Enrollment → Rosters & capacity** | Who is in which class; waitlist | [school-structure.md](school-structure.md) |
| **Enrollment → Payments** | Paid status, admin overrides | [registration-payment.md](registration-payment.md) |
| **Communications → School announcements** | School-wide feed (logged-in) | [announcements.md](announcements.md) |
| **Volunteers → Duty calendar** | Duty roster and reminders | [admin-portal.md](admin-portal.md) |
| **Settings → School contact** | Contact page, footer | [contact-and-calendar.md](contact-and-calendar.md) |
| **Settings → Authentication** | Enabled login methods | [authentication.md](authentication.md) |
| **Settings → Payment gateways** | Stripe / Square | [registration-payment.md](registration-payment.md) |
| **Settings → Roles & permissions** | Who can post homepage, announcements, etc. | [rbac.md](rbac.md) |

---

## Implementation notes (vendor)

| Topic | Guidance |
|-------|----------|
| **Deep links** | Use stable admin URLs (e.g. `/admin/content/homepage/announcements/{id}/edit`) so frontend “Configure” links survive releases. |
| **Preview** | Homepage and catalog should support **preview as staff** before publish. |
| **Cache** | Public homepage and catalog may be cached; invalidate when admin publishes. |
| **Audit** | Log who changed prices, discounts, and published homepage items. |

---

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-FBC-01 | Every dynamic public homepage block (hero, announcements, events) has a documented admin configuration path. | Confirmed |
| REQ-FBC-02 | Course catalog prices and schedules are driven by **Academic year → Courses**, not hard-coded. | Confirmed |
| REQ-FBC-03 | Cart discounts and tuition rules are driven by **Pricing** admin configuration. | Confirmed |
| REQ-FBC-04 | Student and parent schedules are driven by **Master schedule** and enrollment rosters. | Confirmed |
| REQ-FBC-05 | Class and school announcements are created in **Communications** / **Teacher course** admin paths. | Confirmed |
| REQ-FBC-06 | Staff with permission can navigate from frontend context to the matching backend config (link or menu). | Confirmed |

---

## Related documents

- [Admin portal](admin-portal.md)
- [Public homepage](public-homepage.md)
- [Public site content](public-site-content.md)
- [Registration flow](registration-flow.md)
- [Announcements](announcements.md)
- [Courses](courses.md)
- [Tuition policies](tuition-policies.md)
