# Roles & permissions (RBAC)

[← Wiki home](../README.md)

## Diagrams

### 🎭 学校里的角色（像徽章）

```mermaid
flowchart TB
  subgraph roles["角色 Roles"]
    PA["👨‍👩‍👧 Parent 家长"]
    ST["👦👧 Student 学生"]
    TE["👩‍🏫 Teacher 老师"]
    TA["🧑‍🎓 TA 助教"]
    VO["🙋 Volunteer 志愿者"]
    AD["📋 Admin 管理员"]
  end
```

### 🧑‍🎓 TA 魔法：一班当老师，另一班当学生

```mermaid
flowchart LR
  U["同一个人"] --> A["在 A 班\n👩‍🏫 老师权限"]
  U --> B["在 B 班\n🎒 学生权限"]
```

### 👨‍👩‍🏫 一个人两个角色

```mermaid
flowchart TB
  LOGIN["🔐 一次登录"] --> P["家长门户"]
  LOGIN --> T["老师门户"]
  NOTE["例如：家长也是老师\n不用两个账号"] --- LOGIN
```

## Principles

| Principle | Detail |
|-----------|--------|
| Permission-based | Every feature maps to granular **permissions** |
| Role assignment | Permissions granted via **roles** and/or **per-user** overrides |
| Multiple roles | One user may hold several roles at once |
| Custom roles | Admins can define new roles and permission sets |

## Default roles

| Role | Typical user | Notes |
|------|--------------|-------|
| **Parent** | Guardian on account | [Parent portal](parent-portal.md): family, enrollment, payments (primary owner), student oversight |
| **Student** | Enrolled child | Own schedule, courses, submissions |
| **Teacher** | Instructor | Course content, grading, class announcements |
| **Staff** | Teachers, TAs, volunteers | School-wide ops, duties, some announcements |
| **Admin** | School administrators | Full configuration and oversight |

## Special cases

### Teaching Assistant (TA)

- In **assigned class**: same privileges as **teacher**
- In **other classes** where enrolled as student: **student** privileges only
- System must resolve context **per course**, not globally per login

### Combined roles

Examples that must work without separate logins:

- Parent + Teacher
- Student + TA

### Volunteers

- May post school-wide content when granted staff announcement permissions
- May appear on **duty schedules** with reminders (see [Admin portal](admin-portal.md))

## Permission examples

| Permission | Parent | Student | Teacher | Admin |
|------------|--------|---------|---------|-------|
| Manage users on account | Primary only | — | — | Yes |
| Create/edit courses | — | — | Own | Yes |
| Assign homework | — | — | Yes | Yes |
| Grade assignments | — | — | Yes | Yes |
| Post school-wide announcement | — | — | — | Yes |
| Post class announcement | — | — | Yes | — |
| Manage master schedule | — | — | Limited | Yes |
| Access payment data | Primary | — | — | Yes |

*Exact matrix to be finalized during implementation.*

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-RBAC-01 | All features controlled via permissions. | Confirmed |
| REQ-RBAC-02 | Permissions assignable to roles and individuals. | Confirmed |
| REQ-RBAC-03 | Users may have multiple simultaneous roles. | Confirmed |
| REQ-RBAC-04 | Admins can create custom roles. | Confirmed |
| REQ-RBAC-05 | TA permissions are **course-scoped**. | Confirmed |
| REQ-RBAC-06 | Students restricted to own data. | Confirmed |

## Related documents

- [Accounts & enrollment](accounts.md)
- [Glossary](glossary.md)
