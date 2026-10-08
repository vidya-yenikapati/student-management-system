import json
from pathlib import Path

FILE_NAME = "students.json"


def load_students():
    file = Path(FILE_NAME)

    if file.exists():
        try:
            with open(file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    return []


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    marks = float(input("Enter marks: "))

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n----- Student Records -----")

    for student in students:
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Course : {student['course']}")
        print(f"Marks  : {student['marks']}")
        print("---------------------------")


def search_student(students):
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Course : {student['course']}")
            print(f"Marks  : {student['marks']}")
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ").strip()
            student["course"] = input("Enter new course: ").strip()
            student["marks"] = float(input("Enter new marks: "))

            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
