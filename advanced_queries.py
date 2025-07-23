# =================================================================
#  File: advanced_queries.py
#  Purpose: Contains functions for the complex, multi-join queries.
# =================================================================
"""
This module contains all the advanced, multi-join queries and reports.
"""
import db_connector
import app_utils

def find_students_in_course_by_lecturer():
    """Finds students in a specific course taught by a specific lecturer."""
    print("\n--- Find Students in a Specific Course/Lecturer Combo ---")
    course_code = app_utils.get_user_input("Enter Course Code (e.g., CS101): ")
    lecturer_last_name = app_utils.get_user_input("Enter Lecturer's Last Name (e.g., Turing): ")

    query = """
        SELECT s.first_name, s.last_name, s.student_email, c.name AS course_name
        FROM Students s
        JOIN Enrollment e ON s.student_id = e.student_id
        JOIN CourseOfferings co ON e.offering_id = co.offering_id
        JOIN Courses c ON co.course_id = c.course_id
        JOIN Lecturers l ON co.lecturer_id = l.lecturer_id
        WHERE c.course_code = %s AND l.last_name = %s;
    """
    results = db_connector.execute_query(query, (course_code, lecturer_last_name), fetch='all')
    app_utils.print_table(results)

def find_high_achieving_final_year_students():
    """Lists final-year students with an average grade above 70%."""
    print("\n--- List High-Achieving Final Year Students (Avg Grade > 70) ---")
    query = """
        SELECT
            s.first_name, s.last_name, p.name AS program_name,
            s.year_of_study, FORMAT(AVG(g.grade_percentage), 2) AS average_grade
        FROM Students s
        JOIN Programs p ON s.program_id = p.program_id
        JOIN Enrollment e ON s.student_id = e.student_id
        JOIN Grades g ON e.enrollment_id = g.enrollment_id
        WHERE s.year_of_study = p.duration_years
        GROUP BY s.student_id, s.first_name, s.last_name, p.name, s.year_of_study
        HAVING AVG(g.grade_percentage) > 70.00
        ORDER BY average_grade DESC;
    """
    results = db_connector.execute_query(query, fetch='all')
    app_utils.print_table(results)

def find_unregistered_students_for_current_semester():
    """Finds students not registered for any courses in a given semester."""
    print("\n--- Find Students Not Registered in Current Semester ---")
    year = app_utils.get_user_input("Enter Current Year (e.g., 2024): ")
    semester = app_utils.get_user_input("Enter Current Semester (e.g., Fall): ")
    query = """
        SELECT s.student_id, s.first_name, s.last_name, s.student_email
        FROM Students s
        WHERE s.student_id NOT IN (
            SELECT DISTINCT e.student_id
            FROM Enrollment e
            JOIN CourseOfferings co ON e.offering_id = co.offering_id
            WHERE co.year = %s AND co.semester = %s
        );
    """
    results = db_connector.execute_query(query, (year, semester), fetch='all')
    app_utils.print_table(results)

def find_advisor_for_student():
    """Retrieves the current advisor for a specific student."""
    print("\n--- Find a Student's Current Advisor ---")
    student_id = app_utils.get_user_input("Enter Student ID: ")
    query = """
        SELECT s.first_name AS student_first, s.last_name AS student_last,
               l.first_name AS advisor_first, l.last_name AS advisor_last, l.work_email
        FROM Students s
        JOIN AdvisingHistory ah ON s.student_id = ah.student_id
        JOIN Lecturers l ON ah.lecturer_id = l.lecturer_id
        WHERE s.student_id = %s AND ah.end_date IS NULL;
    """
    results = db_connector.execute_query(query, (student_id,), fetch='all')
    app_utils.print_table(results)

