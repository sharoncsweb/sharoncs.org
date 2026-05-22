#!/usr/bin/env python3
"""Generate flat-design SVG diagrams for the wiki (English only)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "doc" / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 720, 200
CHAR = 48


def char_parent(x, y, scale=1):
    s = scale
    return f"""
    <g transform="translate({x},{y}) scale({s})">
      <rect x="6" y="22" width="20" height="22" rx="5" fill="#3D9B8A"/>
      <circle cx="16" cy="12" r="9" fill="#F2C9A0"/>
      <path d="M8 10 Q16 4 24 10" fill="#2C2C2C"/>
    </g>"""


def char_student(x, y, scale=1):
    """Smaller proportions than parent/teacher (target age ~7-13). See DIAGRAM-DESIGN.md."""
    s = scale
    return f"""
    <g transform="translate({x},{y}) scale({s})">
      <rect x="8" y="26" width="16" height="15" rx="5" fill="#5B8DEF"/>
      <circle cx="16" cy="13" r="7" fill="#F2C9A0"/>
      <rect x="22" y="28" width="9" height="12" rx="2" fill="#F4B942"/>
    </g>"""


def char_teacher(x, y, scale=1):
    s = scale
    return f"""
    <g transform="translate({x},{y}) scale({s})">
      <rect x="5" y="22" width="22" height="22" rx="5" fill="#6B5CE7"/>
      <circle cx="16" cy="12" r="9" fill="#F2C9A0"/>
      <rect x="24" y="16" width="10" height="3" rx="1" fill="#fff"/>
    </g>"""


def char_admin(x, y, scale=1):
    s = scale
    return f"""
    <g transform="translate({x},{y}) scale({s})">
      <rect x="6" y="22" width="20" height="22" rx="5" fill="#5C6370"/>
      <circle cx="16" cy="12" r="9" fill="#F2C9A0"/>
      <rect x="11" y="26" width="10" height="12" rx="2" fill="#fff"/>
    </g>"""


def char_school(x, y, scale=0.9):
    s = scale
    return f"""
    <g transform="translate({x},{y}) scale({s})">
      <rect x="4" y="18" width="28" height="20" rx="3" fill="#E8ECF2"/>
      <polygon points="18,6 32,18 4,18" fill="#D45B5B"/>
    </g>"""


def arrow(x1, y1, x2, y2):
    return f"""
    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#94A3B8" stroke-width="2" marker-end="url(#arr)"/>
    """


def box(x, y, w, h, text, fill="#F8FAFC", stroke="#CBD5E1"):
    lines = text.split("\\n")
    ty = y + h / 2 - (len(lines) - 1) * 8
    tspans = "".join(
        f'<tspan x="{x + w/2}" dy="{14 if i else 0}">{line}</tspan>'
        for i, line in enumerate(lines)
    )
    return f"""
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
    <text text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#334155" x="{x+w/2}" y="{ty}">{tspans}</text>
    """


def wrap(title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{title}">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#94A3B8"/>
    </marker>
  </defs>
  <rect width="{W}" height="{H}" fill="#FFFFFF"/>
  {body}
</svg>"""


def diagram_stakeholders():
    b = (
        char_school(30, 45)
        + box(95, 50, 150, 75, "Sharon Chinese School", "#EEF2FF", "#A5B4FC")
        + arrow(245, 88, 270, 88)
        + char_parent(270, 65)
        + box(325, 70, 85, 55, "Parent")
        + arrow(410, 88, 435, 88)
        + char_student(435, 72)
        + box(490, 70, 95, 55, "Student")
        + arrow(585, 88, 610, 88)
        + char_teacher(610, 65)
        + box(665, 70, 45, 55, "Staff")
    )
    return wrap("Stakeholders at the school", b)


def diagram_phase_timeline():
    b = (
        box(40, 70, 180, 70, "Phase 1\\nRegistration &\\nParent portal", "#FEF3C7", "#FCD34D")
        + arrow(220, 105, 260, 105)
        + box(260, 70, 180, 70, "Phase 2\\nStudent & Teacher\\nLMS features", "#E0E7FF", "#A5B4FC")
        + arrow(440, 105, 480, 105)
        + box(480, 70, 180, 70, "Ongoing\\nImprovements", "#F1F5F9", "#CBD5E1")
    )
    return wrap("Implementation phases", b)


def diagram_legacy_new():
    b = (
        box(40, 65, 160, 80, "Legacy site\\nHard to use", "#FEE2E2", "#FCA5A5")
        + arrow(200, 105, 250, 105)
        + char_school(255, 50)
        + box(320, 65, 160, 80, "New platform\\nFamily accounts", "#D1FAE5", "#6EE7B7")
        + arrow(480, 105, 530, 105)
        + box(530, 65, 160, 80, "LMS\\nClasses & work", "#DBEAFE", "#93C5FD")
    )
    return wrap("Legacy to new platform", b)


