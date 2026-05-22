# School structure

[← Wiki home](../README.md)

## Diagrams

### 🌳 年级 → 多个班

```mermaid
flowchart TB
  G["📚 二年级中文\nGrade 2 Chinese"]
  G --> A["🅰️ 甲班 Class A\n周六 9:00 · 李老师"]
  G --> B["🅱️ 乙班 Class B\n周六 11:00 · 王老师"]
  A --> S1["👦 学生..."]
  B --> S2["👧 学生..."]
```

### 🎒 一个学生选哪一班

```mermaid
flowchart LR
  STU["👧 小美"] --> PICK["选 Class A 或 B"]
  PICK --> ROSTER["📋 进班级名单"]
  ROSTER --> SCHED["📅 她的课表"]
```

### 🏫 和平时上的学校不同

```mermaid
flowchart LR
  REG["🏫 平时学校\nCurrent regular school"] --> GR["几年级"]
  GR --> HINT["💡 帮助选\n中文班级别"]
  HINT --> CN["📚 莎伦中文课"]
```

## Hierarchy

Sharon Chinese School organizes instruction roughly as:

```
Grade (e.g. Grade 2 Chinese)
 └── Class A  (time, teacher, room, roster)
 └── Class B  (different time/teacher possible)
      └── Students (enrolled per class)
```

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-SCH-01 | A **grade** can have **multiple classes** (sections). | Confirmed |
| REQ-SCH-02 | Classes under the same grade may differ in **time**, **teacher**, and **room**. | Confirmed |
| REQ-SCH-03 | Example: *Grade 2 Chinese* → *Class A* and *Class B*. | Confirmed |
| REQ-SCH-04 | Students enroll in specific **class offerings**, not only a grade label. | Implied |

## Example

| Grade | Class | Schedule | Teacher | Room |
|-------|-------|----------|---------|------|
| Grade 2 Chinese | A | Sat 9:00 | Ms. Li | Room 101 |
| Grade 2 Chinese | B | Sat 11:00 | Mr. Wang | Room 102 |

## Roster rules

- Student belongs to one **account** (family)
- Student may be enrolled in one or more **courses/classes** per semester/year
- Class roster drives teacher gradebook and announcements

## Announcement targeting

| Level | Example | Who posts (see [Announcements](announcements.md)) |
|-------|---------|--------------------------------------------------|
| School-wide | Snow day, registration open | Admin, staff |
| Class-specific | Homework due Friday | Teacher, TA |
| Grade-level | Optional future | TBD |

## Related documents

- [Courses & learning](courses.md)
- [Registration & payment](registration-payment.md)