def find_lecturers_by_expertise():
    """Searches for lecturers by their research area."""
    print("\n--- Search Lecturers by Research Area ---")
    area_name = app_utils.get_user_input("Enter Research Area (e.g., Artificial Intelligence): ")
    query = """
        SELECT l.first_name, l.last_name, l.work_email
        FROM Lecturers l
        JOIN LecturerResearchAreas lra ON l.lecturer_id = lra.lecturer_id
        JOIN ResearchAreas ra ON lra.area_id = ra.area_id
        WHERE ra.name LIKE %s;
    """
    results = db_connector.execute_query(query, (f"%{area_name}%",), fetch='all')
    app_utils.print_table(results)

def find_courses_by_department_lecturer():
    """Lists all courses taught by lecturers from a specific department."""
    print("\n--- List Courses Taught by a Department's Lecturers ---")
    department_name = app_utils.get_user_input("Enter Department Name (e.g., Computer Science): ")
    query = """
        SELECT DISTINCT c.course_code, c.name AS course_name
        FROM Courses c
        JOIN CourseOfferings co ON c.course_id = co.course_id
        JOIN Lecturers l ON co.lecturer_id = l.lecturer_id
        JOIN Departments d ON l.department_id = d.department_id
        WHERE d.name = %s
        ORDER BY c.course_code;
    """
    results = db_connector.execute_query(query, (department_name,), fetch='all')
    app_utils.print_table(results)

def find_top_project_supervisor():
    """Identifies the lecturer supervising the most students on research projects."""
    print("\n--- Identify Lecturer Supervising Most Students on Projects ---")
    query = """
        SELECT l.first_name, l.last_name, COUNT(pm.student_id) AS students_supervised
        FROM Lecturers l
        JOIN ResearchProjects rp ON l.lecturer_id = rp.principal_investigator_id
        JOIN ProjectMembers pm ON rp.project_id = pm.project_id
        GROUP BY l.lecturer_id, l.first_name, l.last_name
        ORDER BY students_supervised DESC
        LIMIT 1;
    """
    results = db_connector.execute_query(query, fetch='all')
    app_utils.print_table(results)

def find_recent_publications():
    """Generates a report of publications from the past year."""
    print("\n--- Generate Report on Publications in the Past Year ---")
    query = """
        SELECT p.year, p.title, p.publication_venue,
               GROUP_CONCAT(CONCAT(l.first_name, ' ', l.last_name) SEPARATOR ', ') AS authors
        FROM Publications p
        JOIN LecturerPublications lp ON p.publication_id = lp.publication_id
        JOIN Lecturers l ON lp.lecturer_id = l.lecturer_id
        WHERE p.year >= (YEAR(CURDATE()) - 1)
        GROUP BY p.publication_id, p.year, p.title, p.publication_venue
        ORDER BY p.year DESC;
    """
    results = db_connector.execute_query(query, fetch='all')
    app_utils.print_table(results)

def find_students_by_advisor():
    """Finds all students currently advised by a specific lecturer."""
    print("\n--- Find Students Advised by a Specific Lecturer ---")
    lecturer_id = app_utils.get_user_input("Enter Lecturer ID: ")
    query = """
        SELECT s.first_name, s.last_name, s.student_email
        FROM Students s
        JOIN AdvisingHistory ah ON s.student_id = ah.student_id
        WHERE ah.lecturer_id = %s AND ah.end_date IS NULL;
    """
    results = db_connector.execute_query(query, (lecturer_id,), fetch='all')
    app_utils.print_table(results)

def find_staff_by_department():
    """Finds all non-academic staff members in a specific department."""
    print("\n--- Find Staff Members by Department ---")
    department_id = app_utils.get_user_input("Enter Department ID: ")
    query = """
        SELECT nas.first_name, nas.last_name, nas.job_title
        FROM NonAcademicStaff nas
        WHERE nas.department_id = %s;
    """
    results = db_connector.execute_query(query, (department_id,), fetch='all')
    app_utils.print_table(results)

def student_employee_supervisor_report():
    """Informs the user that this feature is not supported by the schema."""
    print("\n--- Student Employee Supervisor Report ---")
    print("This functionality is not supported by the current database schema.")
    print("The schema does not include a concept of 'student employees' or a link")
    print("between NonAcademicStaff (as supervisors) and Students (as employees).")
    print("This would be a valuable future enhancement.")
