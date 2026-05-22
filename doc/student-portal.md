# Student portal

[← Wiki home](../README.md)

## Audience

Logged-in **students**. Parents monitor and manage children through the **[Parent portal](parent-portal.md)** (schedule, assignments, progress)—not by default through this portal. Confirm with school whether young students without their own login use parent-only access or a future “view as student” mode from the parent account.

Students only see **their own** enrollments, submissions, and grades ([REQ-RBAC-06](rbac.md)).

## Backend configuration

| Frontend (dynamic) | Configure in admin / teacher | Detailed behavior | Edge cases |
|--------------------|------------------------------|-------------------|------------|
| Daily / weekly schedule | **Admin → Academic year → Master schedule** (+ session overrides) | Dashboard “today” aggregates sessions for local school timezone. | Cancelled session shows status label, not hidden silently. |
| Course list (enrolled) | **Admin → Enrollment → Rosters** | Only current-year active enrollments. | Dropped course removed from list; history policy TBD. |
| Materials, homework, grades | **Teacher portal → Course → …** | Respects teacher publish and grade return. | Ungraded submission shows pending state. |

Full map: **[Frontend ↔ backend configuration map](frontend-backend-config.md#student-portal)**.

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Student dashboard

![Student dashboard](assets/diagrams/student-dashboard.svg)

### Inside a course

![Inside a course](assets/diagrams/student-course-page.svg)

### Submit homework

![Submit homework](assets/diagrams/student-homework.svg)


## Primary features

### Dashboard

- **Daily schedule** — subjects, times, teachers, optional room/location; tap for week view
- **Task overview** — upcoming assignments and exams across courses sorted by due date
- **School-wide feed** — read-only slice of announcements not tied to a single class (when enabled)

**Workflow — school morning check-in**

1. Student signs in (or stays signed in on family device).
2. Dashboard shows today’s sessions and any all-day school notice.
3. Student opens **Tasks** to see due within 7 days.
4. Student enters course hub to download materials or submit work.

### Per-course page

Each enrolled course exposes a learning hub (teacher-controlled visibility):

| Content | Description | Edge cases |
|---------|-------------|------------|
| Lessons / modules | Structured units when teacher organizes them | Empty module hidden or shows “no materials yet.” |
| Materials | PDFs, videos, notes | External video links open in new tab with safety policy. |
| Assignments | Due dates, attachments, submission status | Late submit allowed only if teacher enables. |
| Announcements | Class-specific posts from teacher or TA | Read-only; no student replies in v1 unless specified later. |
| Progress | Completion and grading summary where applicable | Withheld grades until teacher returns work. |

### Submissions

Students complete work offline when needed: print teacher attachment, work on paper, photograph or scan to PDF, upload before due time. File types and size limits match teacher portal constraints.

| Edge case | Behavior |
|-----------|----------|
| Upload fails mid-network | Retry preserves draft if implemented; else clear error. |
| Multiple photos | Allow multi-file merge or single PDF per assignment policy. |
| Wrong file uploaded | Resubmit if teacher allows; else contact teacher/parent. |

## Requirements

| ID | Requirement | Detailed behavior | Edge cases | Acceptance criteria | Status |
|----|-------------|-------------------|------------|---------------------|--------|
| REQ-STU-01 | Students see a **daily schedule** on the dashboard. | At least today + next session; week view optional. | No classes today shows friendly empty state. | Schedule matches admin master data for enrolled courses. | Confirmed |
| REQ-STU-02 | Master schedule data is **admin-defined** for the year; teachers/admins may adjust single sessions. | Exceptions overlay recurring rule. | Student sees updated time after exception publish. | Rescheduled session reflects new time on dashboard. | Confirmed |
| REQ-STU-03 | Course pages show materials, assignments, announcements, and progress as enabled by teacher. | Sections collapse when empty. | Parent parallel view may match visibility rules. | Published material visible; hidden material not. | Confirmed |
| REQ-STU-04 | Students submit assignment/exam work as **PDF or image** uploads after printing attachments if needed. | Timestamp recorded; teacher notified optional. | HEIC converted or rejected with message. | Successful upload moves status to submitted. | Confirmed |
| REQ-STU-05 | Students only access **their own** data and enrolled courses. | Authorization on every API by student id. | Sibling on same account cannot switch without own login. | Tampered course id returns forbidden. | Confirmed |

## Schedule fields

Each schedule entry should support at minimum:

- Subject / course
- Teacher (primary or substitute for that session)
- Time slot (start/end, timezone)
- Classroom / location (optional)
- Status (scheduled, rescheduled, cancelled)

## Related documents

- [Parent portal](parent-portal.md)
- [Courses & learning](courses.md)
- [Teacher portal](teacher-portal.md)
- [School structure](school-structure.md)
- [RBAC](rbac.md)
