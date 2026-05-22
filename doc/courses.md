# Courses & learning

[← Wiki home](../README.md)

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Course lifecycle

![Course lifecycle](assets/diagrams/courses-lifecycle.svg)

### In-person plus LMS

![In-person plus LMS](assets/diagrams/courses-in-person.svg)

### Course page layout

![Course page layout](assets/diagrams/courses-classroom-style.svg)


## Philosophy

Learning is **primarily in-person**. The LMS supports assignments, exams, communication (announcements, feedback), materials (PDFs, videos, notes), and scheduling with academic tracking. It should **not** assume fully online video-first instruction in v1.

Teachers use the portal to publish what students need between class meetings; admins own the catalog, roster linkage, and master schedule that define *which* course instances exist for the year.

## Backend configuration

| Frontend (dynamic) | Configure in admin / teacher | Detailed behavior |
|--------------------|------------------------------|-------------------|
| Catalog course name, fee, schedule summary | **Admin → Academic year → Courses** | Public catalog and enrollment picker read the same course record; fee and discount rules come from pricing config. |
| Student course page content | **Teacher portal → Course → Content** | Draft vs published states; hidden items stay invisible to students and parents. |
| Class announcements on course page | **Teacher portal → Course → Announcements** | Scoped to enrolled roster only; appears on student course page and parent visibility for that child. |
| Single-session time / substitute | **Admin → Master schedule** · **Teacher/Admin → Session → Reschedule** | Overrides one occurrence without rewriting the whole recurring series unless admin chooses “apply to series.” |

See **[Frontend ↔ backend configuration map](frontend-backend-config.md)**.

## Course lifecycle

### Annual setup (admin)

At the start of each school year, administrators define course instances tied to grade, class, and academic year:

| Field | Example | Edge cases |
|-------|---------|------------|
| Course name | Grade 2 Chinese — Class A | Duplicate display names allowed if internal codes differ; catalog should show distinguishing schedule or room. |
| Schedule | Day, time, recurrence | Holidays and school closures may suppress sessions without deleting the course. |
| Classroom | Room / location | Optional for v1; if empty, portals show time and teacher only. |
| Assigned teacher | Primary instructor | Substitute and co-teacher fields apply per session, not necessarily yearly assignment. |
| Capacity / waitlist | 24 seats | Enrollment may block checkout when full; waitlist policy is school-configurable. |

**Workflow — yearly course creation**

1. Admin opens academic year and confirms grades/classes exist ([School structure](school-structure.md)).
2. Admin creates each course with schedule template (recurring rule).
3. Admin assigns primary teacher and links catalog metadata (fee, description).
4. System generates session rows from recurrence (or on first publish).
5. Rosters populate as parents enroll; teachers see courses only after assignment + enrollment.

### Ongoing (teacher)

Teachers for each assigned course can:

- Upload **videos**, **PDFs/notes**, **assignments** with file size limits per school policy
- Organize content flexibly (modules/lessons optional — **Google Classroom–like** ordering)
- Control **what students see** on the course page (publish/hide per item)
- Create assignments and exams with attachments and due dates/time zones
- Assign **different work to different students** in the same class (differentiation groups or individual overrides)
- Post class announcements that respect enrollment as of post time (drops may lose visibility going forward)

**Edge cases — teacher operations**

| Situation | Expected behavior |
|-----------|-------------------|
| Student added mid-year | Gains access to published materials; past-due assignments may still show as overdue unless teacher exempts. |
| Student transfers class | Loses old class hub; historical grades remain in records per retention policy. |
| Teacher substitute for one session | Substitute sees session on schedule and grading tools if granted; primary teacher retains course ownership. |
| Unpublished module | Students and parents do not see items; TAs follow teacher visibility rules. |

## Requirements

| ID | Requirement | Detailed behavior | Edge cases | Acceptance criteria | Status |
|----|-------------|-------------------|------------|---------------------|--------|
| REQ-CRS-01 | Admin defines courses yearly (name, schedule, room, teacher). | Course records are versioned per academic year; copying prior year is optional helper, not automatic overwrite. | Archived years are read-only for scheduling; edits require admin role. | Admin can create, edit, and archive a course; catalog and master schedule reflect changes within one minute (or stated SLA). | Confirmed |
| REQ-CRS-02 | Teachers manage course content and visibility. | CRUD on modules/materials/assignments within assigned courses only; publish flag gates student UI. | TA in course A has same content powers as teacher there; in other courses, no teacher tools. | Hidden item never appears in student API/UI; published item visible to enrolled students. | Confirmed |
| REQ-CRS-03 | Course page includes materials, assignments, announcements, progress. | Single hub per enrollment; progress aggregates submission and graded states. | Parent view may omit draft teacher notes marked internal. | Student sees four sections when enabled; empty sections collapse or show friendly empty state. | Confirmed |
| REQ-CRS-04 | Teachers can reschedule a **single session** with admin (occasional conflicts). | Creates exception row linked to master session; notifications optional to roster. | Conflicting room/teacher double-booking should warn admin before save. | One session moves time/room without shifting unrelated sessions. | Confirmed |
| REQ-CRS-05 | Teachers and admins can assign a **substitute teacher** for one session. | Substitute gains session-scoped access; primary teacher remains owner of course config. | Substitute who is also a student in another class still only gets substitute tools for that session. | Roster shows substitute name for that date; substitute can take attendance/grade if permitted. | Confirmed |
| REQ-CRS-06 | Course structure should mirror **Google Classroom** usability where practical. | Stream-like ordering, attachments on assignments, simple status (assigned/submitted/graded). | Full parity with Google Classroom not required in v1. | Usability review: teacher can post assignment with attachment in under 2 minutes without training doc. | Confirmed |

## Delivery modes (future)

| `delivery_mode` | Description | Platform still owns |
|-----------------|-------------|---------------------|
| `internal` | All LMS features in this platform (default v1) | — |
| `google_classroom` | External classroom for assignments/materials/grading | Registration, payments, accounts, scheduling, school/class announcements |
| `hybrid` | Combination per course | Clear labeling on course page so families know where to submit work |

## Course page (student view)

Controlled by teacher; may include lessons or modules, learning materials (PDF, video, notes), assignments and due dates, teacher announcements, and progress tracking. Students who print attachments complete work offline and upload PDF or photos per [Student portal](student-portal.md).

**Acceptance criteria — student course hub**

- Enrolled student opening course lands on teacher-published content only.
- Overdue assignments show due date and status; submitted work shows timestamp.
- Class announcements appear in chronological order with author role (teacher/TA).

## Related documents

- [School structure](school-structure.md)
- [Student portal](student-portal.md)
- [Teacher portal](teacher-portal.md)
- [Admin portal](admin-portal.md)
