import math
import numpy as np

class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.marks = {}

    def show(self):
        print(f"{self.sid} - {self.name} - {self.dob}")

    def add_mark(self, cid, mark):
        mark = math.floor(mark * 10) / 10 
        self.marks[cid] = mark

    def gpa(self, courses):
        scores, credits = [], []
        for c in courses:
            if c.cid in self.marks:
                scores.append(self.marks[c.cid])
                credits.append(c.credit)
        if credits:
            scores = np.array(scores)
            credits = np.array(credits)
            return round(np.sum(scores * credits) / np.sum(credits), 2)
        return 0.0

class Course:
    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit

    def show(self):
        print(f"{self.cid} - {self.name} - {self.credit} credits")

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        n = int(input("Number of students: "))
        for i in range(n):
            print(f"\nStudent {i+1} info: ")
            sid = input("ID: ")
            name = input("Name: ")
            dob = input("DoB: ")
            student = Student(sid, name, dob)
            self.students.append(student)

    def input_courses(self):
        n = int(input("\nNumber of courses: "))
        for i in range(n):
            print(f"\n Course {i+1} info: ")
            cid = input("Course ID: ")
            name = input("Course name: ")
            credit = int(input("Credits: "))
            course = Course(cid, name, credit)
            self.courses.append(course)

    def input_marks(self):
        for c in self.courses:
            print(f"\nMarks for {c.name}:")
            for s in self.students:
                m = float(input(f"{s.name} ({s.sid}): "))
                s.add_mark(c.cid, m)
        print("\nStudent GPAs:")
        for s in self.students:
            print(f"{s.name} ({s.sid}) GPA: {s.gpa(self.courses)}")

    def show_students(self):
        print("\nStudents:")
        for s in self.students:
            s.show()

    def show_courses(self):
        print("\nCourses:")
        for c in self.courses:
            c.show()

    def show_marks(self):
        print("\nMarks:")
        for c in self.courses:
            print(f"\n{c.name} ({c.cid})")
            for s in self.students:
                if c.cid in s.marks:
                    print(f"{s.name}: {s.marks[c.cid]}")

    def choose_course(self):
        cid = input("\nCourse ID to view: ")
        for s in self.students:
            if cid in s.marks:
                print(f"{s.name}: {s.marks[cid]}")
            else:
                print(f"{s.name}: no mark")

    def sort_by_gpa(self):
        self.students.sort(key=lambda st: st.gpa(self.courses), reverse=True)
        print("\nStudents sorted by GPA:")
        for s in self.students:
            print(f"{s.name} ({s.sid}) GPA: {s.gpa(self.courses)}")

if __name__ == "__main__":
    school = School()
    school.input_students()
    school.input_courses()
    school.input_marks()
    school.show_students()
    school.show_courses()
    school.show_marks()
    school.choose_course()
    school.sort_by_gpa()
