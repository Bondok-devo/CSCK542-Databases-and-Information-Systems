# =================================================================
#  File: app_logic.py
#  Purpose: Contains all application logic and database interactions.
# =================================================================
"""
This module separates the application logic from the GUI.
It contains all functions that interact with the database.
"""
import db_connector

# --- Data for Dropdowns ---
def get_programs_list():
    """Fetches all programs for dropdowns."""
    return db_connector.execute_query("SELECT program_id, name FROM Programs ORDER BY name", fetch='all')

def get_departments_list():
    """Fetches all departments for dropdowns."""
    return db_connector.execute_query("SELECT department_id, name FROM Departments ORDER BY name", fetch='all')

def get_lecturers_list():
    """Fetches all lecturers for dropdowns."""
    query = "SELECT lecturer_id, CONCAT(first_name, ' ', last_name) as name FROM Lecturers ORDER BY last_name"
    return db_connector.execute_query(query, fetch='all')

def get_students_list():
    """Fetches all students for dropdowns."""
    query = "SELECT student_id, CONCAT(first_name, ' ', last_name) as name FROM Students ORDER BY last_name"
    return db_connector.execute_query(query, fetch='all')

def get_courses_list():
    """Fetches all courses for dropdowns."""
    return db_connector.execute_query("SELECT course_id, CONCAT(course_code, ' - ', name) as name FROM Courses ORDER BY course_code", fetch='all')

def get_course_offerings_list():
    """Fetches available course offerings for enrollment."""
    query = """
        SELECT co.offering_id, CONCAT(c.course_code, ' (', co.year, ' Sem ', co.semester, ')') as name
        FROM CourseOfferings co
        JOIN Courses c ON co.course_id = c.course_id
        ORDER BY c.course_code, co.year, co.semester
    """
    return db_connector.execute_query(query, fetch='all')

def get_research_areas_list():
    """Fetches all research areas for dropdowns."""
    return db_connector.execute_query("SELECT area_id, name FROM ResearchAreas ORDER BY name", fetch='all')

def get_lecturers_for_course(course_id):
    """Fetches lecturers who teach a specific course."""
    query = """
        SELECT l.lecturer_id, CONCAT(l.first_name, ' ', l.last_name) as name
        FROM Lecturers l
        JOIN CourseOfferings co ON l.lecturer_id = co.lecturer_id
        WHERE co.course_id = %s
        GROUP BY l.lecturer_id, name
        ORDER BY MIN(l.last_name)
    """
    return db_connector.execute_query(query, (course_id,), fetch='all')


# --- Generic CRUD ---
def delete_record(table_name, id_column, record_id):
    """Deletes a record from a table by its ID."""
    query = f"DELETE FROM {table_name} WHERE {id_column} = %s"
    return db_connector.execute_query(query, (record_id,))

def get_record_by_id(table_name, id_column, record_id):
    """Fetches a single full record by its ID."""
    query = f"SELECT * FROM {table_name} WHERE {id_column} = %s"
    return db_connector.execute_query(query, (record_id,), fetch='one')

# --- Department Logic ---
def add_department(data):
    """Adds a new department."""
    query = "INSERT INTO Departments (name) VALUES (%(name)s)"
    return db_connector.execute_query(query, data)

def update_department(data):
    """Updates an existing department."""
    query = "UPDATE Departments SET name=%(name)s WHERE department_id=%(department_id)s"
    return db_connector.execute_query(query, data)

def search_departments(name):
    """Searches for departments."""
    query = "SELECT department_id, name FROM Departments WHERE 1=1"
    params = []
    if name:
        query += " AND name LIKE %s"
        params.append(f"%{name}%")
    query += " ORDER BY name"
    return db_connector.execute_query(query, tuple(params), fetch='all')

# --- Department Research Area Logic ---
def get_department_research_areas(department_id):
    """Gets all research areas for a given department."""
    query = """
        SELECT ra.area_id, ra.name FROM ResearchAreas ra
        JOIN DepartmentResearchAreas dra ON ra.area_id = dra.area_id
        WHERE dra.department_id = %s
    """
    return db_connector.execute_query(query, (department_id,), fetch='all')

