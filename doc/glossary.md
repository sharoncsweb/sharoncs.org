# Glossary

[← Wiki home](../README.md)

Terms below are used consistently across portal, registration, and RBAC documents. When two words appear in requirements (e.g. **course** vs **class**), use the definitions here to avoid ambiguous specs.

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Account, user, and student

![Account, user, and student](assets/diagrams/glossary-concepts.svg)

### Four portals

![Four portals](assets/diagrams/glossary-portals.svg)


## Core identity terms

| Term | Definition | Notes / edge cases |
|------|------------|-------------------|
| **Account** | A family / billing unit. Has one **primary owner**, zero or more **users** (parents/guardians), and one or more **students**. | All tuition checkout for the family runs through primary owner rules unless school policy changes. |
| **Primary owner** | The parent who may manage billing, payments, and adding/removing other users on the account. | Exactly one per account; transfer requires admin process. |
| **User** | A person with login credentials (typically a parent/guardian). May belong to more than one account in edge cases (shared guardianship). | Distinct from **Student** — users log in; students may or may not have their own login in v1. |
| **Student** | A child enrolled in the school. Belongs to **exactly one** account. | Cannot be duplicated across accounts; admin merge if historical duplicates exist. |
| **Family Identifier** | System-generated ID linking users and students on one account. | Shown in parent portal; support staff use it to look up families. |
| **Family Relationship** | How a person links to the account: **Self**, **Spouse**, or **Child**. | Drives which profile fields are required at registration. |

## Roles and access

| Term | Definition | Notes / edge cases |
|------|------------|-------------------|
| **Staff** | Umbrella for teachers, TAs, and parent volunteers performing school operations (not a single job title). | May hold multiple **School Assigned Role** values on one login. |
| **TA (Teaching Assistant)** | Staff in one class (teacher-level permissions there) but may be a **student** in another class. | Permissions are **per class** for TA scope; see [RBAC](rbac.md). |
| **RBAC** | Role-Based Access Control — permissions via roles and optional per-user grants. | Same person can be Parent + Teacher; UI merges capabilities without duplicate accounts. |
| **School Assigned Role** | Role label stored on a person (User or Student) for portal and admin features. | Multiple roles allowed; assignment may be admin-only for staff roles. |

## Academic structure

| Term | Definition | Notes / edge cases |
|------|------------|-------------------|
| **Grade** | Curriculum level label (e.g. Grade 2 Chinese) — may have multiple class sections. | Used for placement hints from “current regular school” grade. |
| **Class / section** | A concrete offering within a grade (e.g. Class A vs Class B) with its own time, teacher, and roster. | Student enrolls in a **class**, not only a grade name. |
| **Course** | A taught subject for a school year (e.g. Grade 2 Chinese — Class A), with schedule, room, and assigned teacher. | In docs, **course** often means the LMS + roster object for one section. |
| **Roster** | List of students enrolled in a class section. | Drives gradebook, attendance, and class announcements. |
| **Academic year** | Container for catalogs, registration, and rosters (e.g. 2025–2026). | Inactive years remain readable for history, not open for new parent self-enrollment unless admin opens. |

## Learning and delivery

| Term | Definition | Notes / edge cases |
|------|------------|-------------------|
| **LMS** | Learning Management System — assignments, materials, announcements, progress within courses. | Phase 2 depth; Phase 1 may expose read-only schedule and announcements. |
| **Delivery mode** | How course content is delivered: `internal` (platform), `google_classroom`, or `hybrid` (future). | v1 default: `internal` + in-person meetings. |
| **Assignment** | Teacher-created work with due date and submission rules (file upload, etc.). | Submissions visible to teacher; parent may see status per portal policy. |
| **Material** | File or link published in course hub (syllabus, handout). | Versioning and delete permissions follow teacher portal rules. |

## Portals and commerce

| Term | Definition | Notes / edge cases |
|------|------------|-------------------|
| **Parent portal** | Authenticated UI for guardians: family, enrollment, payments, student oversight. | Primary owner sees billing; spouse sees children per [Accounts](accounts.md). |
| **Student portal** | Authenticated UI for learners: schedule, course hubs, assignments. | Age-appropriate UX; mobile-friendly submission for photos/PDFs. |
| **Teacher portal** | Workspace for assigned classes: roster, materials, grading. | Substitute access may be time-limited (admin feature). |
| **Admin portal** | School operations: years, classes, payments, users, volunteers. | Highest privilege; audit sensitive actions. |
| **Enrollment** | Process of adding a student to a class section, usually with payment. | Distinct from merely creating a student profile. |
| **Cart** | Selected classes/fees before checkout. | Persisted across session where possible; see payment doc. |

## Usage examples (disambiguation)

| Phrase in conversation | Means |
|------------------------|--------|
| “Add a student” | Create **Student** on **Account**, not a new login User |
| “Sign up” | Create **User** + **Account** (Self) via registration |
| “Enroll in Grade 2” | Must pick **Class A or B** (section), not grade alone |
| “Teacher account” | **User** with Teacher role; may also be Parent on same login |

## Mobile and accessibility (terms in UX copy)

- **Verification code** — SMS OTP for phone signup; must be readable in mobile SMS app and entered in one field with clear expiry message.
- **Primary parent** — UI label aligned with **primary owner** in data model; avoid two different labels on checkout vs settings.

See [Parent portal](parent-portal.md), [Accounts & enrollment](accounts.md), and [Registration — user fields](registration-user-fields.md).
