def show_students(students):
    print("\nStudents:")
    for s in students:
        s.show()

def show_courses(courses):
    print("\nCourses:")
    for c in courses:
        c.show()

def show_marks(students, courses):
    print("\nMarks:")
    for c in courses:
        print(f"\n{c.name} ({c.cid})")
        for s in students:
            if c.cid in s.marks:
                print(f"{s.name}: {s.marks[c.cid]}")

def show_gpas(students, courses):
    print("\nStudent GPAs:")
    for s in students:
        print(f"{s.name} ({s.sid}) GPA: {s.gpa(courses)}")
