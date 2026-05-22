# Legacy content migration

[← Wiki home](../README.md)

Checklist for moving content from [www.sharoncs.org](https://www.sharoncs.org/) to the new platform without losing trust, policies, or history.

**Owner:** School committee + The Web Design LLC.  
**Target specs:** [public-site-content.md](public-site-content.md), [about-school.md](about-school.md).

---

## Migration status

| Content | Legacy | New home | Status |
|---------|--------|----------|--------|
| Mission & history | `about_our_school` | [about-school.md](about-school.md) | Spec ready |
| Homepage announcements | Home carousel | [public-homepage.md](public-homepage.md) | Spec ready |
| Events / news | News, announcements | Homepage events + News (TBD) | Partial |
| Course catalog | `/course` | Public catalog + LMS | Spec ready |
| Register / pay | `/register` | [registration-flow.md](registration-flow.md) | Spec ready |
| Discounts & refunds | `discount_and_refund` | [tuition-policies.md](tuition-policies.md) | Spec ready |
| Registration how-to | Google Doc link | Registration flow + policy page | Replace Doc |
| Contact | `contact_us` | [contact-and-calendar.md](contact-and-calendar.md) | Spec ready |
| School calendar | `school_calendar` | [contact-and-calendar.md](contact-and-calendar.md) | Spec ready |
| Board / admin team | `board_*`, `administration_team` | About subpages | Spec ready |
| PTO | `pto` | About / community | P2 |
| Gallery | `/gallery` | Optional public | P2 |
| Resources | `/resource` | Optional / LMS | P2 |
| Teaching activity | `teaching_*` | Optional public | P2 |
| Behavior guidelines | `*_guideline` | Static public pages | P2 |
| Donation | `donation` | [public-site-content.md](public-site-content.md) | P2 |
| Youth club | `about_youth` | [about-school.md](about-school.md) | P2 |

---

## Content to verify with school

- [ ] Official **mailing** vs **class** address  
- [ ] Mission and history text (EN + CN) for 2025–2026  
- [ ] Nonprofit legal wording  
- [ ] Current discount amounts and early-bird deadlines  
- [ ] Payment gateway (Stripe/Square) vs legacy PayPal copy  
- [ ] Bilingual public site: EN only, CN only, or toggle  

---

## Do not migrate as-is

| Legacy issue | Action |
|--------------|--------|
| Cluttered homepage layout | Redesign per [public-homepage.md](public-homepage.md) |
| External-only registration doc | Integrate into site + [registration-flow.md](registration-flow.md) |
| Copyright © 2021 footer | Update year and school name |
| Duplicate announcement + news lists | Consolidate model |

---

## Related documents

- [Public site content](public-site-content.md)
- [About the school](about-school.md)