def add_area_to_department(department_id, area_id):
    """Adds a research area to a department."""
    query = "INSERT INTO DepartmentResearchAreas (department_id, area_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (department_id, area_id))

def remove_area_from_department(department_id, area_id):
    """Removes a research area from a department."""
    query = "DELETE FROM DepartmentResearchAreas WHERE department_id = %s AND area_id = %s"
    return db_connector.execute_query(query, (department_id, area_id))

# --- Student Logic ---
def add_student(data):
    """Adds a new student."""
    query = """
        INSERT INTO Students (first_name, last_name, dob, phone_number, student_email, program_id, year_of_study, graduation_status)
        VALUES (%(first_name)s, %(last_name)s, %(dob)s, %(phone_number)s, %(student_email)s, %(program_id)s, %(year_of_study)s, %(graduation_status)s)
    """
    return db_connector.execute_query(query, data)

def update_student(data):
    """Updates an existing student."""
    query = """
        UPDATE Students SET first_name=%(first_name)s, last_name=%(last_name)s, dob=%(dob)s,
        phone_number=%(phone_number)s, student_email=%(student_email)s, program_id=%(program_id)s,
        year_of_study=%(year_of_study)s, graduation_status=%(graduation_status)s WHERE student_id=%(student_id)s
    """
    return db_connector.execute_query(query, data)

def search_students(last_name, program_id):
    """Searches for students with optional criteria."""
    query = """
        SELECT s.student_id, s.first_name, s.last_name, p.name as program, s.year_of_study, s.graduation_status
        FROM Students s
        LEFT JOIN Programs p ON s.program_id = p.program_id
        WHERE 1=1
    """
    params = []
    if last_name:
        query += " AND s.last_name LIKE %s"
        params.append(f"%{last_name}%")
    if program_id:
        query += " AND s.program_id = %s"
        params.append(program_id)
    return db_connector.execute_query(query, tuple(params), fetch='all')

# --- Student Enrollment, Grades, Disciplinary ---
def get_student_enrollments(student_id):
    """Gets all enrollments for a student, including grade."""
    query = """
        SELECT e.enrollment_id, c.course_code, c.name, co.year, co.semester, g.grade_percentage
        FROM Enrollment e
        JOIN CourseOfferings co ON e.offering_id = co.offering_id
        JOIN Courses c ON co.course_id = c.course_id
        LEFT JOIN Grades g ON e.enrollment_id = g.enrollment_id
        WHERE e.student_id = %s
        ORDER BY co.year DESC, co.semester DESC
    """
    return db_connector.execute_query(query, (student_id,), fetch='all')

def enroll_student_in_course(student_id, offering_id):
    """Enrolls a student in a course offering."""
    query = "INSERT INTO Enrollment (student_id, offering_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (student_id, offering_id))

def add_or_update_grade(enrollment_id, grade):
    """Adds or updates a grade for an enrollment."""
    # Check if a grade already exists
    check_query = "SELECT grade_id FROM Grades WHERE enrollment_id = %s"
    existing = db_connector.execute_query(check_query, (enrollment_id,), fetch='one')
    if existing:
        query = "UPDATE Grades SET grade_percentage = %s WHERE enrollment_id = %s"
        params = (grade, enrollment_id)
    else:
        query = "INSERT INTO Grades (enrollment_id, grade_percentage) VALUES (%s, %s)"
        params = (enrollment_id, grade)
    return db_connector.execute_query(query, params)

def get_student_disciplinary_records(student_id):
    """Gets all disciplinary records for a student."""
    query = "SELECT record_id, description FROM DisciplinaryRecords WHERE student_id = %s"
    return db_connector.execute_query(query, (student_id,), fetch='all')

def add_disciplinary_record(data):
    """Adds a new disciplinary record."""
    query = "INSERT INTO DisciplinaryRecords (student_id, description) VALUES (%(student_id)s, %(description)s)"
    return db_connector.execute_query(query, data)

