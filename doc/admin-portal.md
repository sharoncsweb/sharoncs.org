# Admin & management portal

[← Wiki home](../README.md)

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Yearly course setup

![Yearly course setup](assets/diagrams/admin-year-setup.svg)

### Volunteer duty reminder

![Volunteer duty reminder](assets/diagrams/admin-volunteer.svg)

### Reschedule one session

![Reschedule one session](assets/diagrams/admin-reschedule.svg)


## Audience

**School administrators** and designated **staff** with elevated permissions. The portal is the control plane for academic year structure, rosters, money, communications, and system settings. Day-to-day teaching stays in the [Teacher portal](teacher-portal.md).

## Primary responsibilities

### Academic year setup

- Define **grades** and **classes** (multiple classes per grade — see [School structure](school-structure.md))
- Create **courses** with schedule, classroom, assigned teacher, capacity, and catalog copy
- Assign **instructors** annually; support **substitute** per session without changing yearly owner
- Clone prior year as starting point optional; admins review diffs before publish

**Workflow — open a new academic year**

1. Admin creates academic year record (dates, registration window).
2. Admin copies or creates grades/classes.
3. Admin creates courses and master recurrence.
4. Admin publishes catalog when registration should open.
5. Admin monitors enrollment dashboards and payment exceptions.

| Edge case | Behavior |
|-----------|----------|
| Mid-year new class section | Add course; enrollments only for new section; schedules generate forward. |
| Course cancelled | Hide from catalog; notify enrolled families; refund policy outside LMS rules. |

### User & staff lifecycle

| Staff type | Typical duties | Admin actions |
|------------|----------------|---------------|
| **Teachers** | Courses, grading, class announcements | Assign to courses; reset portal access; deactivate at year end |
| **TAs** | Teacher privileges in assigned class; student elsewhere | Link TA role to specific course ids |
| **Parent volunteers** | School-wide announcements, advertising/help, duty shifts | Grant scoped staff permissions without full admin |

### Volunteer & duty scheduling

- Calendar for duties (e.g. front desk, hall monitoring)
- **Reminder notifications** a few days before assigned shift (email/SMS when configured)
- Roster of who is on duty when; volunteers confirm or swap per school policy
- No-show tracking optional for admin follow-up

### Timetable management

Admins define the **master timetable**:

- Course / subject
- Time
- Classroom
- Teacher

**Teachers and admins** can:

- Reschedule a **single** session for conflicts (exception row, not silent drift of whole series)
- Assign a **substitute teacher** for one session with notification to roster optional

| Edge case | Behavior |
|-----------|----------|
| Double-booked room | Warn on save; allow override with admin note. |
| Holiday | Bulk skip sessions or mark non-instructional. |

### Enrollment & payments

- View enrollment and class rosters with export for office use
- Track paid / unpaid / partial status per student and term
- Override or assist registration when parents need help (linked to same cart/checkout rules)
- Mark offline payments received; parent portal reflects status

See [Registration & payment](registration-payment.md).

### System configuration

- Enable/disable [authentication](authentication.md) methods
- Manage [RBAC](rbac.md) roles and custom roles
- Reset credentials and assist account recovery with audit
- Payment gateway and tuition policy pointers ([tuition policies](tuition-policies.md))
- Contact info and calendar feeds ([contact and calendar](contact-and-calendar.md))

### Frontend ↔ backend map

All dynamic content on the public site and portals is configured here (or in the teacher portal for class-level items). See **[Frontend ↔ backend configuration map](frontend-backend-config.md)** for config paths and **two example use cases per feature**.

| Config area (admin) | Drives on frontend | Acceptance check |
|---------------------|-------------------|------------------|
| Academic year → Courses | [Course catalog](public-site-content.md#public-course-catalog), enrollment picker, schedules | Catalog price matches admin fee field after save. |
| Content → Homepage | [Homepage](public-homepage.md) announcements, events, hero | Public homepage shows pinned announcement within publish window. |
| Pricing → Tuition & discounts | Catalog prices, cart, [tuition page](tuition-policies.md) | Sibling discount appears in cart math for two children. |
| Master schedule & sessions | [Student](student-portal.md) / [parent](parent-portal.md) schedules | Rescheduled session shows new time on parent schedule view. |
| Communications | School-wide [announcements](announcements.md) | School-wide post visible to logged-in parent. |
| Settings | [Contact](contact-and-calendar.md), [authentication](authentication.md), payment gateways | Disabled login method hidden on sign-in page. |

## Requirements

| ID | Requirement | Detailed behavior | Edge cases | Acceptance criteria | Status |
|----|-------------|-------------------|------------|---------------------|--------|
| REQ-ADM-01 | Admin defines yearly courses, times, rooms, teachers. | CRUD on course instances per academic year; ties to master schedule generator. | Editing recurrence may prompt “this session only vs series.” | New course appears in catalog and teacher assignment list. | Confirmed |
| REQ-ADM-02 | Admin + teacher can reschedule individual sessions. | Exception record with audit (who/when); optional notify roster. | Past sessions may be locked from edit. | Single session time changes without moving other weeks. | Confirmed |
| REQ-ADM-03 | Admin + teacher can assign substitute for one session. | Substitute appears on schedule; scoped permissions per [RBAC](rbac.md). | Substitute cannot access unrelated courses. | Roster shows substitute name for that date only. | Confirmed |
| REQ-ADM-04 | Volunteer duty calendar with advance reminders. | Duty posts with assignee; cron sends reminder N days before. | Volunteer without email still sees duty in portal. | Reminder job fires in test environment for sample duty. | Confirmed |
| REQ-ADM-05 | Admin can view enrollment and payment status. | Filters by class, paid/unpaid, term; export CSV optional. | Refunds recorded as notes or negative lines per finance policy. | Admin dashboard lists unpaid enrollments for current term. | Confirmed |
| REQ-ADM-06 | Admin can create custom roles and assign permissions. | Effective permission preview per user. | Cannot remove last system admin without safeguard. | Custom role assignee gains only selected menus. | Confirmed |

## Related documents

- [School structure](school-structure.md)
- [Courses & learning](courses.md)
- [Announcements](announcements.md)
- [RBAC](rbac.md)
- [Frontend ↔ backend configuration map](frontend-backend-config.md)
