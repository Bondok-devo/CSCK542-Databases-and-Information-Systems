import os
import unittest
import mysql.connector
os.environ["DB_USER"] = "root"
os.environ["DB_PASSWORD"] = "password"
os.environ["DB_NAME"] = "university_db"
os.environ["DB_HOST"] = "localhost"
import app_logic
import datetime

class TestAdvancedQueries(unittest.TestCase):
#databases connect
    def setUp(self):
        self.conn = mysql.connector.connect(
            host=os.environ["DB_HOST"],
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")

        )
        self.cursor = self.conn.cursor(dictionary=True)
#tear down
    def tearDown(self):
        self.cursor.close()
        self.conn.close()

# test CRUD
    def test_full_advising_record_lifecycle(self):
        self.test_data = {
            "student_id": 101,
            "lecturer_id": 20,
            "start_date": datetime.date(2025, 1, 1),
            "end_date": datetime.date(2025, 6, 30)
        }

        # insert the record
        insert_result = app_logic.add_advising_record(self.test_data)
        self.assertIsNotNone(insert_result)

        # search the record
        query_result = app_logic.search_advising_history(self.test_data["student_id"])
        self.assertTrue(any(
        record["start_date"] == self.test_data["start_date"]
        and record["lecturer_id"] == self.test_data["lecturer_id"]
        for record in query_result
        ))

        # update record
        updated_data = self.test_data.copy()
        updated_data["end_date"] = datetime.date(2025, 7, 31)
        update_result = app_logic.update_advising_record(updated_data)
        self.assertIsNotNone(update_result)

        # double check the record has been updated
        query_result = app_logic.search_advising_history(self.test_data["student_id"])
        self.assertTrue(any(
        record["end_date"] == updated_data["end_date"]
        for record in query_result
        ))

        # delete record
        delete_result = app_logic.delete_advising_record(
        self.test_data["student_id"],
        self.test_data["lecturer_id"],
        self.test_data["start_date"]
        )
        self.assertIsNotNone(delete_result)

        # double check the record has been deleted
        final_check = app_logic.search_advising_history(self.test_data["student_id"])
        self.assertFalse(any(
        record["start_date"] == self.test_data["start_date"] and
        record["lecturer_id"] == self.test_data["lecturer_id"]
        for record in final_check
        ))


    def test_find_students_in_course_by_lecturer(self):
        """Finds students in a specific course taught by a specific lecturer."""
        # use true course_id and lecturer_id
        course_id = 1
        lecturer_id = 1
        course_name_expected = "Introduction to Programming"

        # call original method
        result = app_logic.find_students_in_course_by_lecturer(course_id, lecturer_id)

        # verify the data
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        for student in result:
            self.assertIn("student_email", student)
            self.assertEqual(student["course_name"], course_name_expected)


    def test_find_high_achieving_final_year_students(self):
        """Lists final-year students with an average grade above a certain percentage."""
        min_grade = 88
        result = app_logic.find_high_achieving_final_year_students(min_grade)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        for student in result:
            self.assertIn("last_name", student)
            avg_grade=float(student["avg_grade"])
            self.assertGreater(avg_grade, min_grade)

    def test_find_unregistered_students(self):
        """Finds students not registered for any courses in a given semester."""
        year = 2025
        semester = "fall"
        result = app_logic.find_unregistered_students(year, semester)
        # verify the data
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 200)


    def test_find_advisor_for_student(self):
        """Retrieves the current advisor for a specific student."""
        student_id = 33
        first_name_expected="John"
        result = app_logic.find_advisor_for_student(student_id)
        self.assertTrue(any(advisor["first_name"] == first_name_expected for advisor in result))


    def test_find_lecturers_by_expertise(self):
        """Searches for lecturers by their research area."""
        areaid = 1
        result = app_logic.find_lecturers_by_expertise(areaid)

        if isinstance(result, list):
            name = result[0]["first_name"]
        elif isinstance(result, dict):
            name = result["first_name"]
        else:
            raise TypeError("Unexpected result format")
        self.assertEqual(name, "Alan")

    def test_find_courses_by_department_lecturer(self):
        """Lists all courses taught by lecturers from a specific department."""
        department_id = 1
        course_name_expected="Databases"
        result = app_logic .find_courses_by_department_lecturer(department_id)
        self.assertTrue(any(coursename["course_name"] == course_name_expected for coursename in result))


    def test_find_top_project_supervisor(self):
        """Identifies the lecturer supervising the most students on research projects."""
        students_supervised_firstname_expect = "Marie"
        result = app_logic.find_top_project_supervisor()
        self.assertEqual(result["first_name"], students_supervised_firstname_expect)



    def test_find_recent_publications(self):
        """Generates a report of publications from the past year."""
        title_expect = "Revisiting the Fall of Rome"
        result = app_logic.find_recent_publications()
        self.assertTrue(any(publication["title"] == title_expect for publication in result))

    def test_find_students_by_advisor(self):
        """Finds all students currently advised by a specific lecturer."""
        lecturerId = 1
        nameExpect = "Colton"
        result = app_logic.find_students_by_advisor(lecturerId)
        self.assertTrue(any(student["first_name"] == nameExpect for student in result))

    def test_find_staff_by_department(self):
        """Finds all staff (lecturers and non-academic) in a specific department."""
        departmentId = 1
        nameExpect = "Grace"
        result = app_logic.find_staff_by_department(departmentId)
        self.assertIsInstance(result, list, "Expected result to be a list")
        self.assertGreater(len(result), 0, "Result list is not empty")
        self.assertTrue(any(staff["first_name"] == nameExpect for staff in result))

if __name__ == '__main__':
  unittest.main()




