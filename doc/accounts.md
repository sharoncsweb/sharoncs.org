# Accounts & enrollment

[← Wiki home](../README.md)

The platform separates **Account** (family/billing), **User** (login identity), and **Student** (child learner). Registration, payments, and portals all depend on this model—implementers should not collapse students into parent user records.

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### One family account

![One family account](assets/diagrams/accounts-family.svg)

### Family relationships

![Family relationships](assets/diagrams/accounts-relationships.svg)

### Registration flow

![Registration flow](assets/diagrams/accounts-registration-flow.svg)


## Core concepts

Three entities must remain distinct:

### Account

- Represents a **family unit** and **billing entity**
- Must have exactly one **primary owner** (parent)
- May include multiple **users** (parents/guardians) and multiple **students**
- Receives **Family Identifier** at creation (system-generated, stable)

**Detailed behavior:**

- Primary owner is set when the first **Self** user completes registration; transfer requires admin and audit log.
- Billing address and payment methods attach at account level unless provider requires per-user—receipts show Family Identifier.
- Removing the last student does not delete the account; parents may return next year without re-creating login.

### User (parent / guardian)

- Individual **login identity**
- Primarily parents/guardians in v1
- May belong to **multiple accounts** (optional; shared guardianship edge cases)
- Manages students within accounts per permissions
- **Self** user on account creation becomes primary owner unless admin configures otherwise

**Detailed behavior:**

- Spouse may be invited or added by primary owner with email/phone; Spouse completes own credentials.
- User profile edits (nickname, WeChat, address) apply to that user only; students have separate profiles.
- Linking Google/Microsoft/email/phone to same user is supported per [Authentication](authentication.md).

### Student

- A **child** enrolled in the school
- Belongs to **exactly one account** (strict)
- Cannot exist on multiple accounts simultaneously
- May have optional login credentials (policy TBD); always visible to parents on account

**Detailed behavior:**

- Placement fields (regular school, grade) live on student profile and inform class suggestions.
- School Assigned Roles on students (e.g. TA in one class, student in another) are rare but supported via RBAC.

## Relationship diagram

```
Account (family / billing)
├── Primary owner (User) ── billing, payments, add/remove parents
├── Users[] (parents/guardians)
└── Students[] (children)

User ──optional──► many Accounts
Student ──required──► one Account
```

## Requirements

| ID | Requirement | Acceptance criteria | Status |
|----|-------------|---------------------|--------|
| REQ-ACC-01 | Parents **self-register** their own user accounts. | Public registration creates User + Account without admin; admin assist is exception path. | Confirmed |
| REQ-ACC-02 | Parents **create and manage** student profiles on their account. | Add/edit/remove student on account; required fields validated per registration doc. | Confirmed |
| REQ-ACC-03 | Administrators may **assist** with account/user/student creation when needed; this is not the primary flow. | Admin actions logged; family receives same Family Identifier model as self-service. | Confirmed |
| REQ-ACC-04 | Each account has one **primary owner** with exclusive rights to billing, payments, and adding/removing users. | Spouse cannot complete checkout unless school enables exception; UI hides payment actions for non-primary. | Confirmed |
| REQ-ACC-05 | Non-primary parents may have full access initially; **limited access** is a future option. | v1: spouse can view/manage students per parent portal table; limited mode not required for launch. | Future |

## Profile data at registration

When parents and students are created, collect the fields defined in **[Registration — user fields](registration-user-fields.md)** and [`WebSiteUserFields.xlsx`](WebSiteUserFields.xlsx):

- **Login:** Google OAuth, Microsoft OAuth, email + password, or phone + SMS
- **Identity:** nickname, English/Chinese names, gender, date of birth (students)
- **Contact:** WeChat ID, email, residential address (street, city, state, ZIP)
- **Family:** system **Family Identifier**, **Family Relationship** (Self, Spouse, Child)
- **Roles:** **School Assigned Role** (multiple allowed)
- **Placement:** current regular school name and grade (students)

**Validation edge cases:**

