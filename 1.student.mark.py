students = [] 
courses = []  
marks = {}
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    Student_id = input(f"Student {i+1} ID: ")
    name = input(f"Student {i+1} Name: ")
    DoB = input(f"Student {i+1} DoB: ")
    students.append({"id": Student_id, "name": name, "dob": DoB})

num_courses = int(input("\nEnter number of courses: "))
for i in range(num_courses):
    Coure_id = input(f"Course {i+1} ID: ")
    name = input(f"Course {i+1} Name: ")
    courses.append({"id": Coure_id, "name": name})

print("\nEnter marks for each course:")
for c in courses:
    print(f"\nCourse: {c['id']} - {c['name']}")
    course_marks = []
    for s in students:
        mark = float(input(f"Mark for {s['name']} ({s['id']}): "))
        course_marks.append((s["id"], mark))
    marks[c["id"]] = course_marks

print("\nStudents")
for s in students:
    print(f"{s['id']} - {s['name']} - {s['dob']}")

print("\nCourses")
for c in courses:
    print(f"{c['id']} - {c['name']}")

print("\nMarks")
for Course_id, course_marks in marks.items():
    Course_name = next(c["name"] for c in courses if c["id"] == Course_id)
    print(f"\nCourse: {Course_name} ({Course_id})")
    for Sudent_id, mark in course_marks:
        student = next(s for s in students if s["id"] == Student_id)
        print(f"{student['name']} ({Student_id}): {mark}")
