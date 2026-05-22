# Teacher portal

[← Wiki home](../README.md)

## Diagrams

### 👩‍🏫 老师工作台

```mermaid
flowchart TB
  T["👩‍🏫 老师 Teacher Portal"]
  T --> LIST["📋 我的班级"]
  T --> POST["📢 发班级公告"]
  T --> HW["📝 布置作业/考试"]
  T --> GRADE["✅ 批改上传"]
  style T fill:#e8f5e9
```

### 📝 批改作业（像判卷子）

```mermaid
sequenceDiagram
  participant 师 as 👩‍🏫 老师
  participant 生 as 👦 学生
  师->>生: 发布作业 + 附件
  生->>师: 上传 PDF/照片
  师->>生: 分数 + 评语 ⭐
```

### 🎭 助教 TA：两顶帽子

```mermaid
flowchart TB
  TA["🧑‍🎓 张同学\n也是 TA"]
  TA --> C1["班级 A\n👩‍🏫 像老师"]
  TA --> C2["班级 B\n🎒 像学生"]
  style C1 fill:#fff3cd
  style C2 fill:#dfe6ff
```

## Audience

**Teachers** and **TAs** (in classes where they act as teacher).

## Primary features

### My courses

- List of assigned courses for the current school year
- Quick access to each course’s content and roster

### Course content management

- Create and organize modules/lessons (flexible, Google Classroom–style)
- Upload videos, PDFs, notes
- Publish or hide items for students
- Post **class-level** announcements (with TA where permitted)

### Assignments & exams

| Capability | Detail |
|------------|--------|
| Create work | Assignments and exams with **attachments** |
| Differentiation | Assign **different work to different students** in the same class |
| Submissions | Students upload **PDF or photos** of completed work |
| Grading | Score, feedback, return to student |

### Schedule operations

- View master timetable for assigned courses
- **Reschedule a single class** (with admin alignment on policy)
- Request or record **substitute teacher** for a session

## Requirements

| ID | Requirement | Status |
|----|-------------|--------|
| REQ-TCH-01 | Teachers create assignments and exams with attachments. | Confirmed |
| REQ-TCH-02 | Teachers grade PDF/image submissions with feedback. | Confirmed |
| REQ-TCH-03 | Teachers can target assignments to subsets of students. | Confirmed |
| REQ-TCH-04 | Teachers control student-visible content on course pages. | Confirmed |
| REQ-TCH-05 | Teachers and TAs may post **class-level** announcements. | Confirmed |
| REQ-TCH-06 | Teachers can reschedule individual sessions (with admin). | Confirmed |
| REQ-TCH-07 | Teachers can assign substitute for a single session. | Confirmed |

## TA note

A user who is **TA** in Course A has teacher-level tools in Course A only. In courses where they are enrolled as a **student**, they see the [student portal](student-portal.md) only.

See [RBAC](rbac.md).

## Related documents

- [Courses & learning](courses.md)
- [Admin portal](admin-portal.md)
- [Announcements](announcements.md)