def diagram_family_account():
    b = (
        box(280, 30, 160, 40, "Family Account", "#F8FAFC", "#94A3B8")
        + char_parent(80, 95)
        + box(30, 155, 100, 35, "Primary parent\\nBilling")
        + char_parent(220, 95)
        + box(200, 155, 90, 35, "Spouse")
        + char_student(400, 100)
        + box(380, 155, 110, 35, "Student A")
        + char_student(540, 100)
        + box(520, 155, 110, 35, "Student B")
        + arrow(130, 75, 280, 55)
        + arrow(250, 75, 300, 55)
        + arrow(430, 80, 350, 60)
        + arrow(570, 80, 400, 60)
    )
    return wrap("Family account structure", b)


def diagram_relationships():
    b = (
        char_parent(60, 70)
        + box(30, 140, 100, 40, "Self\\nParent user")
        + char_parent(260, 70)
        + box(230, 140, 100, 40, "Spouse\\nParent user")
        + char_student(480, 75)
        + box(450, 140, 110, 40, "Child\\nStudent profile")
        + arrow(130, 100, 230, 100)
        + arrow(330, 100, 450, 100)
    )
    return wrap("Family relationships", b)


def diagram_registration_sequence():
    b = (
        char_parent(40, 60)
        + box(110, 75, 120, 50, "Mobile +\\nverification")
        + arrow(230, 100, 280, 100)
        + box(280, 75, 110, 50, "Profile\\n(Self)")
        + arrow(390, 100, 440, 100)
        + box(440, 75, 110, 50, "Add child")
        + arrow(550, 100, 600, 100)
        + box(600, 75, 100, 50, "Enroll & pay")
        + char_student(640, 55, 0.85)
    )
    return wrap("Registration flow", b)


def diagram_parent_hub():
    b = (
        char_parent(300, 45, 1.2)
        + box(250, 30, 220, 45, "Parent portal", "#ECFDF5", "#34D399")
        + char_student(80, 110)
        + box(50, 155, 100, 35, "My children")
        + box(200, 155, 100, 35, "Enroll & pay")
        + box(350, 155, 100, 35, "Progress")
        + box(500, 155, 100, 35, "Announcements")
        + arrow(350, 75, 100, 120)
        + arrow(350, 75, 250, 150)
        + arrow(360, 75, 400, 150)
        + arrow(360, 75, 550, 150)
    )
    return wrap("Parent portal hub", b)


def diagram_student_dashboard():
    b = (
        char_student(60, 55, 1.2)
        + box(40, 30, 200, 40, "Student portal", "#EFF6FF", "#60A5FA")
        + box(300, 60, 120, 55, "Today schedule")
        + box(440, 60, 120, 55, "To-do work")
        + box(580, 60, 120, 55, "Course pages")
        + arrow(240, 90, 295, 90)
        + arrow(240, 90, 435, 90)
        + arrow(240, 90, 575, 90)
    )
    return wrap("Student dashboard", b)


def diagram_cart_flow():
    b = (
        char_parent(30, 65)
        + box(100, 75, 90, 50, "Pick student")
        + arrow(190, 100, 230, 100)
        + box(230, 75, 90, 50, "Add classes")
        + arrow(320, 100, 360, 100)
        + box(360, 75, 80, 50, "Cart")
        + arrow(440, 100, 480, 100)
        + box(480, 75, 90, 50, "Discounts")
        + arrow(570, 100, 610, 100)
        + box(610, 75, 90, 50, "Pay")
    )
    return wrap("Enrollment and payment", b)


def diagram_rbac_roles():
    b = (
        char_parent(40, 70) + box(25, 140, 70, 30, "Parent")
        + char_student(150, 75) + box(135, 140, 70, 30, "Student")
        + char_teacher(260, 70) + box(245, 140, 70, 30, "Teacher")
        + char_student(370, 70) + box(355, 140, 70, 30, "TA")
        + char_parent(480, 70) + box(465, 140, 80, 30, "Volunteer")
        + char_admin(600, 70) + box(585, 140, 80, 30, "Admin")
    )
    return wrap("School roles", b)


def diagram_platform_map():
    b = (
        box(40, 50, 120, 60, "Public website")
        + arrow(160, 80, 210, 80)
        + box(210, 50, 100, 60, "Sign in")
        + arrow(310, 80, 360, 80)
        + char_parent(365, 55)
        + box(420, 55, 95, 50, "Parent")
        + char_student(530, 58)
        + box(585, 55, 95, 50, "Student")
        + char_teacher(40, 130)
        + box(95, 125, 80, 45, "Teacher")
        + char_admin(200, 130)
        + box(255, 125, 80, 45, "Admin")
    )
    return wrap("Platform portals", b)


