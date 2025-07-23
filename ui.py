# =================================================================
#  File: ui.py
#  Purpose: Handles all user interface menus and prompts.
# =================================================================
"""
This module contains all the user interface menus and logic for the application.
"""
import crud_operations
import advanced_queries

def manage_students_menu():
    """Menu for managing student records."""
    while True:
        print("\n--- Manage Students ---")
        print("1. Add a new Student")
        print("2. Search for Students")
        print("3. Edit a Student (Not Implemented)")
        print("4. Delete a Student (Not Implemented)")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            crud_operations.add_student()
        elif choice == '2':
            crud_operations.search_students()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def manage_lecturers_menu():
    """Menu for managing lecturer records."""
    while True:
        print("\n--- Manage Lecturers ---")
        print("1. Add a new Lecturer")
        print("2. Search for Lecturers")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            crud_operations.add_lecturer()
        elif choice == '2':
            crud_operations.search_lecturers()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def manage_courses_menu():
    """Menu for managing course records."""
    while True:
        print("\n--- Manage Courses ---")
        print("1. Add a new Course")
        print("2. Search for Courses")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            crud_operations.add_course()
        elif choice == '2':
            crud_operations.search_courses()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def advanced_query_menu():
    """Menu for running advanced queries and reports."""
    menu_options = {
        '1': ('Find students in a course by lecturer', advanced_queries.find_students_in_course_by_lecturer),
        '2': ('List high-achieving final year students', advanced_queries.find_high_achieving_final_year_students),
        '3': ('Find students not registered for current semester', advanced_queries.find_unregistered_students_for_current_semester),
        '4': ("Find a student's current advisor", advanced_queries.find_advisor_for_student),
        '5': ('Search lecturers by research area', advanced_queries.find_lecturers_by_expertise),
        '6': ("List courses taught by a department's lecturers", advanced_queries.find_courses_by_department_lecturer),
        '7': ('Identify top student project supervisor', advanced_queries.find_top_project_supervisor),
        '8': ('Generate report on recent publications', advanced_queries.find_recent_publications),
        '9': ('Find students advised by a specific lecturer', advanced_queries.find_students_by_advisor),
        '10': ('Find staff members by department', advanced_queries.find_staff_by_department),
        '11': ('Student Employee Supervisor Report', advanced_queries.student_employee_supervisor_report),
        '0': ('Back to Main Menu', None)
    }

    while True:
        print("\n--- Advanced Queries & Reports ---")
        for key, (text, _) in menu_options.items():
            print(f"{key}. {text}")

        choice = input("Enter your choice: ")
        action = menu_options.get(choice)

        if action:
            if action[1]:
                action[1]()
            else: # This is for '0'
                break
        else:
            print("Invalid choice.")

def main_menu():
    """Displays the main application menu."""
    menu_options = {
        '1': ('Manage Students', manage_students_menu),
        '2': ('Manage Lecturers', manage_lecturers_menu),
        '3': ('Manage Courses', manage_courses_menu),
        '4': ('Advanced Queries & Reports', advanced_query_menu),
        '0': ('Exit', None)
    }

    while True:
        print("\n===== University Record Management System =====")
        for key, (text, _) in menu_options.items():
            print(f"{key}. {text}")

        choice = input("Enter your choice: ")
        action = menu_options.get(choice)

        if action:
            if action[1]:
                action[1]()
            else: # This is for '0'
                print("Exiting program. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")
