# Authentication

[← Wiki home](../README.md) · [Registration flow](registration-flow.md)

## Summary

Users sign in with **one of four supported methods**. A single account may **link** multiple methods after the first signup. All methods resolve to the same **user** record; family and student records attach through [Accounts](accounts.md) and [RBAC](rbac.md).

---

## Supported login methods

| # | Method | How it works | Detailed behavior | Edge cases | Status |
|---|--------|--------------|-------------------|------------|--------|
| 1 | **Google OAuth** | Sign in with Google account | OAuth redirect; store provider subject id; map email when scope allows. | Email already on another user → linking flow or support. | Confirmed |
| 2 | **Microsoft OAuth** | Sign in with Microsoft account | Same pattern as Google with Microsoft identity platform. | School tenant restrictions may limit to org accounts if configured later. | Confirmed |
| 3 | **Email + password** | Email address and password (secure hashing) | Registration may require verified email before full portal access. | Forgot password resets via email link; rate limited. | Confirmed |
| 4 | **Phone + SMS** | Mobile number and one-time verification code (OTP) | OTP sent on login and signup; password may be set after first OTP success. | VoIP numbers may be blocked per fraud policy; international format normalized. | Confirmed |

*Not in scope unless the school adds later:* Facebook, Instagram, username-only login.

### Sign-in screen (UX)

- Show all four options clearly (buttons for Google / Microsoft; forms for email or phone).
- Same user record whether they registered with phone, email, or OAuth.
- After OAuth first sign-in, prompt to complete profile if email/phone not yet on file.
- Disabled methods (admin toggle) hide controls and show short explanation.

### Registration vs login

| Path | Typical use | Detailed behavior | Acceptance criteria |
|------|-------------|-------------------|---------------------|
| **Phone + SMS** | Enter mobile → receive OTP → set password and profile | See [user fields](registration-user-fields.md); Family Identifier assigned at account creation. | OTP expires; invalid code shows retry without revealing whether number exists. | Confirmed flow in QA script |
| **Email + password** | Enter email → verify email (recommended) → set password and profile | Verification link single-use; unverified users may have read-only limits. | Verified user can complete enrollment checkout. | Confirmed |
| **Google / Microsoft** | OAuth → accept scopes → complete or link profile | Minimal scopes; store refresh tokens only if needed for future features. | Returning OAuth user lands on last portal context or role picker. | Confirmed |

**Workflow — first-time phone signup**

1. User enters E.164 phone number.
2. System sends OTP if method enabled and rate limit OK.
3. User enters OTP; system creates or links user.
4. User completes Self profile and account shell.
5. User may add password optional for backup login per policy.

---

## Account linking

- One **user** may link **multiple** login methods (e.g. Google + email + phone).
- User may sign in with **any** linked method.
- Linking and unlinking in account settings, with safeguards (e.g. cannot remove last method without adding another).
- Linking requires re-authentication or OTP on sensitive changes to prevent session hijack linking.

| Edge case | Behavior |
|-----------|----------|
| OAuth email matches existing email/password user | Offer merge with proof (login to both) or support ticket. |
| Phone number recycled by carrier | Old links invalidated after verification failure policy. |
| Admin disables method globally | Existing links may remain but new sign-ins via that method blocked. |

---

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Login methods

![Login methods](assets/diagrams/auth-methods.svg)

### SMS verification at signup

![SMS verification at signup](assets/diagrams/auth-sms.svg)

### Link multiple login methods

![Link multiple login methods](assets/diagrams/auth-linking.svg)


## Security requirements

| ID | Requirement | Detailed behavior | Edge cases | Acceptance criteria | Status |
|----|-------------|-------------------|------------|---------------------|--------|
| REQ-AUTH-01 | Support **Google OAuth**, **Microsoft OAuth**, **email + password**, and **phone + SMS**. | Each method independently enableable; unified session after success. | Method disabled mid-session does not log user out until expiry. | All four methods pass happy-path E2E when enabled. | Confirmed |
| REQ-AUTH-02 | Passwords stored using secure hashing (email/password path). | Modern slow hash + per-user salt; never store plaintext. | Password reset invalidates old sessions optionally. | Hash algorithm meets current OWASP recommendation at ship time. | Confirmed |
| REQ-AUTH-03 | SMS OTP rate-limited; codes expire quickly. | Per-phone and per-IP limits; 5–10 minute TTL typical. | Brute force lockout with admin unlock path. | 6th rapid OTP request blocked; expired code rejected. | Confirmed |
| REQ-AUTH-04 | Rate limiting on all auth endpoints. | Login, OTP, reset, OAuth callbacks included. | Shared NAT users may hit IP limit; captcha fallback TBD. | Load test shows 429 under abuse pattern. | Confirmed |
| REQ-AUTH-05 | Secure session management. | HttpOnly cookies or equivalent; rotation on privilege change. | Concurrent sessions allowed unless school disables. | Session invalid after logout on all devices if “logout everywhere” chosen. | Confirmed |
| REQ-AUTH-06 | Architecture supports **MFA** in the future. | Data model reserves MFA factors without breaking v1 users. | — | Design doc shows extension point without migration break. | Future |
| REQ-AUTH-07 | Admins can enable/disable login methods globally. | Settings page toggles; effective immediately for new attempts. | At least one method must stay enabled. | Disabling SMS hides phone login on public sign-in. | Confirmed |
| REQ-AUTH-08 | Admins can reset credentials and assist recovery. | Force password reset; unlink stuck OAuth with audit. | Admin cannot see password plaintext. | Audit log entry for each admin recovery action. | Confirmed |
| REQ-AUTH-09 | OAuth tokens handled per provider best practices; minimal scopes. | Store only needed ids; refresh tokens encrypted at rest. | Token revocation on unlink. | Security review checklist signed for OAuth storage. | Confirmed |

---

## Admin controls

- Enable/disable each method: Google, Microsoft, email/password, phone/SMS.
- Force password reset (email/password users).
- Audit log for admin recovery actions (recommended).
- Optional: session list and revoke for compromised accounts (recommended).

**Workflow — admin disables a login method**

1. Admin opens **Settings → Authentication**.
2. Admin toggles method off; system validates at least one method remains.
3. New sign-in attempts using disabled method show policy message.
4. Existing linked identities remain for re-enable unless admin purges links.

---

## Student vs parent login

Clarify with school whether young students use the same four methods or access via parent only. If students lack login, parents are the authentication path for all LMS visibility; student accounts created later should link to existing student profile without duplicate enrollment.

| Policy option | Implication |
|---------------|-------------|
| Student login allowed | Same four methods; age-appropriate UX; parental oversight via parent portal. |
| Parent-only access | Student portal hidden or read-only proxy; REQ-STU flows via parent. |

---

## Related documents

- [Registration — user fields](registration-user-fields.md)
- [Accounts & enrollment](accounts.md)
- [RBAC](rbac.md)
