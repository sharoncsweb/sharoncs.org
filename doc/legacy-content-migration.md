# Legacy content migration

[← Wiki home](../README.md)

Checklist for moving content from [www.sharoncs.org](https://www.sharoncs.org/) to the new platform without losing trust, policies, or history.

**Owner:** School committee + The Web Design LLC.  
**Target specs:** [public-site-content.md](public-site-content.md), [about-school.md](about-school.md).

### Migration principles

- **Content before chrome** — migrate mission, policies, and contact first; redesign layout per new specs, do not copy legacy HTML structure.
- **One source of truth** — each legacy URL maps to exactly one new page or redirect target.
- **School approval** — committee signs off on EN copy and nonprofit wording before publish.
- **Measure by priority** — P0 for launch, P1 within weeks, P2 when committee capacity allows.

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

### Workflow — migrate one legacy page

1. Identify legacy URL and owner on the committee.
2. Copy body text into draft; remove outdated dates, PayPal-only language, and duplicate addresses.
3. Enter content in the matching admin screen (see [frontend-backend-config.md](frontend-backend-config.md)).
4. Preview on staging; compare against legacy for missing sections.
5. Publish with redirect from old path; verify footer links and homepage CTAs.

### Acceptance criteria (migration program)

- Every P0 row in the status table is live on the new site with approved copy before public launch.
- No public link points to unmigrated legacy paths except documented temporary redirects.
- Homepage announcements and events replace legacy carousel without losing urgent notices from the current season.
- Registration instructions live on-site (no external-only Google Doc as primary path).
- Tuition and refund text on the new site matches enforced checkout rules.

### Edge cases

- **Bilingual legacy paragraphs** — migrate EN for launch; add CN when school supplies approved text.
- **Broken legacy images** — re-upload assets; do not hotlink old host.
- **News vs announcement duplication** — consolidate into one model per [public site content](public-site-content.md).
- **Gallery hundreds of photos** — phase 2 batch import; homepage does not block on gallery.
- **PDF calendar only on legacy** — provide accessible HTML summary on new calendar page.

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

### Redirect checklist (cutover)

| Legacy pattern | New target | Notes |
|----------------|------------|--------|
| `/` | New homepage | 301 |
| `/school/page/about_our_school` | About | 301 |
| `/school/page/contact_us` | Contact | 301 |
| `/course` | Public catalog | 301 |
| `/register` | Registration entry | 301 |
| `/school/page/discount_and_refund` | Tuition policies | 301 |
| Unmapped P2 URLs | About or homepage | Temporary until page exists |

---

## Related documents

- [Public site content](public-site-content.md)
- [About the school](about-school.md)
