# Tuition, discounts & refunds

[← Wiki home](../README.md) · [Registration flow](registration-flow.md)

Business rules migrated from the [legacy discount & refund page](https://www.sharoncs.org/school/page/discount_and_refund). **School committee must confirm** amounts and dates for each academic year before go-live.

The registration system must **enforce or display** these rules at checkout and in admin reporting.

## Backend configuration

| Frontend (dynamic) | Configure in admin |
|--------------------|-------------------|
| Catalog & cart **prices** | **Admin → Academic year → Courses → Pricing** |
| Early bird, sibling, multi-class, exclusions | **Admin → Pricing → Discount rules** |
| Late-registration tiers | **Admin → Pricing → Tuition rules** |
| Policy text on public tuition page | **Admin → Content → Pages → Tuition** |

Full map: **[Frontend ↔ backend configuration map](frontend-backend-config.md#registration--checkout)**.

---

## Discounts

### Early registration

| Rule | Detail |
|------|--------|
| Amount | **$15 off per course** |
| Application | Automatic when registered by the **early registration deadline**; regular price after |
| Stacking | Applied before other discounts where applicable |

### Other discounts (based on regular price)

Eligible discounts are typically **refunded within the 6th week of school** when applicable (legacy policy — confirm automation vs manual).

| Discount | Amount (legacy) |
|----------|-----------------|
| **Three or more youth courses** per student (per year) | $30 off per school year / $15 off per semester for course 3+ |
| **Teacher’s child** | $30 off per course per year / $15 per semester |
| **Military** | $30 off per course per year / $15 per semester |

**Important:** Legacy states **discounts cannot be combined**. System must apply **one** qualifying discount per course or follow school’s updated stacking rules.

### Courses excluded from discounts

Do not apply discounts to (legacy list — confirm annually):

- The Art of Recitation  
- LEGO Robotic League / Programming  
- College Application Essay Workshop  

---

## Late registration tuition

| Registration timing (full-year courses) | Tuition charged |
|----------------------------------------|-----------------|
| Before end of week 3 | Full tuition |
| Before end of week 10 | **⅔** tuition |
| After week 20 | **⅓** tuition |
| Partial-semester courses | Admin team sets tuition |

---

## Refunds (cancellation / withdrawal)

| Withdrawal timing | Refund |
|-------------------|--------|
| Before Saturday of **2nd class** | **100%** |
| Before Saturday of **3rd class** | **90%** after **$20** processing fee |
| Before Saturday of **4th class** | **80%** after **$20** processing fee |
| After Saturday of **4th class** | **No refund** |

| Item | Policy |
|------|--------|
| Registration fee | **Non-refundable** |
| Payment processor fee | Legacy: PayPal **2.5%** non-refundable — map to Stripe/Square fees in new system |
| Refund processing | ~**two weeks** for checks (legacy); define for card refunds |

---

## Other enrollment policies

| Policy | Detail |
|--------|--------|
| Class changes | No switching after **3rd class** without principal approval |
| Minimum enrollment | Class may be **cancelled or combined** if fewer than **6** students |
| Teacher assignment | School may substitute teacher if needed; **no refund** for teacher change |
| System changes | School reserves right to adjust registration rules with notice |

---

## Public visibility

| Surface | Requirement |
|---------|-------------|
| **Registration checkout** | Show applied discounts and final price |
| **Public policy page** | Full text (or summary + PDF) linked from course catalog and registration |
| **Parent portal** | Payment history and refund status |

### Workflow — parent sees policy at checkout

1. Parent adds classes to cart; system loads active tuition and discount rules from admin.
2. Review screen lists each line: base price, early bird adjustment, one policy discount if eligible, exclusions noted.
3. Parent opens linked tuition policy page for full legal text before paying.
4. After payment, refund requests follow school office process; portal shows status when admin updates.

### Workflow — admin configures season rules

1. Admin sets early-bird deadline and per-course prices in **Courses → Pricing**.
2. Configures discount rules, excluded courses, late tiers, and refund schedule in **Pricing**.
3. Updates public tuition page copy in **Content → Pages → Tuition** to match engine behavior.
4. Runs test carts for early bird, sibling, multi-class, excluded course, and late registration scenarios.

### Acceptance criteria

- Early bird applies automatically before configured deadline (REQ-TUIT-01).
- Checkout applies at most one policy discount per course unless school changes stacking (REQ-TUIT-02).
- Excluded courses never receive policy discounts (REQ-TUIT-03).
- Late registration charges prorated tuition per configured week bands (REQ-TUIT-04).
- Refund amounts follow week-of-withdrawal table after admin processes withdrawal (REQ-TUIT-05).
- Public tuition page is linked from catalog and registration and matches enforced rules (REQ-TUIT-06).

### Edge cases

- **Register day before vs after early-bird deadline** — price changes at deadline boundary in server timezone (confirm with school).
- **Three youth courses — multi-class vs teacher-child** — legacy: no combining; system picks single best discount or school-defined priority.
- **Withdrawal Saturday boundary** — refund tier uses “before Saturday of Nth class” per legacy wording; define class session calendar in admin.
- **Registration fee non-refundable** — shown on checkout even if 100% course refund applies.
- **Processor fee on partial refund** — card fee portion may be non-refundable; disclose on policy page.
- **Class cancelled by school for low enrollment** — full refund path per office policy (automate TBD).

---

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-TUIT-01 | System supports **early bird** pricing by deadline. | Confirmed |
| REQ-TUIT-02 | System enforces **non-combined** discounts unless school changes rule. | Confirmed |
| REQ-TUIT-03 | Excluded courses configured per year. | Confirmed |
| REQ-TUIT-04 | Late registration proration rules configurable. | Confirmed |
| REQ-TUIT-05 | Refund schedule configurable by week of withdrawal. | Confirmed |
| REQ-TUIT-06 | Public **tuition & policy** page linked from registration. | Confirmed |

---

## Related documents

- [Registration & payment](registration-payment.md)
- [Registration flow](registration-flow.md)
- [Public site content](public-site-content.md)
