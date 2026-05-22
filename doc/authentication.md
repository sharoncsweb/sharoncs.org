# Authentication

[← Wiki home](../README.md)

## Diagrams

### 🔐 多种登录方式（选你方便的）

```mermaid
flowchart TB
  YOU["😊 用户"] --> PH["📱 手机+短信码\nPhase 1 主力"]
  YOU --> UN["👤 用户名+密码"]
  YOU --> G["Google"]
  YOU --> MS["Microsoft"]
  YOU --> FB["Facebook/Instagram"]
  style PH fill:#fff3cd
```

### 📱 注册时短信验证

```mermaid
sequenceDiagram
  participant 家长 as 👨‍👩‍👧
  participant 系统 as 🖥️
  家长->>系统: 输入手机号
  系统->>家长: 📲 发验证码
  家长->>系统: 输入验证码 ✅
  系统->>家长: 设置密码 · 继续填资料
```

### 🔗 账号可以绑在一起

```mermaid
flowchart LR
  ONE["😊 一个用户"] --> M1["📱 手机"]
  ONE --> M2["Google"]
  ONE --> M3["用户名"]
  NOTE["任意一种都能登录\n像钥匙串"] --- ONE
```

## Supported login methods

**Phase 1 (registration):** mobile number + **verification code (SMS OTP)** + password; optional **username** as login name. See [Registration — user fields](registration-user-fields.md).

| Method | Status |
|--------|--------|
| Mobile + SMS OTP | Confirmed (phase 1) |
| Username / password | Confirmed |
| Google | Confirmed |
| Microsoft | Confirmed |
| Facebook / Instagram | Confirmed |
| Phone (SMS OTP) | Confirmed |

## Account linking

- One **user** may link **multiple** login methods
- User may sign in with **any** linked method
- Linking and unlinking should be available in account settings (with safeguards)

## Security requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-AUTH-01 | Passwords stored using secure hashing. | Confirmed |
| REQ-AUTH-02 | Rate limiting on auth endpoints. | Confirmed |
| REQ-AUTH-03 | Secure session management. | Confirmed |
| REQ-AUTH-04 | Architecture supports **MFA** in the future. | Future |
| REQ-AUTH-05 | Admins can enable/disable login methods globally. | Confirmed |
| REQ-AUTH-06 | Admins can reset credentials and assist recovery. | Confirmed |

## Admin controls

- Toggle OAuth / SMS providers per school policy
- Force password reset
- Audit log of admin recovery actions (recommended)

## Student vs parent login

Clarify with school whether young students receive their own credentials or access via parent proxy.

## Related documents

- [Accounts & enrollment](accounts.md)
- [RBAC](rbac.md)
