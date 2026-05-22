# Announcements & activity feed

[← Wiki home](../README.md)

## Diagrams

### 📢 谁能发什么公告

```mermaid
flowchart TB
  SW["📣 全校公告\nSnow day · 报名开放"]
  CL["📋 班级公告\n本周作业提醒"]
  AD["📋 Admin"] --> SW
  ST["🙋 Staff/志愿者"] --> SW
  TE["👩‍🏫 Teacher/TA"] --> CL
```

### 👀 谁看到什么（气泡）

```mermaid
flowchart TB
  subgraph all["🏫 全校 Everyone"]
    N1["放假通知"]
  end
  subgraph class["📖 仅本班 Class A"]
    N2["带拼音的作业 😊"]
  end
  P["👨‍👩‍👧 家长"] --> all
  P --> class
  S["👦 学生"] --> class
```

### 📱 信息怎么传到家庭

```mermaid
flowchart LR
  POST["📢 老师发帖"] --> FEED["📰 活动流 Feed"]
  FEED --> PAR["👨‍👩‍👧 家长门户"]
  FEED --> STU["👦 学生门户"]
  FEED -.->|"以后?"| WX["微信 WeChat"]
```

## Overview

The platform provides an **activity feed** and **announcements** with role-based posting and visibility scopes.

## Who can post

| Role | Scope |
|------|--------|
| **Admin** | School-wide |
| **Staff** (incl. certain volunteers) | School-wide |
| **Teachers** | Their class(es) |
| **TAs** | Class(es) where they assist |

Parent volunteers helping with **advertising** or school communications may receive staff-level announcement permissions.

## Visibility levels

| Level | Status | Example |
|-------|--------|---------|
| **School-wide** | Confirmed | Registration opens, holiday closure |
| **Class-specific** | Confirmed | Field trip reminder for Class A |
| **Grade-level** | Future | All Grade 2 Chinese families |

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-ANN-01 | Admin and staff can create **school-wide** announcements. | Confirmed |
| REQ-ANN-02 | Teachers and TAs can create **class-level** announcements. | Confirmed |
| REQ-ANN-03 | Feed respects visibility so users only see relevant posts. | Confirmed |
| REQ-ANN-04 | Grade-level targeting may be added later. | Future |

## Public website overlap

Legacy site sections (*Announcement*, *News*) should migrate into this model or dedicated CMS pages on the new public site. Coordinate content strategy with [Overview](overview.md).

## Related documents

- [RBAC](rbac.md)
- [Teacher portal](teacher-portal.md)
- [Admin portal](admin-portal.md)
