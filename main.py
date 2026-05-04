from student import Student
from database import init_db, add_student, get_all_students, delete_student, get_average
from tabulate import tabulate

def show_menu():
    print("\n===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Get Subject Average")
    print("4. Delete Student")
    print("5. Exit")
    print("=================================")

def add_new_student():
    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    
    while True:
        try:
            grade = int(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")

    student = Student(name, subject, grade)
    add_student(student.name, student.subject, student.grade, student.get_letter_grade())
    print(f"\n✓ {name} added successfully! Letter grade: {student.get_letter_grade()}")

def view_students():
    rows = get_all_students()
    if not rows:
        print("\nNo students found!")
        return
    headers = ["ID", "Name", "Subject", "Grade", "Letter"]
    print("\n" + tabulate(rows, headers=headers, tablefmt="grid"))

def subject_average():
    subject = input("Enter subject name: ")
    avg = get_average(subject)
    if avg == 0:
        print(f"\nNo students found for {subject}!")
    else:
        print(f"\nAverage grade for {subject}: {avg}")

def remove_student():
    view_students()
    try:
        student_id = int(input("\nEnter student ID to delete: "))
        delete_student(student_id)
        print(f"✓ Student {student_id} deleted successfully!")
    except ValueError:
        print("Please enter a valid ID!")

def main():
    init_db()
    print("Welcome to Student Grade Manager!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_new_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            subject_average()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()