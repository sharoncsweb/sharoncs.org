#!/usr/bin/env python3
"""Replace Mermaid Diagram sections with flat SVG image blocks."""
import re
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "doc"
CAST = """| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| ![Parent](assets/characters/parent.svg) | ![Student](assets/characters/student.svg) | ![Teacher](assets/characters/teacher.svg) | ![Admin](assets/characters/admin.svg) | ![School](assets/characters/school.svg) |
| Parent | Student | Teacher | Admin | School |

"""

PAGE_DIAGRAMS = {
    "overview.md": [
        ("Who we are building for", "overview-stakeholders.svg"),
        ("Build order (phase 1 first)", "overview-phases.svg"),
        ("Legacy site to new platform", "overview-legacy-new.svg"),
    ],
    "platform.md": [
        ("One school, one platform", "platform-one-school.svg"),
        ("Platform layers", "platform-layers.svg"),
        ("How tuition is collected", "platform-payment.svg"),
    ],
    "accounts.md": [
        ("One family account", "accounts-family.svg"),
        ("Family relationships", "accounts-relationships.svg"),
        ("Registration flow", "accounts-registration-flow.svg"),
    ],
    "parent-portal.md": [
        ("Parent portal hub", "parent-portal-hub.svg"),
        ("Typical parent session", "parent-portal-day.svg"),
        ("Primary parent vs spouse", "parent-primary-spouse.svg"),
    ],
    "student-portal.md": [
        ("Student dashboard", "student-dashboard.svg"),
        ("Inside a course", "student-course-page.svg"),
        ("Submit homework", "student-homework.svg"),
    ],
    "teacher-portal.md": [
        ("Teacher workspace", "teacher-workspace.svg"),
        ("Grading flow", "teacher-grading.svg"),
        ("TA has two roles", "teacher-ta-dual.svg"),
    ],
    "admin-portal.md": [
        ("Yearly course setup", "admin-year-setup.svg"),
        ("Volunteer duty reminder", "admin-volunteer.svg"),
        ("Reschedule one session", "admin-reschedule.svg"),
    ],
    "registration-user-fields.md": [
        ("Signup steps", "registration-signup-steps.svg"),
        ("Field groups", "registration-field-groups.svg"),
        ("Who fills which fields", "registration-who-fills.svg"),
    ],
    "registration-payment.md": [
        ("Enrollment and payment", "payment-cart.svg"),
        ("Discount types", "payment-discounts.svg"),
        ("Who can checkout", "payment-checkout.svg"),
    ],
    "courses.md": [
        ("Course lifecycle", "courses-lifecycle.svg"),
        ("In-person plus LMS", "courses-in-person.svg"),
        ("Course page layout", "courses-classroom-style.svg"),
    ],
    "school-structure.md": [
        ("Grade with multiple classes", "school-grade-classes.svg"),
        ("Student picks a class", "school-pick-class.svg"),
        ("Placement hints", "school-placement.svg"),
    ],
    "rbac.md": [
        ("School roles", "rbac-roles.svg"),
        ("TA per-class permissions", "rbac-ta-dual.svg"),
        ("Multiple roles, one login", "rbac-multi-role.svg"),
    ],
    "authentication.md": [
        ("Login methods", "auth-methods.svg"),
        ("SMS verification at signup", "auth-sms.svg"),
        ("Link multiple login methods", "auth-linking.svg"),
    ],
    "announcements.md": [
        ("Who can post", "announcements-who-posts.svg"),
        ("Who sees what", "announcements-visibility.svg"),
        ("How families receive news", "announcements-delivery.svg"),
    ],
    "glossary.md": [
        ("Account, user, and student", "glossary-concepts.svg"),
        ("Four portals", "glossary-portals.svg"),
    ],
    "vendor-qa.md": [
        ("School and vendor", "vendor-collaboration.svg"),
        ("Requirements timeline", "vendor-timeline.svg"),
        ("Current vendor focus", "vendor-focus.svg"),
    ],
}

README_DIAGRAMS = [
    ("Platform map", "README-platform-map.svg"),
]


def build_section(diagrams, prefix="assets/diagrams"):
    parts = ["## Diagrams\n\n", CAST]
    for title, file in diagrams:
        parts.append(f"### {title}\n\n")
        parts.append(f"![{title}]({prefix}/{file})\n\n")
    return "".join(parts)


def replace_diagrams(content, section):
    pattern = r"## Diagrams\n\n.*?(?=\n## |\Z)"
    if not re.search(pattern, content, re.DOTALL):
        return content + "\n\n" + section
    return re.sub(pattern, section.rstrip() + "\n\n", content, count=1, flags=re.DOTALL)


for page, diagrams in PAGE_DIAGRAMS.items():
    path = DOC / page
    text = path.read_text(encoding="utf-8")
    section = build_section(diagrams)
    path.write_text(replace_diagrams(text, section), encoding="utf-8")
    print("updated", page)

readme = Path(__file__).resolve().parent.parent / "README.md"
rt = readme.read_text(encoding="utf-8")
section = build_section(README_DIAGRAMS, "doc/assets/diagrams")
# Replace platform map mermaid block
rt = re.sub(
    r"### 🗺️ 平台大地图\n\n```mermaid\n.*?```\n\n",
    "### Platform map\n\n"
    + "![Platform map](doc/assets/diagrams/README-platform-map.svg)\n\n",
    rt,
    count=1,
    flags=re.DOTALL,
)
rt = rt.replace(
    "Each page includes **friendly diagrams** (Mermaid + emoji) for families, students (ages 7–13), and the vendor.",
    "Each page includes **flat-design SVG diagrams** (English labels, simple characters) for the vendor and school team.",
)
readme.write_text(rt, encoding="utf-8")
print("updated README.md")

doc_readme = DOC / "README.md"
drt = doc_readme.read_text(encoding="utf-8")
drt = drt.replace(
    "Each page has **2–3 Mermaid diagrams** with emoji and bilingual labels (中文/English) explaining the business logic for Sharon Chinese School families and students (~7–13).",
    "Each page has **2–3 flat SVG diagrams** with English labels and simple character art (students typically ages 7–13).",
)
doc_readme.write_text(drt, encoding="utf-8")
print("updated doc/README.md")
