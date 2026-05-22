# Public site content (beyond homepage)

[← Wiki home](../README.md)

Pages and features visitors expect from [www.sharoncs.org](https://www.sharoncs.org/) that are **not** only the homepage or LMS login.

---

## Public site map

| Page / feature | Wiki spec | Legacy reference | Priority |
|----------------|-----------|------------------|----------|
| Homepage | [public-homepage.md](public-homepage.md) | `/` | **P0 — Phase 1** |
| About + mission | [about-school.md](about-school.md) | `about_our_school` | **P0 — Phase 1** |
| Contact | [contact-and-calendar.md](contact-and-calendar.md) | `contact_us` | **P0 — Phase 1** |
| Course catalog (browse) | Below | `/course` | P0 |
| Registration | [registration-flow.md](registration-flow.md) | `/register` | P0 |
| Tuition, discounts, refunds | [tuition-policies.md](tuition-policies.md) | `discount_and_refund` | P0 |
| School calendar | [contact-and-calendar.md](contact-and-calendar.md) | `school_calendar` | P1 |
| Registration instructions | Link from catalog + registration | `registration_instructions` (Google Doc) | P1 |
| News / articles | Homepage + optional News section | `/news/*` | P1 |
| Gallery | Optional phase | `/gallery` | P2 |
| Resources library | Optional phase | `/resource` | P2 |
| Teaching showcase | Optional phase | `teaching_*` | P2 |
| Behavior guidelines | Static pages | `*_behavior_guideline` | P2 |
| TA application | Static / form | `ta_application` | P2 |
| Donations | Static page | `donation` | P2 |
| Youth programs | [about-school.md](about-school.md) | `about_youth`, `youth_activity` | P2 |

**P0** = needed for a professional nonprofit school launch. **P1** = soon after. **P2** = migrate when ready.

---

## Public course catalog

Legacy site lets visitors **browse courses before registering** (semester, name EN/CN, tuition, class days).

| Requirement | Detail |
|-------------|--------|
| REQ-CAT-01 | **Anonymous users** can view current semester **course list** with fees and schedule summary. | Confirmed |
| REQ-CAT-02 | Each course links to **Register** or sign-in to enroll. | Confirmed |
| REQ-CAT-03 | Catalog shows **early bird vs regular** price when applicable. | Confirmed |
| REQ-CAT-04 | Link to [tuition policies](tuition-policies.md) from catalog and checkout. | Confirmed |

Filters (legacy): class day, course type — preserve if still used by school.

---

## News vs announcements

| Type | Use | Channel |
|------|-----|---------|
| **Announcement** | Short, timely | Homepage + optional list |
| **News / article** | Longer story, photos | News section or merged into Events |

Recommendation: use **Events** for dated activities and **Announcements** for short notices; add **News** only if school still needs article-length posts.

---

## Donations {#donations}

Nonprofit **donation** page (legacy `/school/page/donation`):

- Mission-aligned giving message  
- How to donate (check, online link — TBD)  
- Tax deductibility statement **only if** school provides approved legal text  

---

## Conduct & guidelines (static)

Migrate as readable public pages (CMS or markdown), no special LMS logic in v1:

- Parent behavior guideline  
- Student behavior guideline  
- Teacher behavior guideline  
- Classroom usage guideline  

---

## Professional standards (all public pages)

| Standard | Application |
|----------|-------------|
| **Clarity** | Plain English for vendors and families; Chinese where school chooses |
| **Trust** | Mission, nonprofit, leadership, policies visible |
| **Consistency** | One address story, one phone, one email |
| **Accessibility** | Readable fonts, contrast, mobile layout |
| **CTA** | Register and Contact reachable within two clicks from homepage |

---

## Related documents

- [Legacy content migration](legacy-content-migration.md)
- [About the school](about-school.md)
- [Public homepage](public-homepage.md)