# --- Lecturer Logic ---
def add_lecturer(data):
    """Adds a new lecturer."""
    query = """
        INSERT INTO Lecturers (first_name, last_name, department_id, phone_number, work_email)
        VALUES (%(first_name)s, %(last_name)s, %(department_id)s, %(phone_number)s, %(work_email)s)
    """
    return db_connector.execute_query(query, data)

def update_lecturer(data):
    """Updates an existing lecturer."""
    query = """
        UPDATE Lecturers SET first_name=%(first_name)s, last_name=%(last_name)s, 
        department_id=%(department_id)s, phone_number=%(phone_number)s, work_email=%(work_email)s 
        WHERE lecturer_id=%(lecturer_id)s
    """
    return db_connector.execute_query(query, data)

def search_lecturers(last_name, department_id):
    """Searches for lecturers with optional criteria."""
    query = """
        SELECT l.lecturer_id, l.first_name, l.last_name, l.work_email, d.name as department
        FROM Lecturers l
        LEFT JOIN Departments d ON l.department_id = d.department_id
        WHERE 1=1
    """
    params = []
    if last_name:
        query += " AND l.last_name LIKE %s"
        params.append(f"%{last_name}%")
    if department_id:
        query += " AND l.department_id = %s"
        params.append(department_id)
    return db_connector.execute_query(query, tuple(params), fetch='all')

# --- Lecturer Research Area Logic ---
def get_lecturer_research_areas(lecturer_id):
    """Gets all research areas for a given lecturer."""
    query = """
        SELECT ra.area_id, ra.name FROM ResearchAreas ra
        JOIN LecturerResearchAreas lra ON ra.area_id = lra.area_id
        WHERE lra.lecturer_id = %s
    """
    return db_connector.execute_query(query, (lecturer_id,), fetch='all')

def add_lecturer_to_area(lecturer_id, area_id):
    """Adds a research area to a lecturer."""
    query = "INSERT INTO LecturerResearchAreas (lecturer_id, area_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (lecturer_id, area_id))

def remove_lecturer_from_area(lecturer_id, area_id):
    """Removes a research area from a lecturer."""
    query = "DELETE FROM LecturerResearchAreas WHERE lecturer_id = %s AND area_id = %s"
    return db_connector.execute_query(query, (lecturer_id, area_id))

# --- Course Logic ---
def add_course(data):
    """Adds a new course."""
    query = """
        INSERT INTO Courses (course_code, name, description, department_id, credits, level)
        VALUES (%(course_code)s, %(name)s, %(description)s, %(department_id)s, %(credits)s, %(level)s)
    """
    return db_connector.execute_query(query, data)

def update_course(data):
    """Updates an existing course."""
    query = """
        UPDATE Courses SET course_code=%(course_code)s, name=%(name)s, description=%(description)s, 
        department_id=%(department_id)s, credits=%(credits)s, level=%(level)s 
        WHERE course_id=%(course_id)s
    """
    return db_connector.execute_query(query, data)

def search_courses(name, department_id):
    """Searches for courses with optional criteria."""
    query = """
        SELECT c.course_id, c.course_code, c.name, d.name as department, c.credits, c.level
        FROM Courses c
        LEFT JOIN Departments d ON c.department_id = d.department_id
        WHERE 1=1
    """
    params = []
    if name:
        query += " AND c.name LIKE %s"
        params.append(f"%{name}%")
    if department_id:
        query += " AND c.department_id = %s"
        params.append(department_id)
    return db_connector.execute_query(query, tuple(params), fetch='all')

# --- Course Prerequisites Logic ---
def get_prerequisites_for_course(course_id):
    """Gets all prerequisite courses for a given course."""
    query = """
        SELECT c.course_id, c.course_code, c.name
        FROM Courses c
        JOIN CoursePrerequisites cp ON c.course_id = cp.prerequisite_id
        WHERE cp.course_id = %s
    """
    return db_connector.execute_query(query, (course_id,), fetch='all')

