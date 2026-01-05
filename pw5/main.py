from inputs import input_students, input_courses, input_marks
from outputs import show_students, show_courses, show_marks, show_gpas
import os, zipfile

def save_data():
    """Compress text files into students.dat"""
    with zipfile.ZipFile("students.dat", "w") as z:
        for fname in ["students.txt", "courses.txt", "marks.txt"]:
            if os.path.exists(fname):
                z.write(fname)
            else:
                print(f"Warning: {fname} not found, skipping.")
    print("All files compressed into students.dat")

def main():
    students = input_students()
    courses = input_courses()
    input_marks(students, courses)

    show_students(students)
    show_courses(courses)
    show_marks(students, courses)
    show_gpas(students, courses)

    save_data()

if __name__ == "__main__":
    main()