| Field / case | Behavior |
|--------------|----------|
| Duplicate email across users | Block or prompt to link login—do not create silent duplicate |
| Minor student DOB | Age-appropriate grade suggestions only; no public display of full DOB |
| Missing Chinese name | Allowed if school marks optional; English name required per spreadsheet |
| International address | US-style fields required for v1 unless school expands schema |

## Enrollment flow (happy path)

1. Parent registers or signs in via **Google OAuth**, **Microsoft OAuth**, **email + password**, or **phone + SMS** (see [Authentication](authentication.md)).
2. Parent completes **Self** profile; system assigns **Family Identifier** (account).
3. Parent adds **Spouse** and/or **Child** members with relationship and profile fields.
4. Parent assigns **school roles** per person where applicable (staff roles may be admin-only).
5. Parent selects classes per student and pays — see [Registration & payment](registration-payment.md).
6. Parent uses the **[Parent portal](parent-portal.md)**; students use the [Student portal](student-portal.md) when they have credentials.

### Extended workflow steps (save and resume)

| Step | User action | System behavior |
|------|-------------|-----------------|
| A | Start registration on phone | Session persists; SMS OTP verified |
| B | Save partial profile | Draft account or wizard state; return link or login continues |
| C | Add second child | Each child gets own profile; cart can include multiple students |
| D | Checkout | Only primary owner sees pay button; webhook confirms enrollment |
| E | Confirmation | Email/SMS receipt; portal shows enrolled classes per student |

## Admin-assisted enrollment

- Admin can create users, students, or fix account linkage on request
- Audit trail recommended (who created/changed what, timestamp, reason code)
- Admin can set or change primary owner with school committee approval
- Admin merge: duplicate accounts for same family combined into one Family Identifier where possible

### Admin edge cases

| Case | Process |
|------|---------|
| Parent locked out | Admin verifies identity, resets login or links OAuth |
| Wrong child on account | Admin moves student only with guardian proof; never copy student to second account |
| Refund family | Financial action in payment provider; roster updated separately |

## Account lifecycle edge cases

| Topic | Notes |
|-------|--------|
| **Student login** | Can younger students log in themselves, or only via parent? (Clarify with school.) If disabled, student portal read-only via parent session or not shown. |
| **Account merge / split** | Divorce or guardianship change — process TBD; expect admin-led split with one student per account after split |
| **Primary owner unavailable** | Spouse calls school; admin temporary payment link or owner transfer |
| **Deceased / inactive user** | Admin disables login; account students remain until admin archives |
| **Typos in legal name** | Parent edits before payment; after payment, admin correction with audit |

## Permissions matrix (v1 baseline)

| Action | Primary owner | Spouse (v1) | Student | Admin |
|--------|---------------|-------------|---------|-------|
| Pay tuition | Yes | No (default) | No | Override |
| Add/remove Spouse user | Yes | No | No | Yes |
| Add/edit student | Yes | Yes* | No | Yes |
| View grades/assignments | Yes | Yes* | Own | Yes |
| Change own profile | Yes | Yes | Yes | Yes |

\*Per parent portal; future **REQ-ACC-05** may restrict spouse to view-only.

## Mobile and accessibility

- Phone + SMS registration: large OTP input, resend cooldown labeled, errors in plain language.
- Adding multiple children: wizard does not lose prior child data on back navigation.
- Primary owner badge visible before checkout (“You are paying as primary parent”) to reduce spouse payment confusion.
- Forms: each field has visible label; required fields marked in text, not color alone.

## Open questions

| Topic | Notes |
|-------|--------|
| Student login | Can younger students log in themselves, or only via parent? (Clarify with school.) |
| Account merge / split | Divorce or guardianship change — process TBD |

## Related documents

- [Parent portal](parent-portal.md)
- [Registration — user fields](registration-user-fields.md)
- [Glossary](glossary.md)
- [RBAC](rbac.md)
- [Authentication](authentication.md)
- [Registration & payment](registration-payment.md)
- [School structure](school-structure.md)
