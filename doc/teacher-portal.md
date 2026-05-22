# Teacher portal

[← Wiki home](../README.md)

## Backend configuration

| Frontend (dynamic) | Configure in admin / teacher | Detailed behavior | Edge cases |
|--------------------|------------------------------|-------------------|------------|
| My courses list | **Admin → Academic year → Courses** (teacher assignment) | List filters to current year and assignments; substitutes see session-only entries. | Teacher removed from course disappears from list next login. |
| Session schedule & substitutes | **Admin → Master schedule** · **Session → Reschedule** | Calendar view with exceptions highlighted. | Past sessions read-only for schedule edits per policy. |
| Course materials, assignments, grades | **Teacher portal → Course → Content / Assignments / Grading** | Publish gates student visibility. | Large uploads fail gracefully with size message. |
| Class announcements | **Teacher portal → Course → Announcements** | Same scope as [Announcements](announcements.md) class level. | Draft announcement not visible to families. |

Full map: **[Frontend ↔ backend configuration map](frontend-backend-config.md#teacher-portal)**.

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Teacher workspace

![Teacher workspace](assets/diagrams/teacher-workspace.svg)

### Grading flow

![Grading flow](assets/diagrams/teacher-grading.svg)

### TA has two roles

![TA has two roles](assets/diagrams/teacher-ta-dual.svg)


## Audience

**Teachers** and **TAs** (in classes where they act as teacher). Substitutes with session-scoped grants use a subset of tools for that session only. Users who are also parents or students switch portal context without a second account ([RBAC](rbac.md)).

## Primary features

### My courses

- List of assigned courses for the current school year with roster counts and next session hint
- Quick access to each course’s content, grading queue, and announcements
- Search/filter when teacher has many sections

### Course content management

- Create and organize modules/lessons (flexible, Google Classroom–style)
- Upload videos, PDFs, notes with publish/hide per item
- Post **class-level** announcements (with TA where permitted)
- Optional duplication from prior year template if school enables

**Workflow — publish weekly materials**

1. Teacher opens course **Content**.
2. Teacher uploads files or links into module.
3. Teacher sets visibility **Published**.
4. Enrolled students and parents see items on next page load.
5. Teacher edits or hides item without deleting submission history tied to assignments.

### Assignments & exams

| Capability | Detail | Edge cases | Acceptance criteria |
|------------|--------|------------|---------------------|
| Create work | Assignments and exams with **attachments** | Due date timezone uses school default. | Student can download attachment and see due date. |
| Differentiation | Assign **different work to different students** in the same class | Subsets by name pick or group tag. | Student A does not see Student B exclusive assignment. |
| Submissions | Students upload **PDF or photos** of completed work | Resubmit allowed if teacher enables. | Teacher inbox lists unsubmitted vs submitted counts. |
| Grading | Score, feedback, return to student | Bulk download submissions optional later. | Returned grade visible to student and parent per visibility rules. |

### Schedule operations

- View master timetable for assigned courses with exception badges
- **Reschedule a single class** (with admin alignment on policy — may require admin approval flag)
- Request or record **substitute teacher** for a session; roster sees updated teacher name

| Edge case | Behavior |
|-----------|----------|
| Teacher absent emergency | Admin can enter substitute without teacher login. |
| Session in past | Gradebook still accessible; schedule edit may be blocked. |

## Requirements

| ID | Requirement | Detailed behavior | Edge cases | Acceptance criteria | Status |
|----|-------------|-------------------|------------|---------------------|--------|
| REQ-TCH-01 | Teachers create assignments and exams with attachments. | Title, description, due, attachments, points optional. | Zero-byte file rejected. | Assignment appears on student course page after publish. | Confirmed |
| REQ-TCH-02 | Teachers grade PDF/image submissions with feedback. | Inline viewer or download; score + comment saved. | Rotated phone images display readable. | Student sees score after teacher returns grade. | Confirmed |
| REQ-TCH-03 | Teachers can target assignments to subsets of students. | Per-student or group selection stored on assignment. | New student added after assign may be excluded until teacher updates. | Only targeted students see assignment card. | Confirmed |
| REQ-TCH-04 | Teachers control student-visible content on course pages. | Publish flag on each content node. | Hidden module does not leak via direct URL. | Unpublished item returns 404 or forbidden for student token. | Confirmed |
| REQ-TCH-05 | Teachers and TAs may post **class-level** announcements. | Permission check on `course_id`. | TA not in course cannot post. | Announcement visible to enrolled parent within one minute. | Confirmed |
| REQ-TCH-06 | Teachers can reschedule individual sessions (with admin). | Creates schedule exception; may notify families. | Conflict detection surfaces to user. | One session moves without altering other weeks. | Confirmed |
| REQ-TCH-07 | Teachers can assign substitute for a single session. | Substitute user picker limited to staff/teacher pool. | Substitute who is a student elsewhere still only gets session scope. | Schedule shows substitute for that session date. | Confirmed |

## TA note

A user who is **TA** in Course A has teacher-level tools in Course A only. In courses where they are enrolled as a **student**, they see the [student portal](student-portal.md) only. UI should label active **course context** when both apply to prevent mis-posts.

See [RBAC](rbac.md).

## Related documents

- [Courses & learning](courses.md)
- [Admin portal](admin-portal.md)
- [Announcements](announcements.md)
- [Student portal](student-portal.md)