def diagram_ta_dual():
    b = (
        char_student(280, 50, 1.1)
        + box(250, 25, 140, 35, "Same person", "#F8FAFC", "#CBD5E1")
        + arrow(300, 95, 120, 120)
        + arrow(340, 95, 520, 120)
        + box(60, 120, 150, 55, "In Class A\\nTeacher rights", "#FEF3C7", "#FCD34D")
        + box(480, 120, 150, 55, "In Class B\\nStudent rights", "#EFF6FF", "#93C5FD")
        + char_teacher(90, 135, 0.9)
        + char_student(520, 140, 0.9)
    )
    return wrap("TA dual role per class", b)


def diagram_who_posts():
    b = (
        char_admin(50, 60)
        + box(30, 130, 110, 40, "School-wide")
        + char_teacher(280, 60)
        + box(260, 130, 110, 40, "Class only")
        + char_parent(500, 65)
        + box(480, 130, 120, 40, "Family reads")
    )
    return wrap("Announcement visibility", b)


def diagram_login_methods():
    b = (
        char_parent(300, 40, 1.1)
        + box(250, 25, 220, 35, "One user account", "#F8FAFC", "#CBD5E1")
        + box(80, 100, 100, 45, "Mobile SMS")
        + box(200, 100, 100, 45, "Username")
        + box(320, 100, 100, 45, "Google")
        + box(440, 100, 100, 45, "Microsoft")
        + box(560, 100, 120, 45, "Social login")
        + arrow(350, 60, 130, 100)
        + arrow(350, 60, 250, 100)
        + arrow(350, 60, 370, 100)
        + arrow(350, 60, 490, 100)
        + arrow(350, 60, 610, 100)
    )
    return wrap("Login methods", b)


def diagram_grade_classes():
    b = (
        box(280, 35, 160, 40, "Grade 2 Chinese", "#EEF2FF", "#A5B4FC")
        + arrow(360, 75, 150, 110)
        + arrow(360, 75, 470, 110)
        + box(80, 110, 140, 55, "Class A\\nSat 9am")
        + box(480, 110, 140, 55, "Class B\\nSat 11am")
        + char_student(110, 95, 0.85)
        + char_student(510, 95, 0.85)
    )
    return wrap("Grade with multiple classes", b)


def diagram_course_lifecycle():
    b = (
        char_admin(50, 65)
        + box(30, 140, 100, 35, "Define course")
        + arrow(130, 100, 200, 100)
        + char_teacher(200, 65)
        + box(180, 140, 110, 35, "Upload content")
        + arrow(290, 100, 380, 100)
        + char_student(380, 70)
        + box(360, 140, 110, 35, "Learn & submit")
    )
    return wrap("Course lifecycle", b)


def diagram_parent_day():
    b = (
        char_parent(40, 60)
        + box(110, 75, 90, 50, "Sign in")
        + arrow(200, 100, 240, 100)
        + box(240, 75, 100, 50, "Announcements")
        + arrow(340, 100, 380, 100)
        + box(380, 75, 100, 50, "Child schedule")
        + arrow(480, 100, 520, 100)
        + box(520, 75, 110, 50, "Enroll or review")
    )
    return wrap("Typical parent session", b)


def diagram_primary_spouse():
    b = (
        char_parent(120, 55, 1.1)
        + box(90, 30, 130, 40, "Primary parent", "#ECFDF5", "#34D399")
        + box(90, 130, 130, 40, "Checkout & billing")
        + char_parent(420, 55, 1.1)
        + box(390, 30, 130, 40, "Spouse", "#F8FAFC", "#CBD5E1")
        + box(390, 130, 130, 40, "View & manage\\n(usually no pay)")
    )
    return wrap("Primary parent vs spouse", b)


def diagram_in_person():
    b = (
        char_school(80, 50)
        + box(50, 120, 140, 45, "In-person class", "#D1FAE5", "#6EE7B7")
        + arrow(190, 90, 280, 90)
        + box(280, 60, 160, 70, "LMS support\\nassignments & materials", "#DBEAFE", "#93C5FD")
        + arrow(440, 90, 530, 90)
        + box(530, 75, 150, 50, "Not a video-only school", "#F1F5F9", "#CBD5E1")
    )
    return wrap("In-person plus LMS", b)


def diagram_volunteer_reminder():
    b = (
        char_parent(60, 60)
        + box(40, 130, 120, 40, "Duty scheduled")
        + arrow(160, 100, 280, 100)
        + box(280, 75, 140, 50, "Reminder 3 days before")
        + arrow(420, 100, 520, 100)
        + box(520, 75, 140, 50, "Shows up on duty")
    )
    return wrap("Volunteer duty reminder", b)