def add_prerequisite_to_course(course_id, prerequisite_id):
    """Adds a prerequisite to a course."""
    query = "INSERT INTO CoursePrerequisites (course_id, prerequisite_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (course_id, prerequisite_id))

def remove_prerequisite_from_course(course_id, prerequisite_id):
    """Removes a prerequisite from a course."""
    query = "DELETE FROM CoursePrerequisites WHERE course_id = %s AND prerequisite_id = %s"
    return db_connector.execute_query(query, (course_id, prerequisite_id))

# --- Course Materials Logic ---
def get_course_materials(offering_id):
    """Gets all materials for a given course offering."""
    query = "SELECT material_id, material_details, material_type FROM CourseMaterials WHERE offering_id = %s"
    return db_connector.execute_query(query, (offering_id,), fetch='all')

def add_course_material(data):
    """Adds a new material to a course offering."""
    query = "INSERT INTO CourseMaterials (offering_id, material_details, material_type) VALUES (%(offering_id)s, %(material_details)s, %(material_type)s)"
    return db_connector.execute_query(query, data)

def update_course_material(data):
    """Updates a course material."""
    query = "UPDATE CourseMaterials SET material_details=%(material_details)s, material_type=%(material_type)s WHERE material_id=%(material_id)s"
    return db_connector.execute_query(query, data)

# --- Course Offerings Logic ---
def search_course_offerings(course_id, year):
    """Searches for course offerings."""
    query = """
        SELECT co.offering_id, c.course_code, c.name, co.year, co.semester, CONCAT(l.first_name, ' ', l.last_name) as lecturer
        FROM CourseOfferings co
        JOIN Courses c ON co.course_id = c.course_id
        JOIN Lecturers l ON co.lecturer_id = l.lecturer_id
        WHERE 1=1
    """
    params = []
    if course_id:
        query += " AND co.course_id = %s"
        params.append(course_id)
    if year:
        query += " AND co.year = %s"
        params.append(year)
    query += " ORDER BY co.year DESC, c.course_code"
    return db_connector.execute_query(query, tuple(params), fetch='all')

def add_course_offering(data):
    """Adds a new course offering."""
    query = "INSERT INTO CourseOfferings (course_id, lecturer_id, year, semester) VALUES (%(course_id)s, %(lecturer_id)s, %(year)s, %(semester)s)"
    return db_connector.execute_query(query, data)

def update_course_offering(data):
    """Updates a course offering."""
    query = "UPDATE CourseOfferings SET course_id=%(course_id)s, lecturer_id=%(lecturer_id)s, year=%(year)s, semester=%(semester)s WHERE offering_id=%(offering_id)s"
    return db_connector.execute_query(query, data)

# --- Program Requirements Logic ---
def get_program_requirements(program_id):
    """Gets all required courses for a given program."""
    query = """
        SELECT c.course_id, c.course_code, c.name
        FROM Courses c
        JOIN ProgramRequirements pr ON c.course_id = pr.course_id
        WHERE pr.program_id = %s
    """
    return db_connector.execute_query(query, (program_id,), fetch='all')

def add_course_to_program(program_id, course_id):
    """Adds a course requirement to a program."""
    query = "INSERT INTO ProgramRequirements (program_id, course_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (program_id, course_id))

def remove_course_from_program(program_id, course_id):
    """Removes a course requirement from a program."""
    query = "DELETE FROM ProgramRequirements WHERE program_id = %s AND course_id = %s"
    return db_connector.execute_query(query, (program_id, course_id))

# --- NonAcademicStaff Logic ---
def add_staff(data):
    """Adds a new non-academic staff member."""
    query = """
        INSERT INTO NonAcademicStaff (first_name, last_name, job_title, department_id, phone_number, work_email)
        VALUES (%(first_name)s, %(last_name)s, %(job_title)s, %(department_id)s, %(phone_number)s, %(work_email)s)
    """
    return db_connector.execute_query(query, data)

