# Announcements & activity feed

[← Wiki home](../README.md)

## Diagrams

**Characters:** Parent · Student (ages 7–13) · Teacher · Admin · School

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

Communications happen in **three places**:

| Channel | Audience | Who publishes |
|---------|----------|----------------|
| **[Public homepage](public-homepage.md)** | Anyone on the internet | Users with homepage permissions (admin, staff, teachers, etc.) |
| **School-wide feed** (logged in) | Families and staff in the platform | Admin and staff (typical); permission-based |
| **Class-level feed** | One class | Teachers and TAs for that class |

This page covers **authenticated** feeds. For the **landing page**, hero, events, and public announcements, see **[Public homepage](public-homepage.md)**.

## Who can post (inside the platform)

| Role | Scope |
|------|--------|
| **Admin** | School-wide |
| **Staff** (incl. certain volunteers) | School-wide |
| **Teachers** | Their class(es) |
| **TAs** | Class(es) where they assist |

Parent volunteers helping with **advertising** or school communications may receive staff-level announcement permissions.

Homepage publishing uses separate permissions (`homepage.post_*`)—see [RBAC](rbac.md).

## Visibility levels

| Level | Status | Example |
|-------|--------|---------|
| **School-wide** | Confirmed | Registration opens, holiday closure |
| **Class-specific** | Confirmed | Field trip reminder for Class A |
| **Grade-level** | Future | All Grade 2 Chinese families |

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-ANN-01 | Admin and staff can create **school-wide** announcements. | Confirmed |
| REQ-ANN-02 | Teachers and TAs can create **class-level** announcements. | Confirmed |
| REQ-ANN-03 | Feed respects visibility so users only see relevant posts. | Confirmed |
| REQ-ANN-04 | Grade-level targeting may be added later. | Future |
| REQ-ANN-05 | Public homepage announcements/events documented in [public homepage](public-homepage.md). | Confirmed |

## Related documents

- [Public homepage & landing page](public-homepage.md)
- [RBAC](rbac.md)
- [Teacher portal](teacher-portal.md)
- [Admin portal](admin-portal.md)
