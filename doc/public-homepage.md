# Public homepage & landing page

[← Wiki home](../README.md)

## Summary

The **public homepage** is the first thing visitors see (prospective families, current parents, and the community). It must look **professional and modern**, with a strong **hero section**, and it must surface **school events** and **announcements** published by authorized staff—not a static brochure only.

Publishing is **permission-based**: administrators, teachers, staff, and other roles may post **only if** they are granted the right permissions (see [RBAC](rbac.md)).

---

## Goals

| Goal | Detail |
|------|--------|
| **Professional first impression** | Clean layout, readable typography, consistent branding, works on mobile and desktop |
| **Modern landing experience** | Contemporary patterns (clear hierarchy, spacing, calls-to-action)—not the cluttered legacy site |
| **Timely public content** | Events and announcements updated by the school without developer involvement |
| **Controlled publishing** | Only users with explicit permissions can add or edit homepage content |

---

## Page structure (recommended)

### Hero section

The hero is the top of the landing page and sets the tone for the whole site.

| Element | Requirement |
|---------|-------------|
| **Headline** | Clear value proposition (e.g. Sharon Chinese School — community, language, culture) |
| **Supporting line** | Short subtitle (location, weekend program, registration window) |
| **Primary CTA** | Prominent action: Register / Sign in / Learn more |
| **Visual** | Professional imagery or illustration (school-appropriate; vendor to propose) |
| **Layout** | Full-width, balanced whitespace; readable on phone and desktop |

*Avoid*: cluttered rotating banners, tiny text, or dated table-based layouts like the legacy site.

### Below the hero

| Section | Purpose |
|---------|---------|
| **Announcements** | Important short notices (closures, registration dates, policy reminders) |
| **Events** | Upcoming school events (open house, performances, holidays, community activities) |
| **Quick links** | About, classes, contact, login (as needed) |
| **Optional** | Gallery, teaching highlights, or news—migrate from legacy site over time |

Order and exact blocks can be refined with The Web Design LLC; announcements and events are **required** on the homepage.

---

## Who can publish (permission-based)

Posting to the **public homepage** is **not** automatic for every teacher or staff member. The system checks **permissions**, not job titles alone.

| Typical grantee | Homepage permissions (examples) |
|-----------------|----------------------------------|
| **Administrator** | Full: create, edit, publish, unpublish, feature on hero |
| **Staff / communications volunteer** | Post announcements and events when granted |
| **Teacher** | Post only if admin assigns permission (e.g. event for their class or school activity) |
| **Parent / student** | No homepage publishing (read-only on public site) |

### Suggested permissions (RBAC)

| Permission | Allows |
|------------|--------|
| `homepage.post_announcement` | Add/edit homepage announcement items |
| `homepage.post_event` | Add/edit homepage event items |
| `homepage.publish` | Make items visible on the live site (or schedule publish) |
| `homepage.manage` | Admin: all content, ordering, hero highlights, archive |

Admins assign these to **roles** or **individual users** (same model as the rest of the platform).

### Content workflow (recommended)

1. Authorized user signs in (not anonymous posting).
2. Creates draft **announcement** or **event** (title, body, date, optional image/link).
3. Previews how it appears on the homepage.
4. Publishes (or submits for admin approval—**TBD** with school).
5. Item appears in the correct homepage section; optional end date hides it automatically.

---

## Announcements vs events

| Type | Use for | Homepage display |
|------|---------|------------------|
| **Announcement** | Short notices, urgent updates, registration reminders | Announcements list / strip near hero |
| **Event** | Dated activities (open house, party, performances, no-school days) | Events list sorted by date (upcoming first) |

Both types are **public** (visible without login). Logged-in users may see the same items again inside portals—see [Announcements](announcements.md).

---

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-HOME-01 | Public homepage has a **professional, modern** design. | Confirmed |
| REQ-HOME-02 | Landing page includes a **professional hero section** with headline and primary CTA. | Confirmed |
| REQ-HOME-03 | Homepage displays **school announcements** and **events** sections. | Confirmed |
| REQ-HOME-04 | Users with the right **permissions** (admin, teacher, staff, etc.) can publish homepage content. | Confirmed |
| REQ-HOME-05 | Users **without** permission cannot publish to the homepage. | Confirmed |
| REQ-HOME-06 | Homepage is **mobile-friendly** and accessible. | Confirmed |
| REQ-HOME-07 | Legacy *Announcement* / *News* content migrates into this model over time. | Planned |

---

## Open items (confirm with school / vendor)

| Topic | Question |
|-------|----------|
| Approval workflow | Publish immediately vs admin approval for non-admin roles? |
| Hero editing | Who may change hero headline/image—admin only? |
| Bilingual copy | English only on public site, or English + Chinese toggle? |
| Featured event | Pin one event in or near the hero? |

---

## Diagrams

**Characters:** Parent · Student (ages 7–13) · Teacher · Admin · School

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Homepage layout

![Homepage layout](assets/diagrams/homepage-layout.svg)

### Permission-based publishing

![Permission-based publishing](assets/diagrams/homepage-publish-flow.svg)

### Public site vs logged-in portals

![Public site vs logged-in portals](assets/diagrams/homepage-vs-portals.svg)


## Related documents

- [Announcements & activity feed](announcements.md) — school-wide and class feeds inside the platform
- [RBAC](rbac.md) — permissions and roles
- [Admin portal](admin-portal.md) — content and configuration
- [Project overview](overview.md) — legacy site and overall scope
- [Platform structure](platform.md)
