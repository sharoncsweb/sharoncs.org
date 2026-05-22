# Roles & permissions (RBAC)

[← Wiki home](../README.md)

## Diagrams

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

### School roles

![School roles](assets/diagrams/rbac-roles.svg)

### TA per-class permissions

![TA per-class permissions](assets/diagrams/rbac-ta-dual.svg)

### Multiple roles, one login

![Multiple roles, one login](assets/diagrams/rbac-multi-role.svg)


## Principles

| Principle | Detail | Detailed behavior |
|-----------|--------|-------------------|
| Permission-based | Every feature maps to granular **permissions** | UI menus and API endpoints check permissions, not hard-coded role names alone. |
| Role assignment | Permissions granted via **roles** and/or **per-user** overrides | Overrides win for allow/deny per school policy; audit log recommended for admin grants. |
| Multiple roles | One user may hold several roles at once | Session carries role set; portal switcher picks **context** without re-auth. |
| Custom roles | Admins can define new roles and permission sets | Custom roles clone from templates; cannot delete system roles in use. |
| Course scope | TA and substitute rights resolve **per course** | Global “teacher” flag is insufficient; enrollment + assignment tables drive scope. |

## Default roles

| Role | Typical user | Notes | Edge cases |
|------|--------------|-------|------------|
| **Parent** | Guardian on account | [Parent portal](parent-portal.md): family, enrollment, payments (primary owner), student oversight | Spouse may lack pay permission; still sees children per account policy. |
| **Student** | Enrolled child | Own schedule, courses, submissions | Cannot see sibling data on same account unless also enrolled in same class. |
| **Teacher** | Instructor | Course content, grading, class announcements | Retired teacher loses write access; historical grades read-only per retention. |
| **Staff** | Teachers, TAs, volunteers | School-wide ops, duties, some announcements | Volunteer subset may post announcements without gradebook access. |
| **Admin** | School administrators | Full configuration and oversight | Break-glass actions (impersonation, if any) must be logged. |

## Special cases

### Teaching Assistant (TA)

- In **assigned class**: same privileges as **teacher** for content, grading, and class announcements unless admin restricts
- In **other classes** where enrolled as student: **student** privileges only
- System must resolve context **per course**, not globally per login
- UI should show active course context when user is both TA and student to prevent accidental posts to wrong class

### Combined roles

Examples that must work without separate logins:

- Parent + Teacher — family dashboard plus link to teacher workspace
- Student + TA — student dashboard default; teacher tools only inside TA-assigned courses
- Parent + Volunteer — duty calendar and announcement tools per staff permissions

**Workflow — permission check**

1. Authenticate user and load role + permission sets (+ overrides).
2. Resolve resource scope (account, course, session, school).
3. Evaluate permission string against scope (e.g. `course.announcement.create` on `course_id`).
4. Deny with generic message if missing; do not leak existence of other users’ data.

### Volunteers

- May post school-wide content when granted staff announcement permissions
- May appear on **duty schedules** with reminders (see [Admin portal](admin-portal.md))
- Typically lack financial and roster export permissions unless explicitly granted

## Permission examples

| Permission | Parent | Student | Teacher | Admin | Edge cases |
|------------|--------|---------|---------|-------|------------|
| Manage users on account | Primary only | — | — | Yes | Spouse add/remove may be primary-only even if spouse can edit students. |
| Create/edit courses | — | — | Own | Yes | “Own” means assigned courses, not every course in school. |
| Assign homework | — | — | Yes | Yes | Admin assign is for support/fix, not daily pedagogy. |
| Grade assignments | — | — | Yes | Yes | Students cannot edit grades after submit; resubmit policy is teacher-controlled. |
| Post school-wide announcement | — | — | — | Yes | Staff/volunteer variant uses delegated permission. |
| Post class announcement | — | — | Yes | — | TA inherits in scoped class only. |
| Manage master schedule | — | — | Limited | Yes | Teacher “limited” = propose or edit single session per policy. |
| Access payment data | Primary | — | — | Yes | Teachers never see card data; only admin and primary parent billing views. |

*Exact matrix to be finalized during implementation; table above is the baseline product intent.*

## Requirements

| ID | Requirement | Detailed behavior | Edge cases | Acceptance criteria | Status |
|----|-------------|-------------------|------------|---------------------|--------|
| REQ-RBAC-01 | All features controlled via permissions. | No hidden admin backdoors in UI without permission; feature flags still respect RBAC. | Legacy routes disabled if permission missing. | Penetration-style check: student token cannot call teacher grade APIs. | Confirmed |
| REQ-RBAC-02 | Permissions assignable to roles and individuals. | Admin UI lists effective permissions per user; diff shows role vs override. | Removing last admin requires safeguard role. | Custom role appears in assignment dropdown; user gains new menu items without redeploy. | Confirmed |
| REQ-RBAC-03 | Users may have multiple simultaneous roles. | One session; portal switcher or unified nav; permissions union with scope rules. | Conflicting deny override on one permission blocks action even if another role allows. | Parent+teacher logs in once and reaches both portals. | Confirmed |
| REQ-RBAC-04 | Admins can create custom roles. | Clone template, toggle permission checkboxes, assign to users. | Cannot rename system role IDs in use. | New role “Front desk” can post school announcement without course edit. | Confirmed |
| REQ-RBAC-05 | TA permissions are **course-scoped**. | API includes `course_id` in authorization; TA not in roster has student-only access. | User TA in A and student in B cannot grade B. | TA in Class A can post announcement in A only. | Confirmed |
| REQ-RBAC-06 | Students restricted to own data. | Schedule, submissions, grades keyed to student profile id. | Twin students on one account remain separate principals. | Student A cannot open Student B assignment URL by ID tampering. | Confirmed |

## Related documents

- [Accounts & enrollment](accounts.md)
- [Glossary](glossary.md)
- [Authentication](authentication.md)
