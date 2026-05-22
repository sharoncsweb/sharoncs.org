# Platform structure

[← Wiki home](../README.md)

## Diagrams

### 🏠 One school, one home

```mermaid
flowchart TB
  WORLD["🌎 互联网 Internet"] --> SITE["🏫 莎伦中文学校\n只有这一所学校"]
  SITE --> PUB["📰 公开网页\n招生 · 公告"]
  SITE --> APP["🔐 登录后平台\n家长 · 学生 · 老师"]
  style SITE fill:#d4edda
```

### 🧩 What lives on the platform

```mermaid
flowchart LR
  subgraph platform["平台 Platform"]
    R["📝 注册缴费\n家长做主"]
    L["📚 上课支持\n作业 · 材料"]
    N["📢 通知公告"]
  end
  R --- L --- N
```

### 💰 钱怎么收（不是月费会员）

```mermaid
flowchart LR
  FREE["🆓 用平台\n不收月费"] --> PAY["💳 家长付\n所选课程学费"]
  PAY --> SCHOOL["🏫 学校收到\nStripe / Square"]
```

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-PLAT-01 | Platform is built for **Sharon Chinese School only** (single tenant). | Confirmed |
| REQ-PLAT-02 | Platform is **not** sold as SaaS to multiple schools in v1. | Confirmed |
| REQ-PLAT-03 | No subscription fee to **access** the platform. | Confirmed |
| REQ-PLAT-04 | Parents **pay for selected courses** during registration (tuition/fees), not platform access. | Confirmed |

## Model

```
┌─────────────────────────────────────────────────────────┐
│              Sharon Chinese School (tenant)              │
├─────────────────────────────────────────────────────────┤
│  Public site          │  Authenticated LMS + portals   │
│  (marketing, info)    │  Parent / Student / Teacher /  │
│                       │  Staff / Admin portals         │
├───────────────────────┴─────────────────────────────────┤
│  Registration & payments │  Schedules │  Courses       │
└─────────────────────────────────────────────────────────┘
```

## Responsibilities split

| Concern | Owner in platform |
|---------|-------------------|
| Family accounts, students, enrollment | Platform |
| Tuition / class payments | Platform (Stripe, Square, or similar) |
| Yearly course catalog & master schedule | Admin |
| Day-to-day class content & grading | Teachers (Google Classroom–like UX) |
| School-wide news & announcements | Admin & staff |
| Class-level announcements | Teachers & TAs |

## Optional future: hybrid delivery

Courses may support a `delivery_mode` field:

| Mode | Platform handles | External (e.g. Google Classroom) |
|------|------------------|----------------------------------|
| `internal` | Full LMS | — |
| `google_classroom` | Registration, accounts, scheduling, announcements | Assignments, materials, grading (TBD) |
| `hybrid` | Mix | Mix |

*v1 target: primarily `internal` with in-person instruction.*

## Related documents

- [Overview](overview.md)
- [Registration & payment](registration-payment.md)
- [Courses & learning](courses.md)
