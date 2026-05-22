# Authentication

[← Wiki home](../README.md) · [Registration flow](registration-flow.md)

## Summary

Users sign in with **one of four supported methods**. A single account may **link** multiple methods after the first signup.

---

## Supported login methods

| # | Method | How it works | Status |
|---|--------|--------------|--------|
| 1 | **Google OAuth** | Sign in with Google account | Confirmed |
| 2 | **Microsoft OAuth** | Sign in with Microsoft account | Confirmed |
| 3 | **Email + password** | Email address and password (secure hashing) | Confirmed |
| 4 | **Phone + SMS** | Mobile number and one-time verification code (OTP) | Confirmed |

*Not in scope unless the school adds later:* Facebook, Instagram, username-only login.

### Sign-in screen (UX)

- Show all four options clearly (buttons for Google / Microsoft; forms for email or phone).
- Same user record whether they registered with phone, email, or OAuth.
- After OAuth first sign-in, prompt to complete profile if email/phone not yet on file.

### Registration vs login

| Path | Typical use |
|------|-------------|
| **Phone + SMS** | Enter mobile → receive OTP → set password and profile (see [user fields](registration-user-fields.md)) |
| **Email + password** | Enter email → verify email (recommended) → set password and profile |
| **Google / Microsoft** | OAuth → accept scopes → complete or link profile |

---

## Account linking

- One **user** may link **multiple** login methods (e.g. Google + email + phone).
- User may sign in with **any** linked method.
- Linking and unlinking in account settings, with safeguards (e.g. cannot remove last method without adding another).

---

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### Login methods

![Login methods](assets/diagrams/auth-methods.svg)

### Phone + SMS at signup

![SMS verification at signup](assets/diagrams/auth-sms.svg)

### Link multiple login methods

![Link multiple login methods](assets/diagrams/auth-linking.svg)

---

## Security requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-AUTH-01 | Support **Google OAuth**, **Microsoft OAuth**, **email + password**, and **phone + SMS**. | Confirmed |
| REQ-AUTH-02 | Passwords stored using secure hashing (email/password path). | Confirmed |
| REQ-AUTH-03 | SMS OTP rate-limited; codes expire quickly. | Confirmed |
| REQ-AUTH-04 | Rate limiting on all auth endpoints. | Confirmed |
| REQ-AUTH-05 | Secure session management. | Confirmed |
| REQ-AUTH-06 | Architecture supports **MFA** in the future. | Future |
| REQ-AUTH-07 | Admins can enable/disable login methods globally. | Confirmed |
| REQ-AUTH-08 | Admins can reset credentials and assist recovery. | Confirmed |
| REQ-AUTH-09 | OAuth tokens handled per provider best practices; minimal scopes. | Confirmed |

---

## Admin controls

- Enable/disable each method: Google, Microsoft, email/password, phone/SMS.
- Force password reset (email/password users).
- Audit log for admin recovery actions (recommended).

---

## Student vs parent login

Clarify with school whether young students use the same four methods or access via parent only.

---

## Related documents

- [Registration — user fields](registration-user-fields.md)
- [Accounts & enrollment](accounts.md)
- [RBAC](rbac.md)
