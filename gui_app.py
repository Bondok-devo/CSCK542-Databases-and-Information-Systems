# =================================================================
#  File: gui_app.py
#  Purpose: The main application file with the tkinter GUI.
# =================================================================
"""
This is the main entry point for the University Management System GUI application.
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import app_logic
import db_connector

class App(tk.Tk):
    """Main application class for the GUI."""

    def __init__(self):
        """Initializes the main application window."""
        super().__init__()
        self.title("University Record Management System")
        self.geometry("1600x950")

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("TNotebook.Tab", padding=[12, 5], font=('Helvetica', 10, 'bold'))
        style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

        # Initialize all instance attributes for widgets
        self.student_entries = {}
        self.student_id_var = tk.StringVar()
        self.lecturer_entries = {}
        self.lecturer_id_var = tk.StringVar()
        self.course_entries = {}
        self.course_id_var = tk.StringVar()
        self.staff_entries = {}
        self.staff_id_var = tk.StringVar()
        self.project_entries = {}
        self.project_id_var = tk.StringVar()
        self.pub_entries = {}
        self.pub_id_var = tk.StringVar()
        self.org_entries = {}
        self.org_id_var = tk.StringVar()
        self.dept_entries = {}
        self.dept_id_var = tk.StringVar()
        self.committee_entries = {}
        self.committee_id_var = tk.StringVar()
        self.program_id_var = tk.StringVar()
        self.research_area_entries = {}
        self.research_area_id_var = tk.StringVar()
        self.offering_entries = {}
        self.offering_id_var = tk.StringVar()
        self.advising_entries = {}
        self.selected_advising_key = {}

        # Attributes for widgets defined outside __init__ - initialize to None
        self.student_enroll_course = None
        self.student_enroll_tree = None
        self.disc_record_date = None
        self.disc_record_desc = None
        self.student_disciplinary_tree = None
        self.contract_id_var = tk.StringVar()
        self.contract_entries = {}
        self.staff_contracts_tree = None
        self.econtact_id_var = tk.StringVar()
        self.econtact_entries = {}
        self.staff_econtacts_tree = None
        self.material_id_var = tk.StringVar()
        self.material_entries = {}
        self.course_materials_tree = None
        self.course_prereq_add = None
        self.course_prereq_tree = None
        self.aq_tree = None
        self.q1_course = None
        self.q1_lecturer = None
        self.q1_lecturer_map = {}
        self.q2_min_grade = None
        self.q3_year = None
        self.q3_semester = None
        self.q4_student = None
        self.q5_area = None
        self.q6_dept = None
        self.q9_lecturer = None
        self.q10_dept = None


        self.load_all_dropdown_data()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)

        # Create all tabs
        self.create_departments_tab()
        self.create_research_areas_tab()
        self.create_programs_tab()
        self.create_students_tab()
        self.create_lecturers_tab()
        self.create_courses_tab()
        self.create_course_offerings_tab()
        self.create_advising_tab()
        self.create_staff_tab()
        self.create_committees_tab()
        self.create_projects_tab()
        self.create_publications_tab()
        self.create_organizations_tab()
        self.create_advanced_queries_tab()

    def load_all_dropdown_data(self):
        """Pre-loads or re-loads data for all comboboxes."""
        self.programs_list = app_logic.get_programs_list()
        self.departments_list = app_logic.get_departments_list()
        self.lecturers_list = app_logic.get_lecturers_list()
        self.students_list = app_logic.get_students_list()
        self.courses_list = app_logic.get_courses_list()
        self.course_offerings_list = app_logic.get_course_offerings_list()
        self.research_areas_list = app_logic.get_research_areas_list()

        self.program_map = {p['name']: p['program_id'] for p in self.programs_list}
        self.department_map = {d['name']: d['department_id'] for d in self.departments_list}
        self.lecturer_map = {l['name']: l['lecturer_id'] for l in self.lecturers_list}
        self.student_map = {s['name']: s['student_id'] for s in self.students_list}
        self.course_map = {c['name']: c['course_id'] for c in self.courses_list}
        self.research_area_map = {ra['name']: ra['area_id'] for ra in self.research_areas_list}
        self.course_offering_map = {
            co['name']: co['offering_id'] for co in self.course_offerings_list
        }

    def refresh_all_comboboxes(self):
        """Updates the values of all comboboxes in the application."""
        # Department dropdowns
        dept_names = [""] + list(self.department_map.keys())
        self.lecturer_search_dept['values'] = dept_names
        self.course_search_dept['values'] = dept_names
        self.staff_search_dept['values'] = dept_names
        self.lecturer_entries['department_id']['values'] = list(self.department_map.keys())
        self.course_entries['department_id']['values'] = list(self.department_map.keys())
        self.staff_entries['department_id']['values'] = list(self.department_map.keys())
        self.q6_dept['values'] = list(self.department_map.keys())
        self.q10_dept['values'] = list(self.department_map.keys())

        # Program dropdowns
        prog_names = [""] + list(self.program_map.keys())
        self.student_search_program['values'] = prog_names
        self.student_entries['program_id']['values'] = list(self.program_map.keys())

        # Lecturer dropdowns
        lecturer_names = [""] + list(self.lecturer_map.keys())
        self.project_search_pi['values'] = lecturer_names
        self.project_entries['principal_investigator_id']['values'] = list(self.lecturer_map.keys())
        self.committee_member_add['values'] = list(self.lecturer_map.keys())
        self.offering_entries['lecturer_id']['values'] = list(self.lecturer_map.keys())
        self.advising_entries['lecturer_id']['values'] = list(self.lecturer_map.keys())
        self.q9_lecturer['values'] = list(self.lecturer_map.keys())

        # Student dropdowns
        student_names = [""] + list(self.student_map.keys())
        self.project_member_student['values'] = list(self.student_map.keys())
        self.org_member_student['values'] = list(self.student_map.keys())
        self.advising_entries['student_id']['values'] = list(self.student_map.keys())
        self.advising_search_student['values'] = student_names
        self.q4_student['values'] = list(self.student_map.keys())

        # Course dropdowns
        course_names = [""] + list(self.course_map.keys())
        self.program_req_course['values'] = list(self.course_map.keys())
        self.course_prereq_add['values'] = list(self.course_map.keys())
        self.offering_entries['course_id']['values'] = list(self.course_map.keys())
        self.offering_search_course['values'] = course_names
        self.q1_course['values'] = list(self.course_map.keys())

        # Research Area dropdowns
        research_area_names = list(self.research_area_map.keys())
        self.dept_area_add['values'] = research_area_names
        self.lecturer_area_add['values'] = research_area_names
        self.q5_area['values'] = research_area_names

        # Course Offering dropdowns
        offering_names = list(self.course_offering_map.keys())
        self.student_enroll_course['values'] = offering_names

    def create_crud_tab(self, tab_name, fields):
        """Generic helper to create a simple CRUD tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text=tab_name)

        form_frame = ttk.LabelFrame(frame, text=f"{tab_name.split(' ')[-1]} Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)

        entries = {}
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(
                row=i, column=0, padx=5, pady=5, sticky="w")
            entry = ttk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            entries[field] = entry

        id_var = tk.StringVar()

        button_frame = ttk.Frame(frame)
        button_frame.pack(fill="x", padx=10, pady=5)

        search_frame = ttk.LabelFrame(frame, text=f"Search {tab_name.split(' ')[-1]}s", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)

        tree = self.create_results_treeview(frame)

        return entries, id_var, tree, search_frame, button_frame

    # =================================================================
    # DEPARTMENTS TAB
    # =================================================================
    def create_departments_tab(self):
        """Creates the 'Manage Departments' tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Departments")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=1)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=1)

        # Left side: Department CRUD
        dept_form_frame = ttk.LabelFrame(left_frame, text="Department Details", padding=10)
        dept_form_frame.pack(fill="x", pady=5)
        ttk.Label(dept_form_frame, text="Name:").grid(row=0, column=0, sticky="w")
        self.dept_entries['name'] = ttk.Entry(dept_form_frame, width=30)
        self.dept_entries['name'].grid(row=0, column=1, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_department).pack(side="left")
        ttk.Button(btn_frame, text="Update", command=self.update_department).pack(side="left")
        ttk.Button(btn_frame, text="Delete", command=self.delete_department).pack(side="left")
        ttk.Button(btn_frame, text="Clear", command=self.clear_department_form).pack(side="left")

        search_frame = ttk.LabelFrame(left_frame, text="Search Departments", padding="10")
        search_frame.pack(fill="x", pady=5)
        ttk.Label(search_frame, text="Name:").pack(side="left")
        self.dept_search_name = ttk.Entry(search_frame)
        self.dept_search_name.pack(side="left", fill="x", expand=True)
        ttk.Button(search_frame, text="Search", command=self.search_departments).pack(side="left")

        self.dept_tree = self.create_results_treeview(left_frame)
        self.dept_tree.bind("<<TreeviewSelect>>", self.on_department_select)

        # Right side: Department Research Areas
        area_frame = ttk.LabelFrame(right_frame, text="Manage Research Areas", padding="10")
        area_frame.pack(fill="both", expand=True)

        add_area_frame = ttk.Frame(area_frame)
        add_area_frame.pack(fill="x", pady=5)
        ttk.Label(add_area_frame, text="Area to Add:").pack(side="left")
        self.dept_area_add = ttk.Combobox(add_area_frame,
                                          values=list(self.research_area_map.keys()),
                                          state="readonly")
        self.dept_area_add.pack(side="left", fill="x", expand=True)
        ttk.Button(add_area_frame, text="Add", command=self.add_dept_area).pack(side="left")

        self.dept_area_tree = self.create_results_treeview(area_frame)
        ttk.Button(area_frame, text="Remove Selected Area",
                   command=self.remove_dept_area).pack(pady=5)

        self.search_departments()

    def add_department(self):
        """Adds a new department to the database."""
        data = {'name': self.dept_entries['name'].get()}
        if self.handle_add(data, app_logic.add_department, self.clear_department_form,
                           self.search_departments, "Department"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def update_department(self):
        """Updates the selected department in the database."""
        data = {'name': self.dept_entries['name'].get()}
        if self.handle_update(data, app_logic.update_department, self.dept_id_var,
                              "department_id", self.clear_department_form,
                              self.search_departments, "Department"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def delete_department(self):
        """Deletes the selected department from the database."""
        if self.handle_delete(self.dept_id_var, "Departments", "department_id",
                              self.clear_department_form, self.search_departments,
                              "Department"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def search_departments(self):
        """Searches for departments and displays them in the treeview."""
        self.display_in_treeview(self.dept_tree,
                                 app_logic.search_departments(self.dept_search_name.get()))
        self.clear_department_form()

    def on_department_select(self, _event):
        """Handles the selection of a department in the treeview."""
        self.handle_on_select(self.dept_tree, self.dept_id_var, self.dept_entries,
                              "Departments", "department_id", self.clear_department_form)
        self.refresh_department_areas()

    def clear_department_form(self):
        """Clears the department form."""
        self.clear_form(self.dept_id_var, self.dept_entries)
        self.refresh_department_areas()

    def refresh_department_areas(self):
        """Refreshes the research areas for the selected department."""
        dept_id = self.dept_id_var.get()
        if dept_id:
            areas = app_logic.get_department_research_areas(dept_id)
            self.display_in_treeview(self.dept_area_tree, areas)
        else:
            self.display_in_treeview(self.dept_area_tree, [])

    def add_dept_area(self):
        """Adds a research area to the selected department."""
        dept_id = self.dept_id_var.get()
        area_name = self.dept_area_add.get()
        if not dept_id or not area_name:
            messagebox.showerror("Error", "Select a department and a research area.")
            return
        area_id = self.research_area_map.get(area_name)
        if app_logic.add_area_to_department(dept_id, area_id):
            self.refresh_department_areas()
        else:
            messagebox.showerror("Error", "Failed to add area (already exists?).")

    def remove_dept_area(self):
        """Removes a research area from the selected department."""
        dept_id = self.dept_id_var.get()
        selected_item = self.dept_area_tree.focus()
        if not dept_id or not selected_item:
            messagebox.showerror("Error", "Select a department and an area to remove.")
            return
        area_id = self.dept_area_tree.item(selected_item)["values"][0]
        if app_logic.remove_area_from_department(dept_id, area_id):
            self.refresh_department_areas()
        else:
            messagebox.showerror("Error", "Failed to remove area.")

    # =================================================================
    # RESEARCH AREAS TAB
    # =================================================================
    def create_research_areas_tab(self):
        """Creates the 'Manage Research Areas' tab."""
        fields = ["name"]
        entries, id_var, tree, search_frame, btn_frame = self.create_crud_tab(
            "Manage Research Areas", fields
        )
        self.research_area_entries, self.research_area_id_var, self.research_area_tree = \
            entries, id_var, tree

        ttk.Label(search_frame, text="Name:").pack(side="left", padx=5)
        self.research_area_search_name = ttk.Entry(search_frame)
        self.research_area_search_name.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_research_areas).pack(
            side="left", padx=10
        )

        ttk.Button(btn_frame, text="Add", command=self.add_research_area).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_research_area).pack(
            side="left", padx=5
        )
        ttk.Button(btn_frame, text="Delete", command=self.delete_research_area).pack(
            side="left", padx=5
        )
        ttk.Button(btn_frame, text="Clear", command=self.clear_research_area_form).pack(
            side="left", padx=5
        )

        self.research_area_tree.bind("<<TreeviewSelect>>", self.on_research_area_select)
        self.search_research_areas()

    def add_research_area(self):
        """Adds a new research area to the database."""
        data = {'name': self.research_area_entries['name'].get()}
        if self.handle_add(data, app_logic.add_research_area, self.clear_research_area_form,
                           self.search_research_areas, "Research Area"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def update_research_area(self):
        """Updates the selected research area in the database."""
        data = {'name': self.research_area_entries['name'].get()}
        if self.handle_update(data, app_logic.update_research_area, self.research_area_id_var,
                              "area_id", self.clear_research_area_form,
                              self.search_research_areas, "Research Area"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def delete_research_area(self):
        """Deletes the selected research area from the database."""
        if self.handle_delete(self.research_area_id_var, "ResearchAreas", "area_id",
                              self.clear_research_area_form, self.search_research_areas,
                              "Research Area"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def search_research_areas(self):
        """Searches for research areas and displays them in the treeview."""
        self.display_in_treeview(self.research_area_tree,
                                 app_logic.search_research_areas(
                                     self.research_area_search_name.get()))

    def on_research_area_select(self, _event):
        """Handles the selection of a research area in the treeview."""
        self.handle_on_select(self.research_area_tree, self.research_area_id_var,
                              self.research_area_entries, "ResearchAreas", "area_id",
                              self.clear_research_area_form)

    def clear_research_area_form(self):
        """Clears the research area form."""
        self.clear_form(self.research_area_id_var, self.research_area_entries)

    # =================================================================
    # PROGRAMS TAB
    # =================================================================
    def create_programs_tab(self):
        """Creates the tab for managing program requirements."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Programs")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=1)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=2)

        # Left side: List of programs
        program_list_frame = ttk.LabelFrame(left_frame, text="Select a Program", padding=10)
        program_list_frame.pack(fill="both", expand=True)
        self.program_tree = self.create_results_treeview(program_list_frame)
        self.program_tree.bind("<<TreeviewSelect>>", self.on_program_select)
        self.search_programs()

        # Right side: Program requirements management
        req_frame = ttk.LabelFrame(right_frame, text="Manage Course Requirements", padding=10)
        req_frame.pack(fill="both", expand=True)

        add_req_frame = ttk.Frame(req_frame)
        add_req_frame.pack(fill="x", pady=5)
        ttk.Label(add_req_frame, text="Course to Add:").pack(side="left")
        self.program_req_course = ttk.Combobox(add_req_frame,
                                               values=list(self.course_map.keys()),
                                               state="readonly")
        self.program_req_course.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(add_req_frame, text="Add Requirement",
                   command=self.add_program_requirement).pack(side="left")

        self.program_req_tree = self.create_results_treeview(req_frame)
        ttk.Button(req_frame, text="Remove Selected Requirement",
                   command=self.remove_program_requirement).pack(pady=5)

    def search_programs(self):
        """Displays all programs in the treeview."""
        self.display_in_treeview(self.program_tree, self.programs_list)

    def on_program_select(self, _event):
        """Handles the selection of a program in the treeview."""
        selected_item = self.program_tree.focus()
        if not selected_item:
            return
        self.program_id_var.set(self.program_tree.item(selected_item)["values"][0])
        self.refresh_program_requirements()

    def refresh_program_requirements(self):
        """Refreshes the list of course requirements for the selected program."""
        program_id = self.program_id_var.get()
        if program_id:
            reqs = app_logic.get_program_requirements(program_id)
            self.display_in_treeview(self.program_req_tree, reqs)
        else:
            self.display_in_treeview(self.program_req_tree, [])

    def add_program_requirement(self):
        """Adds a course requirement to the selected program."""
        program_id = self.program_id_var.get()
        course_name = self.program_req_course.get()
        if not program_id:
            messagebox.showerror("Error", "Please select a program first.")
            return
        if not course_name:
            messagebox.showerror("Error", "Please select a course to add.")
            return
        course_id = self.course_map.get(course_name)
        if app_logic.add_course_to_program(program_id, course_id):
            messagebox.showinfo("Success", "Requirement added.")
            self.program_req_course.set('')
            self.refresh_program_requirements()
        else:
            messagebox.showerror("Error", "Failed to add requirement (it may already exist).")

    def remove_program_requirement(self):
        """Removes a course requirement from the selected program."""
        program_id = self.program_id_var.get()
        selected_item = self.program_req_tree.focus()
        if not program_id or not selected_item:
            messagebox.showerror("Error", "Select a program and a requirement to remove.")
            return
        course_id = self.program_req_tree.item(selected_item)["values"][0]
        if app_logic.remove_course_from_program(program_id, course_id):
            messagebox.showinfo("Success", "Requirement removed.")
            self.refresh_program_requirements()
        else:
            messagebox.showerror("Error", "Failed to remove requirement.")

    # =================================================================
    # STUDENTS TAB
    # =================================================================
    def create_students_tab(self):
        """Creates the 'Manage Students' tab with sub-tabs for details."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Students")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=2)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=3)

        # --- Left Side: Student Form and Search ---
        form_frame = ttk.LabelFrame(left_frame, text="Student Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)

        fields = ["first_name", "last_name", "dob", "phone_number", "student_email",
                  "program_id", "year_of_study", "graduation_status"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            if field == "program_id":
                self.student_entries[field] = ttk.Combobox(form_frame,
                                                           values=list(self.program_map.keys()),
                                                           state="readonly")
            elif field == "graduation_status":
                self.student_entries[field] = ttk.Combobox(form_frame,
                                                           values=["Enrolled", "Graduated",
                                                                   "Withdrawn"],
                                                           state="readonly")
            else:
                self.student_entries[field] = ttk.Entry(form_frame, width=30)
            self.student_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_student).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_student).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_student).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_student_form).pack(side="left",
                                                                                 padx=5)

        search_frame = ttk.LabelFrame(left_frame, text="Search Students", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Last Name:").pack(side="left", padx=5)
        self.student_search_ln = ttk.Entry(search_frame)
        self.student_search_ln.pack(side="left", padx=5)
        ttk.Label(search_frame, text="Program:").pack(side="left", padx=5)
        self.student_search_program = ttk.Combobox(search_frame,
                                                   values=[""] + list(self.program_map.keys()),
                                                   state="readonly")
        self.student_search_program.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_students).pack(side="left",
                                                                                   padx=10)

        self.student_tree = self.create_results_treeview(left_frame)
        self.student_tree.bind("<<TreeviewSelect>>", self.on_student_select)

        # --- Right Side: Sub-notebook for Grades, etc. ---
        self.student_details_notebook = ttk.Notebook(right_frame)
        self.student_details_notebook.pack(fill='both', expand=True)

        self.create_student_enrollment_tab()
        self.create_student_disciplinary_tab()

        self.search_students()

    def create_student_enrollment_tab(self):
        """Creates the sub-tab for student enrollments and grades."""
        frame = ttk.Frame(self.student_details_notebook, padding="10")
        self.student_details_notebook.add(frame, text="Enrollments & Grades")

        add_enroll_frame = ttk.Frame(frame)
        add_enroll_frame.pack(fill="x", pady=5)
        ttk.Label(add_enroll_frame, text="Enroll in Course Offering:").pack(side="left")
        self.student_enroll_course = ttk.Combobox(
            add_enroll_frame, values=list(self.course_offering_map.keys()), state="readonly"
        )
        self.student_enroll_course.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(add_enroll_frame, text="Enroll Student",
                   command=self.enroll_student).pack(side="left")

        self.student_enroll_tree = self.create_results_treeview(frame)
        ttk.Button(frame, text="Add/Update Grade for Selected",
                   command=self.add_update_grade).pack(pady=5)

    def create_student_disciplinary_tab(self):
        """Creates the sub-tab for student disciplinary records."""
        frame = ttk.Frame(self.student_details_notebook, padding="10")
        self.student_details_notebook.add(frame, text="Disciplinary Records")

        add_record_frame = ttk.LabelFrame(frame, text="New Record", padding=10)
        add_record_frame.pack(fill="x", pady=5)
        ttk.Label(add_record_frame, text="Description:").grid(row=1, column=0, sticky="w")
        self.disc_record_desc = ttk.Entry(add_record_frame)
        self.disc_record_desc.grid(row=1, column=1, sticky="ew")
        ttk.Button(add_record_frame, text="Add Record",
                   command=self.add_disciplinary_record).grid(row=2, columnspan=2, pady=5)

        self.student_disciplinary_tree = self.create_results_treeview(frame)
        ttk.Button(frame, text="Delete Selected Record",
                   command=self.delete_disciplinary_record).pack(pady=5)

    def add_student(self):
        """Adds a new student to the database."""
        data = {key: entry.get() for key, entry in self.student_entries.items()}
        data['program_id'] = self.program_map.get(data['program_id'])
        if self.handle_add(data, app_logic.add_student, self.clear_student_form,
                           self.search_students, "Student"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def update_student(self):
        """Updates the selected student in the database."""
        data = {key: entry.get() for key, entry in self.student_entries.items()}
        data['program_id'] = self.program_map.get(data['program_id'])
        self.handle_update(data, app_logic.update_student, self.student_id_var, "student_id",
                           self.clear_student_form, self.search_students, "Student")

    def delete_student(self):
        """Deletes the selected student from the database."""
        if self.handle_delete(self.student_id_var, "Students", "student_id",
                              self.clear_student_form, self.search_students, "Student"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def search_students(self):
        """Searches for students and displays them in the treeview."""
        program_name = self.student_search_program.get()
        program_id = self.program_map.get(program_name)
        self.display_in_treeview(self.student_tree,
                                 app_logic.search_students(self.student_search_ln.get(),
                                                           program_id))
        self.clear_student_form()

    def on_student_select(self, _event):
        """Handles the selection of a student in the treeview."""
        map_fields = {'program_id': {v: k for k, v in self.program_map.items()}}
        self.handle_on_select(self.student_tree, self.student_id_var, self.student_entries,
                              "Students", "student_id", self.clear_student_form, map_fields)
        self.refresh_student_details()

    def clear_student_form(self):
        """Clears the student form."""
        self.clear_form(self.student_id_var, self.student_entries)
        self.refresh_student_details()

    def refresh_student_details(self):
        """Refreshes the student's details in the sub-tabs."""
        student_id = self.student_id_var.get()
        if student_id:
            self.display_in_treeview(self.student_enroll_tree,
                                     app_logic.get_student_enrollments(student_id))
            self.display_in_treeview(self.student_disciplinary_tree,
                                     app_logic.get_student_disciplinary_records(student_id))
        else:
            self.display_in_treeview(self.student_enroll_tree, [])
            self.display_in_treeview(self.student_disciplinary_tree, [])

    def enroll_student(self):
        """Enrolls the selected student in a course offering."""
        student_id = self.student_id_var.get()
        offering_name = self.student_enroll_course.get()
        if not student_id or not offering_name:
            messagebox.showerror("Error", "Select a student and a course offering.")
            return
        offering_id = self.course_offering_map.get(offering_name)
        if app_logic.enroll_student_in_course(student_id, offering_id):
            messagebox.showinfo("Success", "Student enrolled.")
            self.student_enroll_course.set('')
            self.refresh_student_details()
        else:
            messagebox.showerror("Error", "Failed to enroll (already enrolled?).")

    def add_update_grade(self):
        """Adds or updates a grade for the selected enrollment."""
        selected_item = self.student_enroll_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Select an enrollment record.")
            return
        enrollment_id = self.student_enroll_tree.item(selected_item)['values'][0]

        grade = simpledialog.askstring("Input", "Enter Grade Percentage:", parent=self)
        if grade is not None:
            try:
                float(grade)  # validate
                if app_logic.add_or_update_grade(enrollment_id, grade):
                    messagebox.showinfo("Success", "Grade updated.")
                    self.refresh_student_details()
                else:
                    messagebox.showerror("Error", "Failed to update grade.")
            except (ValueError, TypeError):
                messagebox.showerror("Error", "Invalid grade. Please enter a number.")

    def add_disciplinary_record(self):
        """Adds a disciplinary record for the selected student."""
        student_id = self.student_id_var.get()
        if not student_id:
            messagebox.showerror("Error", "Please select a student first.")
            return
        data = {
            'student_id': student_id,
            'description': self.disc_record_desc.get()
        }
        if not data['description']:
            messagebox.showerror("Error", "Description is required.")
            return
        if app_logic.add_disciplinary_record(data):
            messagebox.showinfo("Success", "Record added.")
            self.disc_record_desc.delete(0, 'end')
            self.refresh_student_details()
        else:
            messagebox.showerror("Error", "Failed to add record.")

    def delete_disciplinary_record(self):
        """Deletes the selected disciplinary record."""
        selected_item = self.student_disciplinary_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "Select a record to delete.")
            return
        record_id = self.student_disciplinary_tree.item(selected_item)['values'][0]
        if messagebox.askyesno("Confirm", "Delete this disciplinary record?"):
            if app_logic.delete_record("DisciplinaryRecords", "record_id", record_id):
                messagebox.showinfo("Success", "Record deleted.")
                self.refresh_student_details()
            else:
                messagebox.showerror("Error", "Failed to delete record.")

    # =================================================================
    # LECTURERS TAB
    # =================================================================
    def create_lecturers_tab(self):
        """Creates the 'Manage Lecturers' tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Lecturers")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=1)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=1)

        # --- Left Side: Lecturer Form and Search ---
        form_frame = ttk.LabelFrame(left_frame, text="Lecturer Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)
        fields = ["first_name", "last_name", "department_id", "phone_number", "work_email"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            if field == "department_id":
                self.lecturer_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.department_map.keys()), state="readonly"
                )
            else:
                self.lecturer_entries[field] = ttk.Entry(form_frame, width=30)
            self.lecturer_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_lecturer).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_lecturer).pack(side="left",
                                                                                 padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_lecturer).pack(side="left",
                                                                                 padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_lecturer_form).pack(side="left",
                                                                                   padx=5)

        search_frame = ttk.LabelFrame(left_frame, text="Search Lecturers", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Last Name:").pack(side="left", padx=5)
        self.lecturer_search_ln = ttk.Entry(search_frame)
        self.lecturer_search_ln.pack(side="left", padx=5)
        ttk.Label(search_frame, text="Department:").pack(side="left", padx=5)
        self.lecturer_search_dept = ttk.Combobox(
            search_frame, values=[""] + list(self.department_map.keys()), state="readonly"
        )
        self.lecturer_search_dept.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_lecturers).pack(side="left",
                                                                                    padx=10)

        self.lecturer_tree = self.create_results_treeview(left_frame)
        self.lecturer_tree.bind("<<TreeviewSelect>>", self.on_lecturer_select)

        # --- Right Side: Research Area Management ---
        area_frame = ttk.LabelFrame(right_frame, text="Manage Research Areas", padding="10")
        area_frame.pack(fill="both", expand=True)

        add_area_frame = ttk.Frame(area_frame)
        add_area_frame.pack(fill="x", pady=5)
        ttk.Label(add_area_frame, text="Area to Add:").pack(side="left")
        self.lecturer_area_add = ttk.Combobox(add_area_frame,
                                              values=list(self.research_area_map.keys()),
                                              state="readonly")
        self.lecturer_area_add.pack(side="left", fill="x", expand=True)
        ttk.Button(add_area_frame, text="Add", command=self.add_lecturer_area).pack(side="left")

        self.lecturer_area_tree = self.create_results_treeview(area_frame)
        ttk.Button(area_frame, text="Remove Selected Area",
                   command=self.remove_lecturer_area).pack(pady=5)

        self.search_lecturers()

    def add_lecturer(self):
        """Adds a new lecturer to the database."""
        data = {key: entry.get() for key, entry in self.lecturer_entries.items()}
        data['department_id'] = self.department_map.get(data['department_id'])
        if self.handle_add(data, app_logic.add_lecturer, self.clear_lecturer_form,
                           self.search_lecturers, "Lecturer"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def update_lecturer(self):
        """Updates the selected lecturer in the database."""
        data = {key: entry.get() for key, entry in self.lecturer_entries.items()}
        data['department_id'] = self.department_map.get(data['department_id'])
        self.handle_update(data, app_logic.update_lecturer, self.lecturer_id_var, "lecturer_id",
                           self.clear_lecturer_form, self.search_lecturers, "Lecturer")

    def delete_lecturer(self):
        """Deletes the selected lecturer from the database."""
        if self.handle_delete(self.lecturer_id_var, "Lecturers", "lecturer_id",
                              self.clear_lecturer_form, self.search_lecturers, "Lecturer"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def search_lecturers(self):
        """Searches for lecturers and displays them in the treeview."""
        dept_name = self.lecturer_search_dept.get()
        dept_id = self.department_map.get(dept_name)
        self.display_in_treeview(self.lecturer_tree,
                                 app_logic.search_lecturers(self.lecturer_search_ln.get(),
                                                            dept_id))
        self.clear_lecturer_form()

    def on_lecturer_select(self, _event):
        """Handles the selection of a lecturer in the treeview."""
        map_fields = {'department_id': {v: k for k, v in self.department_map.items()}}
        self.handle_on_select(self.lecturer_tree, self.lecturer_id_var, self.lecturer_entries,
                              "Lecturers", "lecturer_id", self.clear_lecturer_form, map_fields)
        self.refresh_lecturer_areas()

    def clear_lecturer_form(self):
        """Clears the lecturer form."""
        self.clear_form(self.lecturer_id_var, self.lecturer_entries)
        self.refresh_lecturer_areas()

    def refresh_lecturer_areas(self):
        """Refreshes the research areas for the selected lecturer."""
        lecturer_id = self.lecturer_id_var.get()
        if lecturer_id:
            areas = app_logic.get_lecturer_research_areas(lecturer_id)
            self.display_in_treeview(self.lecturer_area_tree, areas)
        else:
            self.display_in_treeview(self.lecturer_area_tree, [])

    def add_lecturer_area(self):
        """Adds a research area to the selected lecturer."""
        lecturer_id = self.lecturer_id_var.get()
        area_name = self.lecturer_area_add.get()
        if not lecturer_id or not area_name:
            messagebox.showerror("Error", "Select a lecturer and a research area.")
            return
        area_id = self.research_area_map.get(area_name)
        if app_logic.add_lecturer_to_area(lecturer_id, area_id):
            self.refresh_lecturer_areas()
        else:
            messagebox.showerror("Error", "Failed to add area (already exists?).")

    def remove_lecturer_area(self):
        """Removes a research area from the selected lecturer."""
        lecturer_id = self.lecturer_id_var.get()
        selected_item = self.lecturer_area_tree.focus()
        if not lecturer_id or not selected_item:
            messagebox.showerror("Error", "Select a lecturer and an area to remove.")
            return
        area_id = self.lecturer_area_tree.item(selected_item)["values"][0]
        if app_logic.remove_lecturer_from_area(lecturer_id, area_id):
            self.refresh_lecturer_areas()
        else:
            messagebox.showerror("Error", "Failed to remove area.")

    # =================================================================
    # COURSES TAB
    # =================================================================
    def create_courses_tab(self):
        """Creates the 'Manage Courses' tab with prerequisites and materials."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Courses")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=2)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=2)

        # --- Left Side: Course Form and Search ---
        form_frame = ttk.LabelFrame(left_frame, text="Course Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)
        fields = ["course_code", "name", "description", "department_id", "credits", "level"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            if field == "department_id":
                self.course_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.department_map.keys()), state="readonly"
                )
            else:
                self.course_entries[field] = ttk.Entry(form_frame, width=40)
            self.course_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_course).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_course).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_course).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_course_form).pack(side="left",
                                                                                 padx=5)

        search_frame = ttk.LabelFrame(left_frame, text="Search Courses", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Name:").pack(side="left", padx=5)
        self.course_search_name = ttk.Entry(search_frame)
        self.course_search_name.pack(side="left", padx=5)
        ttk.Label(search_frame, text="Department:").pack(side="left", padx=5)
        self.course_search_dept = ttk.Combobox(
            search_frame, values=[""] + list(self.department_map.keys()), state="readonly"
        )
        self.course_search_dept.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_courses).pack(side="left",
                                                                                  padx=10)

        self.course_tree = self.create_results_treeview(left_frame)
        self.course_tree.bind("<<TreeviewSelect>>", self.on_course_select)

        # --- Right Side: Sub-notebook for Prerequisites and Materials ---
        self.course_details_notebook = ttk.Notebook(right_frame)
        self.course_details_notebook.pack(fill='both', expand=True)

        self.create_course_prerequisites_tab()

        self.search_courses()

    def create_course_prerequisites_tab(self):
        """Creates the sub-tab for course prerequisites."""
        prereq_frame = ttk.Frame(self.course_details_notebook, padding="10")
        self.course_details_notebook.add(prereq_frame, text="Prerequisites")

        add_prereq_frame = ttk.Frame(prereq_frame)
        add_prereq_frame.pack(fill="x", pady=5)
        ttk.Label(add_prereq_frame, text="Prerequisite:").pack(side="left")
        self.course_prereq_add = ttk.Combobox(
            add_prereq_frame, values=list(self.course_map.keys()), state="readonly"
        )
        self.course_prereq_add.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(add_prereq_frame, text="Add", command=self.add_prerequisite).pack(side="left")

        self.course_prereq_tree = self.create_results_treeview(prereq_frame)
        ttk.Button(prereq_frame, text="Remove Selected",
                   command=self.remove_prerequisite).pack(pady=5)

    def add_course(self):
        """Adds a new course to the database."""
        data = {key: entry.get() for key, entry in self.course_entries.items()}
        data['department_id'] = self.department_map.get(data['department_id'])
        if self.handle_add(data, app_logic.add_course, self.clear_course_form,
                           self.search_courses, "Course"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def update_course(self):
        """Updates the selected course in the database."""
        data = {key: entry.get() for key, entry in self.course_entries.items()}
        data['department_id'] = self.department_map.get(data['department_id'])
        self.handle_update(data, app_logic.update_course, self.course_id_var, "course_id",
                           self.clear_course_form, self.search_courses, "Course")

    def delete_course(self):
        """Deletes the selected course from the database."""
        if self.handle_delete(self.course_id_var, "Courses", "course_id",
                              self.clear_course_form, self.search_courses, "Course"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def search_courses(self):
        """Searches for courses and displays them in the treeview."""
        dept_name = self.course_search_dept.get()
        dept_id = self.department_map.get(dept_name)
        self.display_in_treeview(self.course_tree,
                                 app_logic.search_courses(self.course_search_name.get(),
                                                          dept_id))
        self.clear_course_form()

    def on_course_select(self, _event):
        """Handles the selection of a course in the treeview."""
        map_fields = {'department_id': {v: k for k, v in self.department_map.items()}}
        self.handle_on_select(self.course_tree, self.course_id_var, self.course_entries,
                              "Courses", "course_id", self.clear_course_form, map_fields)
        self.refresh_prerequisites()

    def clear_course_form(self):
        """Clears the course form."""
        self.clear_form(self.course_id_var, self.course_entries)
        self.refresh_prerequisites()

    def refresh_prerequisites(self):
        """Refreshes the list of prerequisites for the selected course."""
        course_id = self.course_id_var.get()
        if course_id:
            prereqs = app_logic.get_prerequisites_for_course(course_id)
            self.display_in_treeview(self.course_prereq_tree, prereqs)
        else:
            self.display_in_treeview(self.course_prereq_tree, [])

    def add_prerequisite(self):
        """Adds a prerequisite to the selected course."""
        course_id = self.course_id_var.get()
        prereq_name = self.course_prereq_add.get()
        if not course_id or not prereq_name:
            messagebox.showerror("Error", "Select a course and a prerequisite to add.")
            return
        prereq_id = self.course_map.get(prereq_name)
        if course_id == prereq_id:
            messagebox.showerror("Error", "A course cannot be a prerequisite of itself.")
            return
        if app_logic.add_prerequisite_to_course(course_id, prereq_id):
            self.refresh_prerequisites()
        else:
            messagebox.showerror("Error", "Failed to add prerequisite (it may already exist).")

    def remove_prerequisite(self):
        """Removes a prerequisite from the selected course."""
        course_id = self.course_id_var.get()
        selected_item = self.course_prereq_tree.focus()
        if not course_id or not selected_item:
            messagebox.showerror("Error", "Select a course and a prerequisite to remove.")
            return
        prereq_id = self.course_prereq_tree.item(selected_item)["values"][0]
        if app_logic.remove_prerequisite_from_course(course_id, prereq_id):
            self.refresh_prerequisites()
        else:
            messagebox.showerror("Error", "Failed to remove prerequisite.")

    # =================================================================
    # COURSE OFFERINGS TAB
    # =================================================================
    def create_course_offerings_tab(self):
        """Creates the 'Manage Course Offerings' tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Course Offerings")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=1)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=1)

        # --- Left Side: Offering Form and Search ---
        form_frame = ttk.LabelFrame(left_frame, text="Offering Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)

        fields = ["course_id", "lecturer_id", "year", "semester"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            if field == "course_id":
                self.offering_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.course_map.keys()), state="readonly"
                )
            elif field == "lecturer_id":
                self.offering_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.lecturer_map.keys()), state="readonly"
                )
            else:
                self.offering_entries[field] = ttk.Entry(form_frame, width=40)
            self.offering_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_offering).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_offering).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_offering).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_offering_form).pack(side="left",
                                                                                   padx=5)

        search_frame = ttk.LabelFrame(left_frame, text="Search Offerings", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Course:").pack(side="left", padx=5)
        self.offering_search_course = ttk.Combobox(
            search_frame, values=[""] + list(self.course_map.keys()), state="readonly"
        )
        self.offering_search_course.pack(side="left", padx=5)
        ttk.Label(search_frame, text="Year:").pack(side="left", padx=5)
        self.offering_search_year = ttk.Entry(search_frame)
        self.offering_search_year.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_offerings).pack(side="left",
                                                                                    padx=10)

        self.offering_tree = self.create_results_treeview(left_frame)
        self.offering_tree.bind("<<TreeviewSelect>>", self.on_offering_select)

        # --- Right Side: Course Materials ---
        self.create_course_materials_tab(right_frame)

        self.search_offerings()

    def create_course_materials_tab(self, parent_frame):
        """Creates the UI for managing course materials."""
        material_frame = ttk.LabelFrame(parent_frame, text="Manage Materials", padding=10)
        material_frame.pack(fill="both", expand=True)

        self.material_id_var = tk.StringVar()
        form = ttk.LabelFrame(material_frame, text="Material Details", padding=10)
        form.pack(fill="x", pady=5)
        fields = ["material_details", "material_type"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.material_entries[field] = ttk.Entry(form)
            self.material_entries[field].grid(row=i, column=1, sticky="ew", padx=5, pady=2)

        btn_frame = ttk.Frame(form)
        btn_frame.grid(row=len(fields), columnspan=2, pady=10)
        ttk.Button(btn_frame, text="Add New", command=self.add_material).pack(side="left")
        ttk.Button(btn_frame, text="Update Selected", command=self.update_material).pack(side="left")
        ttk.Button(btn_frame, text="Clear Form", command=self.clear_material_form).pack(side="left")

        self.course_materials_tree = self.create_results_treeview(material_frame)
        self.course_materials_tree.bind("<<TreeviewSelect>>", self.on_material_select)
        ttk.Button(material_frame, text="Delete Selected Material",
                   command=self.delete_material).pack(pady=5)

    def add_offering(self):
        """Adds a new course offering."""
        data = {k: e.get() for k, e in self.offering_entries.items()}
        data['course_id'] = self.course_map.get(data['course_id'])
        data['lecturer_id'] = self.lecturer_map.get(data['lecturer_id'])
        if self.handle_add(data, app_logic.add_course_offering, self.clear_offering_form,
                           self.search_offerings, "Offering"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def update_offering(self):
        """Updates the selected course offering."""
        data = {k: e.get() for k, e in self.offering_entries.items()}
        data['course_id'] = self.course_map.get(data['course_id'])
        data['lecturer_id'] = self.lecturer_map.get(data['lecturer_id'])
        self.handle_update(data, app_logic.update_course_offering, self.offering_id_var,
                           "offering_id", self.clear_offering_form,
                           self.search_offerings, "Offering")

    def delete_offering(self):
        """Deletes the selected course offering."""
        if self.handle_delete(self.offering_id_var, "CourseOfferings", "offering_id",
                              self.clear_offering_form, self.search_offerings, "Offering"):
            self.load_all_dropdown_data()
            self.refresh_all_comboboxes()

    def search_offerings(self):
        """Searches for course offerings."""
        course_name = self.offering_search_course.get()
        course_id = self.course_map.get(course_name)
        year = self.offering_search_year.get()
        self.display_in_treeview(self.offering_tree,
                                 app_logic.search_course_offerings(course_id, year))
        self.clear_offering_form()

    def on_offering_select(self, _event):
        """Handles the selection of a course offering."""
        map_fields = {
            'course_id': {v: k for k, v in self.course_map.items()},
            'lecturer_id': {v: k for k, v in self.lecturer_map.items()}
        }
        self.handle_on_select(self.offering_tree, self.offering_id_var, self.offering_entries,
                              "CourseOfferings", "offering_id", self.clear_offering_form,
                              map_fields)
        self.refresh_course_materials()

    def clear_offering_form(self):
        """Clears the course offering form."""
        self.clear_form(self.offering_id_var, self.offering_entries)
        self.refresh_course_materials()

    def refresh_course_materials(self):
        """Refreshes the course materials for the selected course offering."""
        offering_id = self.offering_id_var.get()
        if offering_id:
            materials = app_logic.get_course_materials(offering_id)
            self.display_in_treeview(self.course_materials_tree, materials)
        else:
            self.display_in_treeview(self.course_materials_tree, [])
        self.clear_material_form()

    def add_material(self):
        """Adds a new material for the selected course offering."""
        offering_id = self.offering_id_var.get()
        if not offering_id:
            messagebox.showerror("Error", "Select a course offering first.")
            return
        data = {k: e.get() for k, e in self.material_entries.items()}
        data['offering_id'] = offering_id
        if self.handle_add(data, app_logic.add_course_material, self.clear_material_form,
                           self.refresh_course_materials, "Material"):
            self.clear_material_form()

    def update_material(self):
        """Updates the selected material."""
        data = {k: e.get() for k, e in self.material_entries.items()}
        self.handle_update(data, app_logic.update_course_material, self.material_id_var,
                           "material_id", self.clear_material_form,
                           self.refresh_course_materials, "Material")

    def delete_material(self):
        """Deletes the selected material."""
        self.handle_delete(self.material_id_var, "CourseMaterials", "material_id",
                           self.clear_material_form, self.refresh_course_materials, "Material")

    def on_material_select(self, _event):
        """Handles the selection of a material in the treeview."""
        self.handle_on_select(self.course_materials_tree, self.material_id_var,
                              self.material_entries, "CourseMaterials", "material_id",
                              self.clear_material_form)

    def clear_material_form(self):
        """Clears the material form."""
        self.clear_form(self.material_id_var, self.material_entries)

    # =================================================================
    # ADVISING TAB
    # =================================================================
    def create_advising_tab(self):
        """Creates the 'Manage Advising' tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Advising")

        form_frame = ttk.LabelFrame(frame, text="Advising Record Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)

        fields = ["student_id", "lecturer_id", "start_date", "end_date"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            if field == "student_id":
                self.advising_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.student_map.keys()), state="readonly"
                )
            elif field == "lecturer_id":
                self.advising_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.lecturer_map.keys()), state="readonly"
                )
            else:
                self.advising_entries[field] = ttk.Entry(form_frame, width=40)
            self.advising_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_advising).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_advising).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_advising).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_advising_form).pack(side="left",
                                                                                   padx=5)

        search_frame = ttk.LabelFrame(frame, text="Search Records by Student", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Student:").pack(side="left", padx=5)
        self.advising_search_student = ttk.Combobox(
            search_frame, values=[""] + list(self.student_map.keys()), state="readonly"
        )
        self.advising_search_student.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(search_frame, text="Search", command=self.search_advising).pack(side="left",
                                                                                   padx=10)

        self.advising_tree = self.create_results_treeview(frame)
        self.advising_tree.bind("<<TreeviewSelect>>", self.on_advising_select)
        self.search_advising()

    def add_advising(self):
        """Adds a new advising record."""
        data = {k: e.get() for k, e in self.advising_entries.items()}
        data['student_id'] = self.student_map.get(data['student_id'])
        data['lecturer_id'] = self.lecturer_map.get(data['lecturer_id'])
        if data['end_date'] == '':
            data['end_date'] = None
        self.handle_add(data, app_logic.add_advising_record, self.clear_advising_form,
                        self.search_advising, "Advising Record")

    def update_advising(self):
        """Updates the selected advising record."""
        if not self.selected_advising_key:
            messagebox.showerror("Error", "No advising record selected.")
            return

        data = self.selected_advising_key.copy()
        end_date = self.advising_entries['end_date'].get()
        data['end_date'] = end_date if end_date else None

        if app_logic.update_advising_record(data):
            messagebox.showinfo("Success", "Advising record updated successfully.")
            self.clear_advising_form()
            self.search_advising()
        else:
            messagebox.showerror("Error", "Failed to update advising record.")

    def delete_advising(self):
        """Deletes the selected advising record."""
        if not self.selected_advising_key:
            messagebox.showerror("Error", "No advising record selected.")
            return

        if messagebox.askyesno("Confirm Delete", "Delete this advising record?"):
            if app_logic.delete_advising_record(**self.selected_advising_key):
                messagebox.showinfo("Success", "Advising record deleted.")
                self.clear_advising_form()
                self.search_advising()
            else:
                messagebox.showerror("Error", "Failed to delete advising record.")

    def search_advising(self):
        """Searches for advising records."""
        student_name = self.advising_search_student.get()
        student_id = self.student_map.get(student_name)
        self.display_in_treeview(self.advising_tree,
                                 app_logic.search_advising_history(student_id))
        self.clear_advising_form()

    def on_advising_select(self, _event):
        """Handles the selection of an advising record."""
        selected_item = self.advising_tree.focus()
        if not selected_item:
            return

        self.clear_advising_form()
        item = self.advising_tree.item(selected_item)
        values = item['values']

        # Manually find the keys from the treeview columns
        columns = self.advising_tree['columns']
        record = dict(zip(columns, values))

        # Populate form fields
        self.advising_entries['student_id'].set(record.get('student', ''))
        self.advising_entries['lecturer_id'].set(record.get('lecturer', ''))
        self.advising_entries['start_date'].insert(0, record.get('start_date', ''))
        self.advising_entries['end_date'].insert(0, record.get('end_date', ''))

        # Store the composite key for update/delete
        self.selected_advising_key = {
            'student_id': record.get('student_id'),
            'lecturer_id': record.get('lecturer_id'),
            'start_date': record.get('start_date')
        }

    def clear_advising_form(self):
        """Clears the advising record form."""
        self.selected_advising_key = {}
        for entry in self.advising_entries.values():
            if isinstance(entry, ttk.Combobox):
                entry.set('')
            else:
                entry.delete(0, "end")

    # =================================================================
    # STAFF TAB
    # =================================================================
    def create_staff_tab(self):
        """Creates the 'Manage Staff' tab with contracts and emergency contacts."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Staff")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=2)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=3)

        # --- Left Side: Staff Form and Search ---
        form_frame = ttk.LabelFrame(left_frame, text="Staff Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)
        fields = ["first_name", "last_name", "job_title", "department_id", "phone_number",
                  "work_email"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            if field == "department_id":
                self.staff_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.department_map.keys()), state="readonly"
                )
            else:
                self.staff_entries[field] = ttk.Entry(form_frame, width=30)
            self.staff_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_staff).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_staff).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_staff).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_staff_form).pack(side="left",
                                                                                padx=5)

        search_frame = ttk.LabelFrame(left_frame, text="Search Staff", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Last Name:").pack(side="left", padx=5)
        self.staff_search_ln = ttk.Entry(search_frame)
        self.staff_search_ln.pack(side="left", padx=5)
        ttk.Label(search_frame, text="Department:").pack(side="left", padx=5)
        self.staff_search_dept = ttk.Combobox(
            search_frame, values=[""] + list(self.department_map.keys()), state="readonly"
        )
        self.staff_search_dept.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_staff).pack(side="left",
                                                                                padx=10)

        self.staff_tree = self.create_results_treeview(left_frame)
        self.staff_tree.bind("<<TreeviewSelect>>", self.on_staff_select)

        # --- Right Side: Sub-notebook for Contracts, etc. ---
        self.staff_details_notebook = ttk.Notebook(right_frame)
        self.staff_details_notebook.pack(fill='both', expand=True)
        self.create_staff_contracts_tab()
        self.create_staff_emergency_contacts_tab()

        self.search_staff()

    def create_staff_contracts_tab(self):
        """Creates the sub-tab for staff contracts."""
        frame = ttk.Frame(self.staff_details_notebook, padding="10")
        self.staff_details_notebook.add(frame, text="Contracts")

        form = ttk.LabelFrame(frame, text="Contract Details", padding=10)
        form.pack(fill="x", pady=5)
        fields = ["employment_type", "salary", "start_date", "end_date"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.contract_entries[field] = ttk.Entry(form)
            self.contract_entries[field].grid(row=i, column=1, sticky="ew", padx=5, pady=2)

        btn_frame = ttk.Frame(form)
        btn_frame.grid(row=len(fields), columnspan=2, pady=10)
        ttk.Button(btn_frame, text="Add New", command=self.add_contract).pack(side="left")
        ttk.Button(btn_frame, text="Update Selected", command=self.update_contract).pack(side="left")
        ttk.Button(btn_frame, text="Clear Form", command=self.clear_contract_form).pack(side="left")

        self.staff_contracts_tree = self.create_results_treeview(frame)
        self.staff_contracts_tree.bind("<<TreeviewSelect>>", self.on_contract_select)
        ttk.Button(frame, text="Delete Selected Contract",
                   command=self.delete_contract).pack(pady=5)

    def create_staff_emergency_contacts_tab(self):
        """Creates the sub-tab for staff emergency contacts."""
        frame = ttk.Frame(self.staff_details_notebook, padding="10")
        self.staff_details_notebook.add(frame, text="Emergency Contacts")

        form = ttk.LabelFrame(frame, text="Emergency Contact Details", padding=10)
        form.pack(fill="x", pady=5)
        fields = ["name", "relationship", "phone_number"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form, text=label_text).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            self.econtact_entries[field] = ttk.Entry(form)
            self.econtact_entries[field].grid(row=i, column=1, sticky="ew", padx=5, pady=2)

        btn_frame = ttk.Frame(form)
        btn_frame.grid(row=len(fields), columnspan=2, pady=10)
        ttk.Button(btn_frame, text="Add New", command=self.add_econtact).pack(side="left")
        ttk.Button(btn_frame, text="Update Selected", command=self.update_econtact).pack(side="left")
        ttk.Button(btn_frame, text="Clear Form", command=self.clear_econtact_form).pack(side="left")

        self.staff_econtacts_tree = self.create_results_treeview(frame)
        self.staff_econtacts_tree.bind("<<TreeviewSelect>>", self.on_econtact_select)
        ttk.Button(frame, text="Delete Selected Contact",
                   command=self.delete_econtact).pack(pady=5)

    def add_staff(self):
        """Adds a new staff member to the database."""
        data = {key: entry.get() for key, entry in self.staff_entries.items()}
        data['department_id'] = self.department_map.get(data['department_id'])
        self.handle_add(data, app_logic.add_staff, self.clear_staff_form,
                        self.search_staff, "Staff")

    def update_staff(self):
        """Updates the selected staff member in the database."""
        data = {key: entry.get() for key, entry in self.staff_entries.items()}
        data['department_id'] = self.department_map.get(data['department_id'])
        self.handle_update(data, app_logic.update_staff, self.staff_id_var, "staff_id",
                           self.clear_staff_form, self.search_staff, "Staff")

    def delete_staff(self):
        """Deletes the selected staff member from the database."""
        self.handle_delete(self.staff_id_var, "NonAcademicStaff", "staff_id",
                           self.clear_staff_form, self.search_staff, "Staff")

    def search_staff(self):
        """Searches for staff members and displays them in the treeview."""
        dept_name = self.staff_search_dept.get()
        dept_id = self.department_map.get(dept_name)
        self.display_in_treeview(self.staff_tree,
                                 app_logic.search_staff(self.staff_search_ln.get(), dept_id))
        self.clear_staff_form()

    def on_staff_select(self, _event):
        """Handles the selection of a staff member in the treeview."""
        map_fields = {'department_id': {v: k for k, v in self.department_map.items()}}
        self.handle_on_select(self.staff_tree, self.staff_id_var, self.staff_entries,
                              "NonAcademicStaff", "staff_id", self.clear_staff_form, map_fields)
        self.refresh_staff_details()

    def clear_staff_form(self):
        """Clears the staff form."""
        self.clear_form(self.staff_id_var, self.staff_entries)
        self.refresh_staff_details()

    def refresh_staff_details(self):
        """Refreshes the staff details in the sub-tabs."""
        staff_id = self.staff_id_var.get()
        if staff_id:
            self.display_in_treeview(self.staff_contracts_tree,
                                     app_logic.get_staff_contracts(staff_id))
            self.display_in_treeview(self.staff_econtacts_tree,
                                     app_logic.get_staff_emergency_contacts(staff_id))
        else:
            self.display_in_treeview(self.staff_contracts_tree, [])
            self.display_in_treeview(self.staff_econtacts_tree, [])
        self.clear_contract_form()
        self.clear_econtact_form()

    def add_contract(self):
        """Adds a new contract for the selected staff member."""
        staff_id = self.staff_id_var.get()
        if not staff_id:
            messagebox.showerror("Error", "Select a staff member first.")
            return
        data = {k: e.get() for k, e in self.contract_entries.items()}
        data['staff_id'] = staff_id
        if self.handle_add(data, app_logic.add_contract, self.clear_contract_form,
                           self.refresh_staff_details, "Contract"):
            self.clear_contract_form()

    def update_contract(self):
        """Updates the selected contract."""
        data = {k: e.get() for k, e in self.contract_entries.items()}
        self.handle_update(data, app_logic.update_contract, self.contract_id_var, "contract_id",
                           self.clear_contract_form, self.refresh_staff_details, "Contract")

    def delete_contract(self):
        """Deletes the selected contract."""
        self.handle_delete(self.contract_id_var, "StaffContracts", "contract_id",
                           self.clear_contract_form, self.refresh_staff_details, "Contract")

    def on_contract_select(self, _event):
        """Handles the selection of a contract in the treeview."""
        self.handle_on_select(self.staff_contracts_tree, self.contract_id_var,
                              self.contract_entries, "StaffContracts", "contract_id",
                              self.clear_contract_form)

    def clear_contract_form(self):
        """Clears the contract form."""
        self.clear_form(self.contract_id_var, self.contract_entries)

    def add_econtact(self):
        """Adds a new emergency contact for the selected staff member."""
        staff_id = self.staff_id_var.get()
        if not staff_id:
            messagebox.showerror("Error", "Select a staff member first.")
            return
        data = {k: e.get() for k, e in self.econtact_entries.items()}
        data['staff_id'] = staff_id
        if self.handle_add(data, app_logic.add_emergency_contact, self.clear_econtact_form,
                           self.refresh_staff_details, "Emergency Contact"):
            self.clear_econtact_form()

    def update_econtact(self):
        """Updates the selected emergency contact."""
        data = {k: e.get() for k, e in self.econtact_entries.items()}
        self.handle_update(data, app_logic.update_emergency_contact, self.econtact_id_var,
                           "contact_id", self.clear_econtact_form,
                           self.refresh_staff_details, "Emergency Contact")

    def delete_econtact(self):
        """Deletes the selected emergency contact."""
        self.handle_delete(self.econtact_id_var, "EmergencyContacts", "contact_id",
                           self.clear_econtact_form, self.refresh_staff_details,
                           "Emergency Contact")

    def on_econtact_select(self, _event):
        """Handles the selection of an emergency contact in the treeview."""
        self.handle_on_select(self.staff_econtacts_tree, self.econtact_id_var,
                              self.econtact_entries, "EmergencyContacts", "contact_id",
                              self.clear_econtact_form)

    def clear_econtact_form(self):
        """Clears the emergency contact form."""
        self.clear_form(self.econtact_id_var, self.econtact_entries)

    # =================================================================
    # COMMITTEES TAB
    # =================================================================
    def create_committees_tab(self):
        """Creates the tab for managing committees and their members."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Committees")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=2)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=1)

        # --- Left Side: Committee Form and Search ---
        form_frame = ttk.LabelFrame(left_frame, text="Committee Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)
        fields = ["name", "description"]
        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            self.committee_entries[field] = ttk.Entry(form_frame, width=40)
            self.committee_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_committee).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_committee).pack(side="left",
                                                                                 padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_committee).pack(side="left",
                                                                                 padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_committee_form).pack(side="left",
                                                                                    padx=5)

        search_frame = ttk.LabelFrame(left_frame, text="Search Committees", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Name:").pack(side="left", padx=5)
        self.committee_search_name = ttk.Entry(search_frame)
        self.committee_search_name.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(search_frame, text="Search", command=self.search_committees).pack(side="left",
                                                                                     padx=10)

        self.committee_tree = self.create_results_treeview(left_frame)
        self.committee_tree.bind("<<TreeviewSelect>>", self.on_committee_select)

        # --- Right Side: Member Management ---
        members_frame = ttk.LabelFrame(right_frame, text="Manage Lecturer Members", padding="10")
        members_frame.pack(fill="both", expand=True)

        add_member_frame = ttk.Frame(members_frame)
        add_member_frame.pack(fill="x", pady=5)
        ttk.Label(add_member_frame, text="Lecturer:").pack(side="left")
        self.committee_member_add = ttk.Combobox(
            add_member_frame, values=list(self.lecturer_map.keys()), state="readonly"
        )
        self.committee_member_add.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(add_member_frame, text="Add Member",
                   command=self.add_committee_member).pack(side="left")

        self.committee_members_tree = self.create_results_treeview(members_frame)
        ttk.Button(members_frame, text="Remove Selected Member",
                   command=self.remove_committee_member).pack(pady=5)

        self.search_committees()

    def add_committee(self):
        """Adds a new committee to the database."""
        data = {k: e.get() for k, e in self.committee_entries.items()}
        self.handle_add(data, app_logic.add_committee, self.clear_committee_form,
                        self.search_committees, "Committee")

    def update_committee(self):
        """Updates the selected committee in the database."""
        data = {k: e.get() for k, e in self.committee_entries.items()}
        self.handle_update(data, app_logic.update_committee, self.committee_id_var,
                           "committee_id", self.clear_committee_form,
                           self.search_committees, "Committee")

    def delete_committee(self):
        """Deletes the selected committee from the database."""
        self.handle_delete(self.committee_id_var, "Committees", "committee_id",
                           self.clear_committee_form, self.search_committees, "Committee")

    def search_committees(self):
        """Searches for committees and displays them in the treeview."""
        self.display_in_treeview(self.committee_tree,
                                 app_logic.search_committees(self.committee_search_name.get()))
        self.clear_committee_form()

    def on_committee_select(self, _event):
        """Handles the selection of a committee in the treeview."""
        self.handle_on_select(self.committee_tree, self.committee_id_var,
                              self.committee_entries, "Committees", "committee_id",
                              self.clear_committee_form)
        self.refresh_committee_members()

    def clear_committee_form(self):
        """Clears the committee form."""
        self.clear_form(self.committee_id_var, self.committee_entries)
        self.refresh_committee_members()

    def refresh_committee_members(self):
        """Refreshes the list of members for the selected committee."""
        committee_id = self.committee_id_var.get()
        if committee_id:
            self.display_in_treeview(self.committee_members_tree,
                                     app_logic.get_committee_members(committee_id))
        else:
            self.display_in_treeview(self.committee_members_tree, [])

    def add_committee_member(self):
        """Adds a lecturer to the selected committee."""
        committee_id = self.committee_id_var.get()
        lecturer_name = self.committee_member_add.get()
        if not committee_id or not lecturer_name:
            messagebox.showerror("Error", "Select a committee and a lecturer.")
            return
        lecturer_id = self.lecturer_map.get(lecturer_name)
        if app_logic.add_lecturer_to_committee(committee_id, lecturer_id):
            self.refresh_committee_members()
        else:
            messagebox.showerror("Error", "Failed to add member (already a member?).")

    def remove_committee_member(self):
        """Removes a lecturer from the selected committee."""
        committee_id = self.committee_id_var.get()
        selected_item = self.committee_members_tree.focus()
        if not committee_id or not selected_item:
            messagebox.showerror("Error", "Select a committee and a member to remove.")
            return
        lecturer_id = self.committee_members_tree.item(selected_item)["values"][0]
        if app_logic.remove_lecturer_from_committee(committee_id, lecturer_id):
            self.refresh_committee_members()
        else:
            messagebox.showerror("Error", "Failed to remove member.")

    # =================================================================
    # PROJECTS, PUBLICATIONS, ORGANIZATIONS (Existing Tabs - simplified for brevity)
    # =================================================================
    def create_projects_tab(self):
        """Creates the 'Manage Research Projects' tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Manage Projects")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=2)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=1)

        form_frame = ttk.LabelFrame(left_frame, text="Project Details", padding="10")
        form_frame.pack(fill="x", padx=10, pady=5)

        self.project_entries = {}
        fields = ["title", "funding_source", "outcome_summary", "principal_investigator_id"]

        for i, field in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            ttk.Label(form_frame, text=f"{label_text}:").grid(row=i, column=0,
                                                              padx=5, pady=5, sticky="w")
            if field == "principal_investigator_id":
                self.project_entries[field] = ttk.Combobox(
                    form_frame, values=list(self.lecturer_map.keys()), state="readonly"
                )
            else:
                self.project_entries[field] = ttk.Entry(form_frame, width=40)
            self.project_entries[field].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Add", command=self.add_project).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_project).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_project).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_project_form).pack(side="left",
                                                                                  padx=5)

        search_frame = ttk.LabelFrame(left_frame, text="Search Projects", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(search_frame, text="Title:").pack(side="left", padx=5)
        self.project_search_title = ttk.Entry(search_frame)
        self.project_search_title.pack(side="left", padx=5)
        ttk.Label(search_frame, text="PI:").pack(side="left", padx=5)
        self.project_search_pi = ttk.Combobox(
            search_frame, values=[""] + list(self.lecturer_map.keys()), state="readonly"
        )
        self.project_search_pi.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_projects).pack(side="left",
                                                                                   padx=10)

        self.project_tree = self.create_results_treeview(left_frame)
        self.project_tree.bind("<<TreeviewSelect>>", self.on_project_select)

        members_frame = ttk.LabelFrame(right_frame, text="Manage Student Members", padding="10")
        members_frame.pack(fill="both", expand=True)

        add_member_frame = ttk.Frame(members_frame)
        add_member_frame.pack(fill="x", pady=5)
        ttk.Label(add_member_frame, text="Student to Add:").pack(side="left")
        self.project_member_student = ttk.Combobox(
            add_member_frame, values=list(self.student_map.keys()), state="readonly"
        )
        self.project_member_student.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(add_member_frame, text="Add Member",
                   command=self.add_project_member).pack(side="left")

        self.project_members_tree = self.create_results_treeview(members_frame)
        ttk.Button(members_frame, text="Remove Selected Member",
                   command=self.remove_project_member).pack(pady=5)

        self.search_projects()

    def create_publications_tab(self):
        """Creates the 'Manage Publications' tab."""
        fields = ["title", "year", "publication_venue"]
        self.pub_entries, self.pub_id_var, self.pub_tree, search_frame, btn_frame = \
            self.create_crud_tab("Manage Publications", fields)
        ttk.Label(search_frame, text="Title:").pack(side="left", padx=5)
        self.pub_search_title = ttk.Entry(search_frame)
        self.pub_search_title.pack(side="left", padx=5)
        ttk.Label(search_frame, text="Year:").pack(side="left", padx=5)
        self.pub_search_year = ttk.Entry(search_frame)
        self.pub_search_year.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_publications).pack(
            side="left", padx=10
        )
        ttk.Button(btn_frame, text="Add", command=self.add_publication).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update", command=self.update_publication).pack(side="left",
                                                                                   padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_publication).pack(side="left",
                                                                                   padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_publication_form).pack(
            side="left", padx=5
        )
        self.pub_tree.bind("<<TreeviewSelect>>", self.on_publication_select)
        self.search_publications()

    def create_organizations_tab(self):
        """Creates the 'Manage Student Organizations' tab."""
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Organizations")

        main_pane = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(left_frame, weight=2)
        right_frame = ttk.Frame(main_pane, padding=5)
        main_pane.add(right_frame, weight=1)

        org_form = ttk.LabelFrame(left_frame, text="Organization Details", padding="10")
        org_form.pack(fill="x", pady=5)
        self.org_entries = {}
        ttk.Label(org_form, text="Name:").grid(row=0, column=0, sticky="w")
        self.org_entries['name'] = ttk.Entry(org_form, width=30)
        self.org_entries['name'].grid(row=0, column=1, sticky="ew")
        ttk.Label(org_form, text="Description:").grid(row=1, column=0, sticky="w")
        self.org_entries['description'] = ttk.Entry(org_form, width=30)
        self.org_entries['description'].grid(row=1, column=1, sticky="ew")

        org_btn = ttk.Frame(left_frame)
        org_btn.pack(fill="x", pady=5)
        ttk.Button(org_btn, text="Add", command=self.add_organization).pack(side="left")
        ttk.Button(org_btn, text="Update", command=self.update_organization).pack(side="left")
        ttk.Button(org_btn, text="Delete", command=self.delete_organization).pack(side="left")
        ttk.Button(org_btn, text="Clear", command=self.clear_organization_form).pack(side="left")

        self.org_tree = self.create_results_treeview(left_frame)
        self.org_tree.bind("<<TreeviewSelect>>", self.on_organization_select)

        members_frame = ttk.LabelFrame(right_frame, text="Manage Members", padding="10")
        members_frame.pack(fill="both", expand=True)

        add_member_frame = ttk.Frame(members_frame)
        add_member_frame.pack(fill="x", pady=5)
        ttk.Label(add_member_frame, text="Student to Add:").pack(side="left")
        self.org_member_student = ttk.Combobox(
            add_member_frame, values=list(self.student_map.keys()), state="readonly"
        )
        self.org_member_student.pack(side="left", padx=5, fill="x", expand=True)
        ttk.Button(add_member_frame, text="Add Member",
                   command=self.add_org_member).pack(side="left")

        self.org_members_tree = self.create_results_treeview(members_frame)
        ttk.Button(members_frame, text="Remove Selected Member",
                   command=self.remove_org_member).pack(pady=5)

        self.search_organizations()

    # --- Project Methods ---
    def add_project(self):
        """Adds a new project to the database."""
        data = {key: entry.get() for key, entry in self.project_entries.items()}
        pi_id = self.lecturer_map.get(data['principal_investigator_id'])
        data['principal_investigator_id'] = pi_id
        self.handle_add(data, app_logic.add_project, self.clear_project_form,
                        self.search_projects, "Project")

    def update_project(self):
        """Updates the selected project in the database."""
        data = {key: entry.get() for key, entry in self.project_entries.items()}
        pi_id = self.lecturer_map.get(data['principal_investigator_id'])
        data['principal_investigator_id'] = pi_id
        self.handle_update(data, app_logic.update_project, self.project_id_var, "project_id",
                           self.clear_project_form, self.search_projects, "Project")

    def delete_project(self):
        """Deletes the selected project from the database."""
        self.handle_delete(self.project_id_var, "ResearchProjects", "project_id",
                           self.clear_project_form, self.search_projects, "Project")

    def search_projects(self):
        """Searches for projects and displays them in the treeview."""
        pi_name = self.project_search_pi.get()
        pi_id = self.lecturer_map.get(pi_name)
        self.display_in_treeview(self.project_tree,
                                 app_logic.search_projects(self.project_search_title.get(),
                                                           pi_id))
        self.clear_project_form()

    def on_project_select(self, _event):
        """Handles the selection of a project in the treeview."""
        map_fields = {'principal_investigator_id': {v: k for k, v in self.lecturer_map.items()}}
        self.handle_on_select(self.project_tree, self.project_id_var, self.project_entries,
                              "ResearchProjects", "project_id", self.clear_project_form,
                              map_fields)
        project_id = self.project_id_var.get()
        if project_id:
            members = app_logic.get_project_members(project_id)
            self.display_in_treeview(self.project_members_tree, members)

    def clear_project_form(self):
        """Clears the project form."""
        self.clear_form(self.project_id_var, self.project_entries)
        self.display_in_treeview(self.project_members_tree, [])

    def add_project_member(self):
        """Adds a student to the selected project."""
        project_id = self.project_id_var.get()
        student_name = self.project_member_student.get()
        if not project_id:
            messagebox.showerror("Error", "Please select a project first.")
            return
        if not student_name:
            messagebox.showerror("Error", "Please select a student to add.")
            return
        student_id = self.student_map.get(student_name)
        if app_logic.add_student_to_project(project_id, student_id):
            messagebox.showinfo("Success", "Member added.")
            self.project_member_student.set('')
            members = app_logic.get_project_members(project_id)
            self.display_in_treeview(self.project_members_tree, members)

    def remove_project_member(self):
        """Removes a student from the selected project."""
        project_id = self.project_id_var.get()
        selected_item = self.project_members_tree.focus()
        if not project_id:
            messagebox.showerror("Error", "Please select a project first.")
            return
        if not selected_item:
            messagebox.showerror("Error", "Please select a member to remove.")
            return
        student_id = self.project_members_tree.item(selected_item)["values"][0]
        if app_logic.remove_student_from_project(project_id, student_id):
            messagebox.showinfo("Success", "Member removed.")
            members = app_logic.get_project_members(project_id)
            self.display_in_treeview(self.project_members_tree, members)

    # --- Publication Methods ---
    def add_publication(self):
        """Adds a new publication to the database."""
        data = {k: e.get() for k, e in self.pub_entries.items()}
        self.handle_add(data, app_logic.add_publication, self.clear_publication_form,
                        self.search_publications, "Publication")

    def update_publication(self):
        """Updates the selected publication in the database."""
        data = {k: e.get() for k, e in self.pub_entries.items()}
        self.handle_update(data, app_logic.update_publication, self.pub_id_var,
                           "publication_id", self.clear_publication_form,
                           self.search_publications, "Publication")

    def delete_publication(self):
        """Deletes the selected publication from the database."""
        self.handle_delete(self.pub_id_var, "Publications", "publication_id",
                           self.clear_publication_form, self.search_publications, "Publication")

    def search_publications(self):
        """Searches for publications and displays them in the treeview."""
        self.display_in_treeview(self.pub_tree,
                                 app_logic.search_publications(self.pub_search_title.get(),
                                                               self.pub_search_year.get()))
        self.clear_publication_form()

    def on_publication_select(self, _event):
        """Handles the selection of a publication in the treeview."""
        self.handle_on_select(self.pub_tree, self.pub_id_var, self.pub_entries,
                              "Publications", "publication_id", self.clear_publication_form)

    def clear_publication_form(self):
        """Clears the publication form."""
        self.clear_form(self.pub_id_var, self.pub_entries)

    # --- Organization Methods ---
    def add_organization(self):
        """Adds a new organization to the database."""
        data = {k: e.get() for k, e in self.org_entries.items()}
        self.handle_add(data, app_logic.add_organization, self.clear_organization_form,
                        self.search_organizations, "Organization")

    def update_organization(self):
        """Updates the selected organization in the database."""
        data = {k: e.get() for k, e in self.org_entries.items()}
        self.handle_update(data, app_logic.update_organization, self.org_id_var,
                           "organization_id", self.clear_organization_form,
                           self.search_organizations, "Organization")

    def delete_organization(self):
        """Deletes the selected organization from the database."""
        self.handle_delete(self.org_id_var, "StudentOrganizations", "organization_id",
                           self.clear_organization_form, self.search_organizations,
                           "Organization")

    def search_organizations(self):
        """Searches for organizations and displays them in the treeview."""
        query = "SELECT organization_id, name, description FROM StudentOrganizations"
        self.display_in_treeview(self.org_tree, db_connector.execute_query(query, fetch='all'))
        self.clear_organization_form()

    def on_organization_select(self, _event):
        """Handles the selection of an organization in the treeview."""
        self.handle_on_select(self.org_tree, self.org_id_var, self.org_entries,
                              "StudentOrganizations", "organization_id",
                              self.clear_organization_form)
        org_id = self.org_id_var.get()
        if org_id:
            members = app_logic.get_organization_members(org_id)
            self.display_in_treeview(self.org_members_tree, members)

    def clear_organization_form(self):
        """Clears the organization form."""
        self.clear_form(self.org_id_var, self.org_entries)
        self.display_in_treeview(self.org_members_tree, [])

    def add_org_member(self):
        """Adds a student to the selected organization."""
        org_id = self.org_id_var.get()
        student_name = self.org_member_student.get()
        if not org_id:
            messagebox.showerror("Error", "Please select an organization first.")
            return
        if not student_name:
            messagebox.showerror("Error", "Please select a student to add.")
            return
        student_id = self.student_map.get(student_name)
        if app_logic.add_student_to_organization(org_id, student_id):
            messagebox.showinfo("Success", "Member added.")
            self.org_member_student.set('')
            members = app_logic.get_organization_members(org_id)
            self.display_in_treeview(self.org_members_tree, members)

    def remove_org_member(self):
        """Removes a student from the selected organization."""
        org_id = self.org_id_var.get()
        selected_item = self.org_members_tree.focus()
        if not org_id:
            messagebox.showerror("Error", "Please select an organization first.")
            return
        if not selected_item:
            messagebox.showerror("Error", "Please select a member to remove.")
            return
        student_id = self.org_members_tree.item(selected_item)["values"][0]
        if app_logic.remove_student_from_organization(org_id, student_id):
            messagebox.showinfo("Success", "Member removed.")
            members = app_logic.get_organization_members(org_id)
            self.display_in_treeview(self.org_members_tree, members)

    # =================================================================
    # ADVANCED QUERIES TAB
    # =================================================================
    def create_advanced_queries_tab(self):
        """Creates the tab for running all advanced queries."""
        aq_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(aq_frame, text="Advanced Queries")

        # Main layout: controls on the left, results on the right
        main_pane = ttk.PanedWindow(aq_frame, orient=tk.HORIZONTAL)
        main_pane.pack(fill="both", expand=True)

        controls_outer_frame = ttk.Frame(main_pane)
        main_pane.add(controls_outer_frame, weight=1)
        results_frame = ttk.Frame(main_pane)
        main_pane.add(results_frame, weight=2)

        # Scrollable frame for query controls
        controls_canvas = tk.Canvas(controls_outer_frame)
        scrollbar = ttk.Scrollbar(controls_outer_frame, orient="vertical",
                                  command=controls_canvas.yview)
        scrollable_frame = ttk.Frame(controls_canvas)
        scrollable_frame.bind("<Configure>",
                              lambda e: controls_canvas.configure(
                                  scrollregion=controls_canvas.bbox("all"))
                              )
        controls_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        controls_canvas.configure(yscrollcommand=scrollbar.set)

        controls_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Results treeview
        self.aq_tree = self.create_results_treeview(results_frame)

        # Create individual query frames inside the scrollable frame
        self.create_q1_frame(scrollable_frame)
        self.create_q2_frame(scrollable_frame)
        self.create_q3_frame(scrollable_frame)
        self.create_q4_frame(scrollable_frame)
        self.create_q5_frame(scrollable_frame)
        self.create_q6_frame(scrollable_frame)
        self.create_q7_frame(scrollable_frame)
        self.create_q8_frame(scrollable_frame)
        self.create_q9_frame(scrollable_frame)
        self.create_q10_frame(scrollable_frame)

    def create_q1_frame(self, parent):
        """Creates the UI for advanced query 1."""
        q_frame = ttk.LabelFrame(parent, text="Find Students in Course by Lecturer", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(q_frame, text="Course:").pack(side="left", padx=5)
        self.q1_course = ttk.Combobox(q_frame, values=list(self.course_map.keys()),
                                      state="readonly")
        self.q1_course.pack(side="left", padx=5)
        self.q1_course.bind("<<ComboboxSelected>>", self.update_q1_lecturers)

        ttk.Label(q_frame, text="Lecturer:").pack(side="left", padx=5)
        self.q1_lecturer = ttk.Combobox(q_frame, state="readonly")
        self.q1_lecturer.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q1).pack(side="left", padx=10)

    def update_q1_lecturers(self, _event=None):
        """Updates the lecturer dropdown based on the selected course."""
        course_name = self.q1_course.get()
        if not course_name:
            self.q1_lecturer['values'] = []
            self.q1_lecturer.set('')
            return
        course_id = self.course_map.get(course_name)
        lecturers = app_logic.get_lecturers_for_course(course_id)
        if lecturers:
            self.q1_lecturer_map = {l['name']: l['lecturer_id'] for l in lecturers}
            self.q1_lecturer['values'] = list(self.q1_lecturer_map.keys())
        else:
            self.q1_lecturer['values'] = []
        self.q1_lecturer.set('')

    def run_q1(self):
        """Runs the 'Find Students in Course by Lecturer' query."""
        course_name = self.q1_course.get()
        lecturer_name = self.q1_lecturer.get()
        if not course_name or not lecturer_name:
            messagebox.showerror("Error", "All fields are required.")
            return
        course_id = self.course_map.get(course_name)
        lecturer_id = self.q1_lecturer_map.get(lecturer_name)
        results = app_logic.find_students_in_course_by_lecturer(course_id, lecturer_id)
        self.display_in_treeview(self.aq_tree, results)

    def create_q2_frame(self, parent):
        """Creates the UI for advanced query 2."""
        q_frame = ttk.LabelFrame(parent, text="Find High-Achieving Final Year Students",
                                 padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(q_frame, text="Min Grade %:").pack(side="left", padx=5)
        self.q2_min_grade = ttk.Entry(q_frame, width=10)
        self.q2_min_grade.insert(0, "70")
        self.q2_min_grade.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q2).pack(side="left", padx=10)

    def run_q2(self):
        """Runs the 'Find High-Achieving Students' query."""
        min_grade = self.q2_min_grade.get()
        if not min_grade:
            messagebox.showerror("Error", "Minimum Grade is required.")
            return
        results = app_logic.find_high_achieving_final_year_students(min_grade)
        self.display_in_treeview(self.aq_tree, results)

    def create_q3_frame(self, parent):
        """Creates the UI for advanced query 3."""
        q_frame = ttk.LabelFrame(parent, text="Find Unregistered Students", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)

        current_year = datetime.now().year
        years = [str(y) for y in range(current_year - 5, current_year + 2)]
        semesters = ["Fall", "Spring"]

        ttk.Label(q_frame, text="Year:").pack(side="left", padx=5)
        self.q3_year = ttk.Combobox(q_frame, values=years, state="readonly", width=8)
        self.q3_year.pack(side="left", padx=5)
        ttk.Label(q_frame, text="Semester:").pack(side="left", padx=5)
        self.q3_semester = ttk.Combobox(q_frame, values=semesters, state="readonly", width=10)
        self.q3_semester.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q3).pack(side="left", padx=10)

    def run_q3(self):
        """Runs the 'Find Unregistered Students' query."""
        year = self.q3_year.get()
        semester = self.q3_semester.get()
        if not year or not semester:
            messagebox.showerror("Error", "All fields are required.")
            return
        results = app_logic.find_unregistered_students(year, semester)
        self.display_in_treeview(self.aq_tree, results)

    def create_q4_frame(self, parent):
        """Creates the UI for advanced query 4."""
        q_frame = ttk.LabelFrame(parent, text="Find Student's Advisor", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(q_frame, text="Student:").pack(side="left", padx=5)
        self.q4_student = ttk.Combobox(q_frame, values=list(self.student_map.keys()),
                                       state="readonly", width=30)
        self.q4_student.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q4).pack(side="left", padx=10)

    def run_q4(self):
        """Runs the 'Find Student's Advisor' query."""
        student_name = self.q4_student.get()
        if not student_name:
            messagebox.showerror("Error", "Student is required.")
            return
        student_id = self.student_map.get(student_name)
        self.display_in_treeview(self.aq_tree, app_logic.find_advisor_for_student(student_id))

    def create_q5_frame(self, parent):
        """Creates the UI for advanced query 5."""
        q_frame = ttk.LabelFrame(parent, text="Find Lecturers by Expertise", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(q_frame, text="Research Area:").pack(side="left", padx=5)
        self.q5_area = ttk.Combobox(q_frame, values=list(self.research_area_map.keys()),
                                    state="readonly", width=20)
        self.q5_area.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q5).pack(side="left", padx=10)

    def run_q5(self):
        """Runs the 'Find Lecturers by Expertise' query."""
        area_name = self.q5_area.get()
        if not area_name:
            messagebox.showerror("Error", "Research Area is required.")
            return
        area_id = self.research_area_map.get(area_name)
        self.display_in_treeview(self.aq_tree, app_logic.find_lecturers_by_expertise(area_id))

    def create_q6_frame(self, parent):
        """Creates the UI for advanced query 6."""
        q_frame = ttk.LabelFrame(parent, text="Find Courses by Department", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(q_frame, text="Department:").pack(side="left", padx=5)
        self.q6_dept = ttk.Combobox(q_frame, values=list(self.department_map.keys()),
                                    state="readonly", width=20)
        self.q6_dept.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q6).pack(side="left", padx=10)

    def run_q6(self):
        """Runs the 'Find Courses by Department' query."""
        dept_name = self.q6_dept.get()
        if not dept_name:
            messagebox.showerror("Error", "Department Name is required.")
            return
        dept_id = self.department_map.get(dept_name)
        results = app_logic.find_courses_by_department_lecturer(dept_id)
        self.display_in_treeview(self.aq_tree, results)

    def create_q7_frame(self, parent):
        """Creates the UI for advanced query 7."""
        q_frame = ttk.LabelFrame(parent, text="Find Top Student Project Supervisor", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(q_frame, text="Run", command=self.run_q7).pack(side="left", padx=10)

    def run_q7(self):
        """Runs the 'Find Top Supervisor' query."""
        self.display_in_treeview(self.aq_tree, app_logic.find_top_project_supervisor())

    def create_q8_frame(self, parent):
        """Creates the UI for advanced query 8."""
        q_frame = ttk.LabelFrame(parent, text="Find Recent Publications (Last Year)", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(q_frame, text="Run", command=self.run_q8).pack(side="left", padx=10)

    def run_q8(self):
        """Runs the 'Find Recent Publications' query."""
        self.display_in_treeview(self.aq_tree, app_logic.find_recent_publications())

    def create_q9_frame(self, parent):
        """Creates the UI for advanced query 9."""
        q_frame = ttk.LabelFrame(parent, text="Find Students by Advisor", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(q_frame, text="Lecturer:").pack(side="left", padx=5)
        self.q9_lecturer = ttk.Combobox(q_frame, values=list(self.lecturer_map.keys()),
                                        state="readonly", width=30)
        self.q9_lecturer.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q9).pack(side="left", padx=10)

    def run_q9(self):
        """Runs the 'Find Students by Advisor' query."""
        lecturer_name = self.q9_lecturer.get()
        if not lecturer_name:
            messagebox.showerror("Error", "Lecturer is required.")
            return
        lecturer_id = self.lecturer_map.get(lecturer_name)
        self.display_in_treeview(self.aq_tree, app_logic.find_students_by_advisor(lecturer_id))

    def create_q10_frame(self, parent):
        """Creates the UI for advanced query 10."""
        q_frame = ttk.LabelFrame(parent, text="Find Staff by Department", padding=5)
        q_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(q_frame, text="Department:").pack(side="left", padx=5)
        self.q10_dept = ttk.Combobox(q_frame, values=list(self.department_map.keys()),
                                     state="readonly", width=20)
        self.q10_dept.pack(side="left", padx=5)
        ttk.Button(q_frame, text="Run", command=self.run_q10).pack(side="left", padx=10)

    def run_q10(self):
        """Runs the 'Find Staff by Department' query."""
        dept_name = self.q10_dept.get()
        if not dept_name:
            messagebox.showerror("Error", "Department is required.")
            return
        dept_id = self.department_map.get(dept_name)
        self.display_in_treeview(self.aq_tree, app_logic.find_staff_by_department(dept_id))

    # =================================================================
    # GENERIC HELPERS
    # =================================================================
    def create_results_treeview(self, parent_frame):
        """Helper to create a scrollable results table (Treeview)."""
        tree_frame = ttk.Frame(parent_frame)
        tree_frame.pack(fill="both", expand=True, padx=5, pady=5)
        tree_scroll_y = ttk.Scrollbar(tree_frame, orient="vertical")
        tree_scroll_y.pack(side="right", fill="y")
        tree_scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal")
        tree_scroll_x.pack(side="bottom", fill="x")
        tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set,
                            xscrollcommand=tree_scroll_x.set, show="headings")
        tree.pack(fill="both", expand=True)
        tree_scroll_y.config(command=tree.yview)
        tree_scroll_x.config(command=tree.xview)
        return tree

    def display_in_treeview(self, tree, data):
        """Clears and populates a treeview with new data."""
        for item in tree.get_children():
            tree.delete(item)
        if not data:
            if tree == self.aq_tree and data is not None:
                messagebox.showinfo("Info", "No records found for this query.")
            tree["columns"] = []
            return
        if isinstance(data, dict):  # Handle single record returns
            data = [data]

        tree["columns"] = list(data[0].keys())
        for col in tree["columns"]:
            tree.heading(col, text=col.replace("_", " ").title(), anchor="w")
            tree.column(col, width=120, anchor="w", stretch=tk.YES)
        for row in data:
            tree.insert("", "end", values=[str(v) if v is not None else "" for v in row.values()])

    def handle_add(self, data, add_func, clear_func, search_func, name):
        """Generic handler for adding a record."""
        if add_func(data):
            messagebox.showinfo("Success", f"{name} added successfully.")
            clear_func()
            search_func()
            return True
        else:
            messagebox.showerror("Error", f"Failed to add {name}.")
            return False

    def handle_update(self, data, update_func, id_var, id_key, clear_func, search_func, name):
        """Generic handler for updating a record."""
        selected_id = id_var.get()
        if not selected_id:
            messagebox.showerror("Error", f"No {name} selected.")
            return False
        data[id_key] = selected_id
        if update_func(data):
            messagebox.showinfo("Success", f"{name} updated successfully.")
            clear_func()
            search_func()
            return True
        else:
            messagebox.showerror("Error", f"Failed to update {name}.")
            return False

    def handle_delete(self, id_var, table_name, id_column, clear_func, search_func, name):
        """Generic handler for deleting a record."""
        selected_id = id_var.get()
        if not selected_id:
            messagebox.showerror("Error", f"No {name} selected.")
            return False
        if messagebox.askyesno("Confirm Delete",
                               f"Are you sure you want to delete {name} ID {selected_id}?"
                               " This cannot be undone."):
            if app_logic.delete_record(table_name, id_column, selected_id):
                messagebox.showinfo("Success", f"{name} deleted.")
                clear_func()
                search_func()
                return True
            else:
                messagebox.showerror("Error",
                                     f"Failed to delete {name}. "
                                     "It might be referenced by other records.")
                return False
        return False

    def handle_on_select(self, tree, id_var, entries, table_name, id_column, clear_func,
                         map_fields=None):
        """Generic handler for selecting a record in a treeview."""
        selected_item = tree.focus()
        if not selected_item:
            return
        item_values = tree.item(selected_item)["values"]
        record_id = item_values[0]
        full_details = app_logic.get_record_by_id(table_name, id_column, record_id)
        if full_details:
            clear_func()
            id_var.set(record_id)
            for key, entry_widget in entries.items():
                value = full_details.get(key, "")
                if key in (map_fields or {}):
                    # Reverse map the ID to the display name
                    display_name = map_fields[key].get(value, "")
                    entry_widget.set(display_name)
                elif isinstance(entry_widget, (ttk.Entry, tk.Entry)):
                    entry_widget.delete(0, "end")
                    entry_widget.insert(0, str(value) if value is not None else "")
                elif isinstance(entry_widget, ttk.Combobox):
                    entry_widget.set(str(value) if value is not None else "")

    def clear_form(self, id_var, entries):
        """Generic handler to clear a form."""
        id_var.set("")
        for entry in entries.values():
            if isinstance(entry, ttk.Combobox):
                entry.set('')
            else:
                entry.delete(0, "end")

if __name__ == "__main__":
    # This check is important to ensure the app doesn't run if the DB is down.
    if db_connector.execute_query("SELECT 1", fetch='one') is not None:
        app = App()
        app.mainloop()
    else:
        # Use a more robust way to show the error if the main loop isn't running
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Database Connection Error",
                             "Could not connect to the database. Please check your .env "
                             "configuration and ensure the MySQL server is running.")
