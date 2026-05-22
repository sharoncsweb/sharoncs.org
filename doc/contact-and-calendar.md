# Contact & school calendar

[← Wiki home](../README.md)

## Contact page

A dedicated **Contact us** page is required on the public site (legacy: `/school/page/contact_us`).

### Display on every public page

| Element | Value (verify with school) |
|---------|----------------------------|
| **Email** | admin@sharoncs.org |
| **Phone** | (781) 363-1186 |
| **Class location** | 900 Washington St, Canton, MA 02021 (Canton High School) |

### Contact page body

| Section | Content |
|---------|---------|
| **General inquiries** | Email and phone with click-to-call / mailto |
| **Where classes meet** | Canton High School address; map link (Google Maps) |
| **Mailing address** | Legacy lists **618 Canton St, Westwood MA 02090** for mail — **confirm single official mailing address** with school (do not show two conflicting addresses without labels) |
| **Hours** | Weekend school hours or “contact by email” (TBD) |
| **Registration help** | Link to [registration flow](registration-flow.md) |

---

## School calendar (public)

Legacy: [School calendar and schedule](https://www.sharoncs.org/school/page/school_calendar).

| Requirement | Detail |
|-------------|--------|
| **Purpose** | Show **academic year** key dates: first/last day, holidays, no-school days, registration deadlines |
| **Format** | PDF download and/or on-page calendar view |
| **Updates** | Admin or staff with permission republish each year |
| **Distinction** | Not the same as per-student **class schedule** in the LMS (see [student portal](student-portal.md)) |

### Workflow — update contact (admin)

1. Treasurer or admin edits **Admin → Settings → School contact**.
2. Saves email, phone, class location, and labeled mailing address.
3. Contact page and all public footers refresh from the same settings record.

### Workflow — publish school calendar (admin)

1. Admin uploads annual PDF and/or enters key dates in **Admin → Content → School calendar**.
2. Aligns registration deadline dates with **Registration → Seasons & deadlines**.
3. Publishes; public calendar page and optional homepage link show new year.

### Acceptance criteria

- Contact page shows click-to-call phone, mailto email, class location with map link, and clearly labeled mailing address once school confirms (REQ-CON-01, REQ-CON-02).
- Footer on every public page includes email, phone, and Canton class location (REQ-CON-04).
- School calendar displays academic year boundaries, holidays, and no-school days (REQ-CON-03).
- Registration help section links to [registration flow](registration-flow.md).

### Edge cases

- **Two addresses without labels** — never show mailing and class addresses ambiguously; use “Classes meet at” vs “Mail to”.
- **Calendar PDF inaccessible** — provide HTML list of dates and PDF download side by side.
- **Wrong year published** — admin can unpublish calendar until corrected; homepage should not link stale PDF.
- **Snow day added late** — admin adds exception date; optional mirror as homepage announcement.

## Backend configuration

| Frontend (dynamic) | Configure in admin |
|--------------------|-------------------|
| Contact page & footer email/phone/addresses | **Admin → Settings → School contact** |
| Public school calendar (PDF / view) | **Admin → Content → School calendar** |

See **[Frontend ↔ backend configuration map](frontend-backend-config.md)**.

---

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-CON-01 | Public **Contact** page with email, phone, and labeled addresses. | Confirmed |
| REQ-CON-02 | Resolve and document **one** mailing vs **class** address on the site. | Open (school) |
| REQ-CON-03 | Public **school calendar** for the academic year. | Confirmed |
| REQ-CON-04 | Footer on all public pages includes email, phone, Canton location. | Confirmed |

---

## Related documents

- [About the school](about-school.md)
- [Public homepage](public-homepage.md)
- [Public site content](public-site-content.md)