def update_staff(data):
    """Updates an existing non-academic staff member."""
    query = """
        UPDATE NonAcademicStaff SET first_name=%(first_name)s, last_name=%(last_name)s, job_title=%(job_title)s,
        department_id=%(department_id)s, phone_number=%(phone_number)s, work_email=%(work_email)s
        WHERE staff_id=%(staff_id)s
    """
    return db_connector.execute_query(query, data)

def search_staff(last_name, department_id):
    """Searches for non-academic staff."""
    query = """
        SELECT s.staff_id, s.first_name, s.last_name, s.job_title, d.name as department
        FROM NonAcademicStaff s
        LEFT JOIN Departments d ON s.department_id = d.department_id
        WHERE 1=1
    """
    params = []
    if last_name:
        query += " AND s.last_name LIKE %s"
        params.append(f"%{last_name}%")
    if department_id:
        query += " AND s.department_id = %s"
        params.append(department_id)
    return db_connector.execute_query(query, tuple(params), fetch='all')

# --- Staff Contracts & Emergency Contacts ---
def get_staff_contracts(staff_id):
    """Gets all contracts for a staff member."""
    query = "SELECT contract_id, employment_type, salary, start_date, end_date FROM StaffContracts WHERE staff_id = %s"
    return db_connector.execute_query(query, (staff_id,), fetch='all')

def add_contract(data):
    """Adds a new contract."""
    query = "INSERT INTO StaffContracts (staff_id, employment_type, salary, start_date, end_date) VALUES (%(staff_id)s, %(employment_type)s, %(salary)s, %(start_date)s, %(end_date)s)"
    return db_connector.execute_query(query, data)

def update_contract(data):
    """Updates a contract."""
    query = "UPDATE StaffContracts SET employment_type=%(employment_type)s, salary=%(salary)s, start_date=%(start_date)s, end_date=%(end_date)s WHERE contract_id=%(contract_id)s"
    return db_connector.execute_query(query, data)

def get_staff_emergency_contacts(staff_id):
    """Gets all emergency contacts for a staff member."""
    query = "SELECT contact_id, name, relationship, phone_number FROM EmergencyContacts WHERE staff_id = %s"
    return db_connector.execute_query(query, (staff_id,), fetch='all')

def add_emergency_contact(data):
    """Adds a new emergency contact."""
    query = "INSERT INTO EmergencyContacts (staff_id, name, relationship, phone_number) VALUES (%(staff_id)s, %(name)s, %(relationship)s, %(phone_number)s)"
    return db_connector.execute_query(query, data)

def update_emergency_contact(data):
    """Updates an emergency contact."""
    query = "UPDATE EmergencyContacts SET name=%(name)s, relationship=%(relationship)s, phone_number=%(phone_number)s WHERE contact_id=%(contact_id)s"
    return db_connector.execute_query(query, data)

# --- ResearchProject Logic ---
def add_project(data):
    """Adds a new research project."""
    query = """
        INSERT INTO ResearchProjects (title, funding_source, outcome_summary, principal_investigator_id)
        VALUES (%(title)s, %(funding_source)s, %(outcome_summary)s, %(principal_investigator_id)s)
    """
    return db_connector.execute_query(query, data)

def update_project(data):
    """Updates a research project."""
    query = """
        UPDATE ResearchProjects SET title=%(title)s, funding_source=%(funding_source)s,
        outcome_summary=%(outcome_summary)s, principal_investigator_id=%(principal_investigator_id)s
        WHERE project_id=%(project_id)s
    """
    return db_connector.execute_query(query, data)

def search_projects(title, pi_id):
    """Searches for research projects."""
    query = """
        SELECT p.project_id, p.title, p.funding_source, 
               CONCAT(l.first_name, ' ', l.last_name) as principal_investigator
        FROM ResearchProjects p
        LEFT JOIN Lecturers l ON p.principal_investigator_id = l.lecturer_id
        WHERE 1=1
    """
    params = []
    if title:
        query += " AND p.title LIKE %s"
        params.append(f"%{title}%")
    if pi_id:
        query += " AND p.principal_investigator_id = %s"
        params.append(pi_id)
    return db_connector.execute_query(query, tuple(params), fetch='all')

