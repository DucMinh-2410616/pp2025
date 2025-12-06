class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {} 

    def information(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("DoB:", self.dob)

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def information(self):
        print("ID:", self.id)
        print("Name:", self.name)


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            student_id = input(f"Student {i+1} ID: ")
            name = input(f"Student {i+1} Name: ")
            dob = input(f"Student {i+1} DoB: ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("\nEnter number of courses: "))
        for i in range(num_courses):
            course_id = input(f"Course {i+1} ID: ") 
            name = input(f"Course {i+1} Name: ")
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        print("\nEnter marks for each course:")
        for course in self.courses:
            print(f"\nCourse: {course.id} - {course.name}")
            for student in self.students:
                mark = float(input(f"Mark for {student.name} ({student.id}): "))
                student.add_mark(course.id, mark)

    def show_students(self):
        print("\nStudents")
        for student in self.students:
            student.information()

    def show_courses(self):
        print("\nCourses")
        for course in self.courses:
            course.information()

    def show_marks(self):
        print("\nMarks")
        for course in self.courses:
            print(f"\nCourse: {course.name} ({course.id})") 
            for student in self.students:
                if course.id in student.marks:
                    print(f"{student.name} ({student.id}): {student.marks[course.id]}")

    def choose_course(self):
        course_id = input("\nEnter the course ID to view marks: ")
        print(f"\nMarks for course {course_id}:")
        for student in self.students:
            if course_id in student.marks:
                print(f"{student.name} ({student.id}): {student.marks[course_id]}")
            else:
                print(f"{student.name} ({student.id}): No mark recorded")



if __name__ == "__main__":
    school = School()
    school.input_students()
    school.input_courses()
    school.input_marks()

    school.show_students()
    school.show_courses()
    school.show_marks()
    school.choose_course()