from inputs import input_students, input_courses, input_marks
from outputs import show_students, show_courses, show_marks, show_gpas

def main():
    students = input_students()
    courses = input_courses()
    input_marks(students, courses)

    show_students(students)
    show_courses(courses)
    show_marks(students, courses)
    show_gpas(students, courses)

if __name__ == "__main__":
    main()