def get_project_members(project_id):
    """Gets all student members for a given project."""
    query = """
        SELECT s.student_id, s.first_name, s.last_name FROM Students s
        JOIN ProjectMembers pm ON s.student_id = pm.student_id
        WHERE pm.project_id = %s
    """
    return db_connector.execute_query(query, (project_id,), fetch='all')

def add_student_to_project(project_id, student_id):
    """Adds a student to a project."""
    query = "INSERT INTO ProjectMembers (project_id, student_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (project_id, student_id))

def remove_student_from_project(project_id, student_id):
    """Removes a student from a project."""
    query = "DELETE FROM ProjectMembers WHERE project_id = %s AND student_id = %s"
    return db_connector.execute_query(query, (project_id, student_id))

# --- Publication Logic ---
def add_publication(data):
    """Adds a new publication."""
    query = "INSERT INTO Publications (title, year, publication_venue) VALUES (%(title)s, %(year)s, %(publication_venue)s)"
    return db_connector.execute_query(query, data)

def update_publication(data):
    """Updates a publication."""
    query = "UPDATE Publications SET title=%(title)s, year=%(year)s, publication_venue=%(publication_venue)s WHERE publication_id=%(publication_id)s"
    return db_connector.execute_query(query, data)

def search_publications(title, year):
    """Searches for publications."""
    query = "SELECT publication_id, title, year, publication_venue FROM Publications WHERE 1=1"
    params = []
    if title:
        query += " AND title LIKE %s"
        params.append(f"%{title}%")
    if year:
        query += " AND year = %s"
        params.append(year)
    return db_connector.execute_query(query, tuple(params), fetch='all')

# --- Student Organization Logic ---
def add_organization(data):
    """Adds a new student organization."""
    query = "INSERT INTO StudentOrganizations (name, description) VALUES (%(name)s, %(description)s)"
    return db_connector.execute_query(query, data)

def update_organization(data):
    """Updates a student organization."""
    query = "UPDATE StudentOrganizations SET name=%(name)s, description=%(description)s WHERE organization_id=%(organization_id)s"
    return db_connector.execute_query(query, data)
def get_organization_members(org_id):
    """Gets all student members for a given organization."""
    query = """
        SELECT s.student_id, s.first_name, s.last_name FROM Students s
        JOIN OrganizationMembers om ON s.student_id = om.student_id
        WHERE om.organization_id = %s
    """
    return db_connector.execute_query(query, (org_id,), fetch='all')

def add_student_to_organization(org_id, student_id):
    """Adds a student to an organization."""
    query = "INSERT INTO OrganizationMembers (organization_id, student_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (org_id, student_id))

def remove_student_from_organization(org_id, student_id):
    """Removes a student from an organization."""
    query = "DELETE FROM OrganizationMembers WHERE organization_id = %s AND student_id = %s"
    return db_connector.execute_query(query, (org_id, student_id))

# --- Committee Logic ---
def add_committee(data):
    """Adds a new committee."""
    query = "INSERT INTO Committees (name, description) VALUES (%(name)s, %(description)s)"
    return db_connector.execute_query(query, data)

def update_committee(data):
    """Updates a committee."""
    query = "UPDATE Committees SET name=%(name)s, description=%(description)s WHERE committee_id=%(committee_id)s"
    return db_connector.execute_query(query, data)

def search_committees(name):
    """Searches for committees."""
    query = "SELECT committee_id, name, description FROM Committees WHERE 1=1"
    params = []
    if name:
        query += " AND name LIKE %s"
        params.append(f"%{name}%")
    query += " ORDER BY name"
    return db_connector.execute_query(query, tuple(params), fetch='all')

def get_committee_members(committee_id):
    """Gets all lecturer members for a given committee."""
    query = """
        SELECT l.lecturer_id, l.first_name, l.last_name FROM Lecturers l
        JOIN CommitteeMembers cm ON l.lecturer_id = cm.lecturer_id
        WHERE cm.committee_id = %s
    """
    return db_connector.execute_query(query, (committee_id,), fetch='all')

