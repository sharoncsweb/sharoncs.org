# School structure

[← Wiki home](../README.md)

Instruction is organized by **grade** (curriculum level) and **class sections** (schedulable offerings). This page defines how rosters, placement, and announcements attach to that hierarchy.

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Grade with multiple classes

![Grade with multiple classes](assets/diagrams/school-grade-classes.svg)

### Student picks a class

![Student picks a class](assets/diagrams/school-pick-class.svg)

### Placement hints

![Placement hints](assets/diagrams/school-placement.svg)


## Hierarchy

Sharon Chinese School organizes instruction roughly as:

```
Grade (e.g. Grade 2 Chinese)
 └── Class A  (time, teacher, room, roster)
 └── Class B  (different time/teacher possible)
      └── Students (enrolled per class)
```

**Admin workflow:** For each academic year, create grades, then create one or more **sections** per grade with capacity, schedule, and assigned teacher. Parents never enroll in a grade label alone—they select a **section** that fits schedule and placement.

## Requirements

| ID | Requirement | Acceptance criteria | Status |
|----|-------------|---------------------|--------|
| REQ-SCH-01 | A **grade** can have **multiple classes** (sections). | Admin UI lists multiple sections under one grade; parent enrollment shows each section separately. | Confirmed |
| REQ-SCH-02 | Classes under the same grade may differ in **time**, **teacher**, and **room**. | Each section record stores independent schedule/teacher/room; roster queries use section ID. | Confirmed |
| REQ-SCH-03 | Example: *Grade 2 Chinese* → *Class A* and *Class B*. | Seed or demo data matches example for UAT scripts. | Confirmed |
| REQ-SCH-04 | Students enroll in specific **class offerings**, not only a grade label. | Checkout and roster rows reference section ID; grade alone does not create enrollment. | Implied |

## Example

| Grade | Class | Schedule | Teacher | Room | Capacity |
|-------|-------|----------|---------|------|----------|
| Grade 2 Chinese | A | Sat 9:00 | Ms. Li | Room 101 | 20 |
| Grade 2 Chinese | B | Sat 11:00 | Mr. Wang | Room 102 | 20 |

## Placement workflow (parent + system)

1. Parent enters student **current regular school** and **grade** (see [Registration — user fields](registration-user-fields.md)).
2. Registration UI suggests eligible **grades/sections** (school rules: age, prior Sharon level, or assessment — confirm rule table with committee).
3. Parent selects **one section per student per subject** unless school allows multiple (e.g. culture elective).
4. On successful payment (if required), student appears on **roster** and **schedule**.

### Placement edge cases

| Case | Handling |
|------|----------|
| Student new to Sharon, unclear level | Admin override placement or hold enrollment until assessed |
| Sibling in different section same grade | Allowed if schedule fits; no automatic “same class as sibling” unless school adds rule |
| Student repeats level | Admin assigns section; history from prior year visible to admin |
| Mid-year transfer between A/B | Admin moves roster; parent sees updated schedule; payment adjustment admin-mediated |

## Roster rules

- Student belongs to one **account** (family)
- Student may be enrolled in one or more **courses/classes** per semester/year (per school policy on electives)
- Class roster drives teacher gradebook and announcements
- **Capacity:** When section is full, registration follows waitlist or block per [Registration & payment](registration-payment.md)
- **Dropped students:** Admin or parent-initiated drop removes roster row; financial credit per school policy

### Roster integrity

| Rule | Detail |
|------|--------|
| Uniqueness | Same student should not appear twice in the same section |
| Active year | Roster queries default to active academic year |
| Teacher view | Teacher sees only sections they are assigned to |
| Substitute | Substitute teacher access is time-bound and does not change roster ownership |

## Schedule aggregation

- **Student schedule** = union of all enrolled sections’ meeting times
- **Conflict detection:** If two sections overlap in time, block at cart or warn (school preference — specify in UAT)
- **One-off changes:** Admin reschedules single session; calendars update for affected section only (see admin portal doc)

## Announcement targeting

| Level | Example | Who posts (see [Announcements](announcements.md)) | Audience |
|-------|---------|--------------------------------------------------|----------|
| School-wide | Snow day, registration open | Admin, staff | All authenticated users + public where applicable |
| Class-specific | Homework due Friday | Teacher, TA | Roster students and linked parents |
| Grade-level | Optional future | TBD | All families with student in any section of that grade |

**Edge case:** Student in Class A must not receive Class B-only posts unless also enrolled there.

## Mobile and accessibility

- Section picker in registration shows **time and teacher** on small screens without requiring horizontal table scroll.
- Schedule views use local timezone for Saturday sessions; clear date format (e.g. Sat, Sep 14, 9:00 AM).
- Screen readers: section names announced as “Grade 2 Chinese, Class A, Saturday 9:00 AM, Room 101.”

## Related documents

- [Courses & learning](courses.md)
- [Registration & payment](registration-payment.md)
- [Accounts & enrollment](accounts.md)
- [School structure → parent enrollment UI](parent-portal.md)
