from Domains.Student import Student
from Domains.Course import Course

def input_students():
    n = int(input("Number of students: "))
    students = []
    for i in range(n):
        print(f"\nStudent {i+1} info: ")
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        student = Student(sid, name, dob)
        students.append(student)
        print("Recorded student:")
        student.show()

    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.sid},{s.name},{s.dob}\n")

    return students

def input_courses():
    n = int(input("Number of courses: "))
    courses = []
    for i in range(n):
        print(f"\nCourse {i+1} info: ")
        cid = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credits: "))
        course = Course(cid, name, credit)
        courses.append(course)
        print("Recorded course:")
        course.show()

    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c.cid},{c.name},{c.credit}\n")
    return courses

def input_marks(students, courses):
    with open("marks.txt", "w") as f:
        for c in courses:
            print(f"\nMarks for {c.name}:")
            for s in students:
                m = float(input(f"{s.name} ({s.sid}): "))
                s.add_mark(c.cid, m)
                f.write(f"{s.sid},{c.cid},{m}\n")
