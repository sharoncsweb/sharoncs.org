# Tuition, discounts & refunds

[← Wiki home](../README.md) · [Registration flow](registration-flow.md)

Business rules migrated from the [legacy discount & refund page](https://www.sharoncs.org/school/page/discount_and_refund). **School committee must confirm** amounts and dates for each academic year before go-live.

The registration system must **enforce or display** these rules at checkout and in admin reporting.

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

---

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-TUIT-01 | System supports **early bird** pricing by deadline. | Confirmed (legacy rules) |
| REQ-TUIT-02 | System enforces **non-combined** discounts unless school changes rule. | Confirmed (legacy) |
| REQ-TUIT-03 | Excluded courses configured per year. | Confirmed |
| REQ-TUIT-04 | Late registration proration rules configurable. | Confirmed |
| REQ-TUIT-05 | Refund schedule configurable by week of withdrawal. | Confirmed |
| REQ-TUIT-06 | Public **tuition & policy** page linked from registration. | Confirmed |

---

## Related documents

- [Registration & payment](registration-payment.md)
- [Registration flow](registration-flow.md)
- [Public site content](public-site-content.md)