def add_lecturer_to_committee(committee_id, lecturer_id):
    """Adds a lecturer to a committee."""
    query = "INSERT INTO CommitteeMembers (committee_id, lecturer_id) VALUES (%s, %s)"
    return db_connector.execute_query(query, (committee_id, lecturer_id))

def remove_lecturer_from_committee(committee_id, lecturer_id):
    """Removes a lecturer from a committee."""
    query = "DELETE FROM CommitteeMembers WHERE committee_id = %s AND lecturer_id = %s"
    return db_connector.execute_query(query, (committee_id, lecturer_id))

# --- Research Area Logic ---
def add_research_area(data):
    """Adds a new research area."""
    query = "INSERT INTO ResearchAreas (name) VALUES (%(name)s)"
    return db_connector.execute_query(query, data)

def update_research_area(data):
    """Updates a research area."""
    query = "UPDATE ResearchAreas SET name=%(name)s WHERE area_id=%(area_id)s"
    return db_connector.execute_query(query, data)

def search_research_areas(name):
    """Searches for research areas."""
    query = "SELECT area_id, name FROM ResearchAreas WHERE 1=1"
    params = []
    if name:
        query += " AND name LIKE %s"
        params.append(f"%{name}%")
    query += " ORDER BY name"
    return db_connector.execute_query(query, tuple(params), fetch='all')

# --- Advising History Logic ---
def search_advising_history(student_id):
    """Searches for advising history records."""
    query = """
        SELECT CONCAT(s.first_name, ' ', s.last_name) as student,
               CONCAT(l.first_name, ' ', l.last_name) as lecturer,
               ah.start_date, ah.end_date,
               ah.student_id, ah.lecturer_id
        FROM AdvisingHistory ah
        JOIN Students s ON ah.student_id = s.student_id
        JOIN Lecturers l ON ah.lecturer_id = l.lecturer_id
        WHERE 1=1
    """
    params = []
    if student_id:
        query += " AND ah.student_id = %s"
        params.append(student_id)
    query += " ORDER BY ah.start_date DESC"
    return db_connector.execute_query(query, tuple(params), fetch='all')

def add_advising_record(data):
    """Adds a new advising record."""
    query = "INSERT INTO AdvisingHistory (student_id, lecturer_id, start_date, end_date) VALUES (%(student_id)s, %(lecturer_id)s, %(start_date)s, %(end_date)s)"
    return db_connector.execute_query(query, data)

def update_advising_record(data):
    """Updates an advising record's end_date."""
    query = "UPDATE AdvisingHistory SET end_date=%(end_date)s WHERE student_id=%(student_id)s AND lecturer_id=%(lecturer_id)s AND start_date=%(start_date)s"
    return db_connector.execute_query(query, data)

def delete_advising_record(student_id, lecturer_id, start_date):
    """Deletes an advising record."""
    query = "DELETE FROM AdvisingHistory WHERE student_id=%s AND lecturer_id=%s AND start_date=%s"
    return db_connector.execute_query(query, (student_id, lecturer_id, start_date))

# --- Advanced Queries ---
def find_students_in_course_by_lecturer(course_id, lecturer_id):
    """Finds students in a specific course taught by a specific lecturer."""
    query = """
        SELECT s.first_name, s.last_name, s.student_email, c.name AS course_name
        FROM Students s
        JOIN Enrollment e ON s.student_id = e.student_id
        JOIN CourseOfferings co ON e.offering_id = co.offering_id
        JOIN Courses c ON co.course_id = c.course_id
        WHERE co.course_id = %s AND co.lecturer_id = %s;
    """
    return db_connector.execute_query(query, (course_id, lecturer_id), fetch='all')

