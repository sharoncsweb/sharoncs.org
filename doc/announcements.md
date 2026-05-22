# Announcements & activity feed

[← Wiki home](../README.md)

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Who can post

![Who can post](assets/diagrams/announcements-who-posts.svg)

### Who sees what

![Who sees what](assets/diagrams/announcements-visibility.svg)

### How families receive news

![How families receive news](assets/diagrams/announcements-delivery.svg)


## Overview

The platform provides an **activity feed** and **announcements** with role-based posting and visibility scopes. School-wide items surface on the parent dashboard, student dashboard (where applicable), and public homepage when configured. Class-level items attach to course rosters and appear on course hubs.

Feeds are **read-mostly** for families; authoring is limited to roles with explicit permissions ([RBAC](rbac.md)).

## Backend configuration

| Frontend (dynamic) | Configure in admin | Detailed behavior | Edge cases |
|--------------------|-------------------|-------------------|------------|
| Public homepage announcements / events | **Admin → Content → Homepage → Announcements / Events** | May schedule publish/start/end; unpublish removes from public site. | Expired events move to archive, not deleted without confirm. |
| School-wide feed (logged in) | **Admin → Communications → School announcements** (or staff post UI) | Visible to all authenticated school users unless future grade filter applies. | Draft school post invisible until published. |
| Class announcements | **Teacher portal → Course → Announcements** | Scoped to current enrollment; parents see via child linkage. | Post before enrollment day may use “all future roster” rule per policy. |

Full table: **[Frontend ↔ backend configuration map](frontend-backend-config.md)**.

## Who can post

| Role | Scope | Detailed behavior | Edge cases |
|------|--------|-------------------|------------|
| **Admin** | School-wide | Full HTML/markdown subset; pin to top; optional email blast later. | Emergency closure posts may bypass quiet hours if configured. |
| **Staff** (incl. certain volunteers) | School-wide | Permission `announcement.school.create` required. | Volunteer without permission sees read-only feed. |
| **Teachers** | Their class(es) | Posts tagged with `course_id`; TAs inherit in scoped courses. | Teacher removed mid-year loses create on that course. |
| **TAs** | Class(es) where they assist | Same as teacher for announcement create if TA role active in course. | Cannot post school-wide unless also staff role. |

Parent volunteers helping with **advertising** or school communications may receive staff-level announcement permissions without gradebook access.

## Visibility levels

| Level | Status | Example | Detailed behavior | Acceptance criteria |
|-------|--------|---------|-------------------|---------------------|
| **School-wide** | Confirmed | Registration opens, holiday closure | Appears on parent/staff feeds; homepage if flagged. | Parent with no enrollments still sees school-wide items when logged in. |
| **Class-specific** | Confirmed | Field trip reminder for Class A | Filtered by enrollment at view time. | Student in Class A sees post; student only in Class B does not. |
| **Grade-level** | Future | All Grade 2 Chinese families | Targets grade + subject without picking each section. | TBD when implemented |

## Feed behavior

| Concern | Behavior |
|---------|----------|
| Ordering | Reverse chronological; pinned school items stay top until unpinned. |
| Read state | Optional “mark read” per user; unread badge on portal entry. |
| Attachments | Images/PDF allowed within size limits; virus scan per infra policy. |
| Edit/delete | Author or admin may edit within window; audit trail for school-wide edits. |
| Moderation | Admin can hide inappropriate class posts without deleting grade data. |

**Workflow — class announcement**

1. Teacher opens **Course → Announcements → New**.
2. Teacher composes title/body and optional attachments.
3. System validates `course.announcement.create` and enrollment scope.
4. On publish, feed entries created for enrolled students and linked parents.
5. Optional notification queue (email/SMS/WeChat) when integrations exist.

## Requirements

| ID | Requirement | Detailed behavior | Edge cases | Acceptance criteria | Status |
|----|-------------|-------------------|------------|---------------------|--------|
| REQ-ANN-01 | Admin and staff can create **school-wide** announcements. | Permission-gated composer; schedule and pin supported. | Staff without permission denied with clear message. | School-wide post visible to two test parents in different families. | Confirmed |
| REQ-ANN-02 | Teachers and TAs can create **class-level** announcements. | Course-scoped; shows on course page and child visibility for parents. | TA outside course cannot post. | Class post not visible to non-enrolled student. | Confirmed |
| REQ-ANN-03 | Feed respects visibility so users only see relevant posts. | Server-side filter; no client-only hiding. | User with multiple children sees union of class posts. | API returns only scoped items for test tokens. | Confirmed |
| REQ-ANN-04 | Grade-level targeting may be added later. | Data model may tag `grade_id` without breaking v1 scopes. | — | Feature flagged off in v1. | Future |

## Public website overlap

Legacy site sections (*Announcement*, *News*) should migrate into this model or dedicated CMS pages on the new public site. Coordinate content strategy with [Overview](overview.md). Public homepage may show subset of school-wide posts marked **public**; logged-in feed may show additional internal items.

## Related documents

- [RBAC](rbac.md)
- [Teacher portal](teacher-portal.md)
- [Admin portal](admin-portal.md)
- [Parent portal](parent-portal.md)