def diagram_reschedule():
    b = (
        box(60, 75, 140, 50, "Yearly schedule")
        + arrow(200, 100, 280, 100)
        + box(280, 75, 120, 50, "One conflict")
        + arrow(400, 100, 480, 100)
        + box(480, 75, 180, 50, "Move session or substitute")
    )
    return wrap("Reschedule one session", b)


def diagram_registration_flow_complete():
    b = (
        box(30, 85, 95, 45, "1. Register\\nMobile + SMS", "#FEF3C7", "#FCD34D")
        + arrow(125, 108, 155, 108)
        + box(155, 85, 95, 45, "2. Parent\\nprofile", "#ECFDF5", "#6EE7B7")
        + arrow(250, 108, 280, 108)
        + box(280, 85, 95, 45, "3. Add\\nchildren", "#EFF6FF", "#93C5FD")
        + arrow(375, 108, 405, 108)
        + box(405, 85, 95, 45, "4. Pick\\nclasses", "#E0E7FF", "#A5B4FC")
        + arrow(500, 108, 530, 108)
        + box(530, 85, 95, 45, "5. Pay", "#D1FAE5", "#34D399")
        + arrow(625, 108, 655, 108)
        + box(655, 85, 55, 45, "Done", "#F1F5F9", "#CBD5E1")
        + char_parent(50, 35, 0.9)
        + char_student(300, 38, 0.85)
    )
    return wrap("Complete registration flow phase 1", b)


def diagram_vendor_collab():
    b = (
        char_school(60, 55)
        + box(40, 130, 120, 40, "School team")
        + arrow(160, 100, 280, 100)
        + box(280, 70, 160, 60, "Requirements wiki")
        + arrow(440, 100, 520, 100)
        + box(520, 70, 160, 60, "The Web Design LLC")
    )
    return wrap("School and vendor collaboration", b)


# Map filename -> generator
ALL = {
    "overview-stakeholders": diagram_stakeholders,
    "overview-phases": diagram_phase_timeline,
    "overview-legacy-new": diagram_legacy_new,
    "accounts-family": diagram_family_account,
    "accounts-relationships": diagram_relationships,
    "accounts-registration-flow": diagram_registration_sequence,
    "parent-portal-hub": diagram_parent_hub,
    "parent-portal-day": diagram_parent_day,
    "parent-primary-spouse": diagram_primary_spouse,
    "student-dashboard": diagram_student_dashboard,
    "student-course-page": diagram_student_dashboard,
    "student-homework": diagram_registration_sequence,
    "teacher-workspace": diagram_course_lifecycle,
    "teacher-grading": diagram_registration_sequence,
    "teacher-ta-dual": diagram_ta_dual,
    "admin-year-setup": diagram_course_lifecycle,
    "admin-volunteer": diagram_volunteer_reminder,
    "admin-reschedule": diagram_reschedule,
    "registration-signup-steps": diagram_registration_sequence,
    "registration-field-groups": diagram_relationships,
    "registration-who-fills": diagram_family_account,
    "payment-cart": diagram_cart_flow,
    "payment-discounts": diagram_phase_timeline,
    "payment-checkout": diagram_family_account,
    "courses-lifecycle": diagram_course_lifecycle,
    "courses-in-person": diagram_in_person,
    "courses-classroom-style": diagram_student_dashboard,
    "school-grade-classes": diagram_grade_classes,
    "school-pick-class": diagram_grade_classes,
    "school-placement": diagram_registration_sequence,
    "rbac-roles": diagram_rbac_roles,
    "rbac-ta-dual": diagram_ta_dual,
    "rbac-multi-role": diagram_login_methods,
    "auth-methods": diagram_login_methods,
    "auth-sms": diagram_registration_sequence,
    "auth-linking": diagram_login_methods,
    "announcements-who-posts": diagram_who_posts,
    "announcements-visibility": diagram_who_posts,
    "announcements-delivery": diagram_parent_hub,
    "glossary-concepts": diagram_family_account,
    "glossary-portals": diagram_platform_map,
    "vendor-collaboration": diagram_vendor_collab,
    "vendor-timeline": diagram_phase_timeline,
    "vendor-focus": diagram_cart_flow,
    "platform-one-school": diagram_stakeholders,
    "platform-layers": diagram_platform_map,
    "platform-payment": diagram_cart_flow,
    "README-platform-map": diagram_platform_map,
    "registration-flow-complete": diagram_registration_flow_complete,
}

for name, fn in ALL.items():
    (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
    print("wrote", name)

print(f"Generated {len(ALL)} diagrams in {OUT}")