def find_high_achieving_final_year_students(min_grade):
    """Lists final-year students with an average grade above a certain percentage."""
    query = """
        SELECT s.first_name, s.last_name, p.name AS program, FORMAT(AVG(g.grade_percentage), 2) AS avg_grade
        FROM Students s
        JOIN Programs p ON s.program_id = p.program_id
        JOIN Enrollment e ON s.student_id = e.student_id
        JOIN Grades g ON e.enrollment_id = g.enrollment_id
        WHERE s.year_of_study = p.duration_years
        GROUP BY s.student_id, s.first_name, s.last_name, p.name
        HAVING AVG(g.grade_percentage) > %s;
    """
    return db_connector.execute_query(query, (min_grade,), fetch='all')

def find_unregistered_students(year, semester):
    """Finds students not registered for any courses in a given semester."""
    query = """
        SELECT s.student_id, s.first_name, s.last_name, s.student_email
        FROM Students s
        LEFT JOIN (
            SELECT DISTINCT e.student_id
            FROM Enrollment e
            JOIN CourseOfferings co ON e.offering_id = co.offering_id
            WHERE co.year = %s AND co.semester = %s
        ) AS registered_students ON s.student_id = registered_students.student_id
        WHERE registered_students.student_id IS NULL;
    """
    return db_connector.execute_query(query, (year, semester), fetch='all')

def find_advisor_for_student(student_id):
    """Retrieves the current advisor for a specific student."""
    query = """
        SELECT l.first_name, l.last_name, l.work_email
        FROM Lecturers l
        JOIN AdvisingHistory ah ON l.lecturer_id = ah.lecturer_id
        WHERE ah.student_id = %s AND ah.end_date IS NULL;
    """
    return db_connector.execute_query(query, (student_id,), fetch='all')

def find_lecturers_by_expertise(area_id):
    """Searches for lecturers by their research area."""
    query = """
        SELECT l.first_name, l.last_name, l.work_email
        FROM Lecturers l
        JOIN LecturerResearchAreas lra ON l.lecturer_id = lra.lecturer_id
        WHERE lra.area_id = %s;
    """
    return db_connector.execute_query(query, (area_id,), fetch='all')

def find_courses_by_department_lecturer(department_id):
    """Lists all courses taught by lecturers from a specific department."""
    query = """
        SELECT DISTINCT c.course_code, c.name AS course_name
        FROM Courses c
        JOIN CourseOfferings co ON c.course_id = co.course_id
        JOIN Lecturers l ON co.lecturer_id = l.lecturer_id
        WHERE l.department_id = %s ORDER BY c.course_code;
    """
    return db_connector.execute_query(query, (department_id,), fetch='all')

def find_top_project_supervisor():
    """Identifies the lecturer supervising the most students on research projects."""
    query = """
        SELECT l.first_name, l.last_name, COUNT(pm.student_id) AS students_supervised
        FROM Lecturers l
        JOIN ResearchProjects rp ON l.lecturer_id = rp.principal_investigator_id
        JOIN ProjectMembers pm ON rp.project_id = pm.project_id
        GROUP BY l.lecturer_id, l.first_name, l.last_name
        ORDER BY students_supervised DESC LIMIT 1;
    """
    return db_connector.execute_query(query, fetch='one')

def find_recent_publications():
    """Generates a report of publications from the past year."""
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
    return db_connector.execute_query(query, fetch='all')

def find_students_by_advisor(lecturer_id):
    """Finds all students currently advised by a specific lecturer."""
    query = """
        SELECT s.first_name, s.last_name, s.student_email
        FROM Students s
        JOIN AdvisingHistory ah ON s.student_id = ah.student_id
        WHERE ah.lecturer_id = %s AND ah.end_date IS NULL;
    """
    return db_connector.execute_query(query, (lecturer_id,), fetch='all')

def find_staff_by_department(department_id):
    """Finds all staff (lecturers and non-academic) in a specific department."""
    query = """
        (SELECT first_name, last_name, job_title
         FROM NonAcademicStaff
         WHERE department_id = %s)
        UNION
        (SELECT first_name, last_name, 'Lecturer' as job_title
         FROM Lecturers
         WHERE department_id = %s)
        ORDER BY last_name, first_name;
    """
    return db_connector.execute_query(query, (department_id, department_id), fetch='all')
