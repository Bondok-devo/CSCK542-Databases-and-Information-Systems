import unittest
from unittest.mock import patch
import app_logic


class TestAppLogic(unittest.TestCase):

    # --- CRUD ---

        #add
        @patch('app_logic.db_connector.execute_query')
        def test_add_course_material(self, mock_execute):
            data = {'offering_id': 1, 'material_details': 'Slides', 'material_type': 'PDF'}
            app_logic.add_course_material(data)
            mock_execute.assert_called_with(
                "INSERT INTO CourseMaterials (offering_id, material_details, material_type) VALUES (%(offering_id)s, %(material_details)s, %(material_type)s)",
                data
            )
  #update
        @patch('app_logic.db_connector.execute_query')
        def test_update_course_material(self, mock_execute):
         data = {'material_id': 10, 'material_details': 'Updated Slides', 'material_type': 'PDF'}

         app_logic.update_course_material(data)
         mock_execute.assert_called_with(
            "UPDATE CourseMaterials SET material_details=%(material_details)s, material_type=%(material_type)s WHERE material_id=%(material_id)s",
            data
           )
#search
        @patch('app_logic.db_connector.execute_query')
        def test_search_course_offerings(self, mock_execute):
            mock_execute.return_value = []
            app_logic.search_course_offerings(1001, 2024)
            mock_execute.assert_called()
#delete
        @patch('app_logic.db_connector.execute_query')
        def test_remove_course_from_program(self, mock_execute):
            program_id = 1001
            course_id = 2002

            app_logic.remove_course_from_program(program_id, course_id)

            mock_execute.assert_called_once_with(
                "DELETE FROM ProgramRequirements WHERE program_id = %s AND course_id = %s",
                (program_id, course_id)
            )

        @patch('app_logic.db_connector.execute_query')
        def test_find_students_in_course_by_lecturer(self, mock_execute_query):
            mock_execute_query.return_value = [
                {'first_name': 'John', 'last_name': 'Doe', 'student_email': 'john@example.com', 'course_name': 'Math'}
            ]
            result = app_logic.find_students_in_course_by_lecturer(101, 202)
            mock_execute_query.assert_called_once()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]['course_name'], 'Math')

        @patch('app_logic.db_connector.execute_query')
        def test_find_high_achieving_final_year_students(self, mock_execute_query):
            mock_execute_query.return_value = [
                {'first_name': 'Jane', 'last_name': 'Smith', 'program': 'CS', 'avg_grade': '89.50'}
            ]
            result = app_logic.find_high_achieving_final_year_students(85)
            mock_execute_query.assert_called_once()
            self.assertGreater(float(result[0]['avg_grade']), 85)

        @patch('app_logic.db_connector.execute_query')
        def test_find_unregistered_students(self, mock_execute_query):
            mock_execute_query.return_value = [
                {'student_id': 301, 'first_name': 'Alice', 'last_name': 'Wong', 'student_email': 'alice@example.com'}
            ]
            result = app_logic.find_unregistered_students(2025, 'Fall')
            mock_execute_query.assert_called_once()
            self.assertEqual(result[0]['first_name'], 'Alice')


        @patch('app_logic.db_connector.execute_query')
        def test_find_advisor_for_student(self, mock_execute):
            student_id = 101
            app_logic.find_advisor_for_student(student_id)
            args, kwargs = mock_execute.call_args
            sql = args[0]

            assert "FROM Lecturers" in sql
            assert "JOIN AdvisingHistory" in sql
            assert "WHERE ah.student_id = %s" in sql
            assert "AND ah.end_date IS NULL" in sql
            assert args[1] == (101,)
            assert kwargs['fetch'] == 'all'

        @patch('app_logic.db_connector.execute_query')
        def test_find_lecturers_by_expertise(self, mock_execute):
            area_id = 301
            app_logic.find_lecturers_by_expertise(area_id)
            args, kwargs = mock_execute.call_args
            sql = args[0]

            assert "FROM Lecturers" in sql
            assert "WHERE lra.area_id = %s" in sql
            assert (301,) == args[1]
            assert kwargs.get('fetch') == 'all'




        @patch('app_logic.db_connector.execute_query')
        def test_find_courses_by_department_lecturer(self, mock_execute):
            dept_id = 77
            app_logic.find_courses_by_department_lecturer(dept_id)
            args, kwargs = mock_execute.call_args
            sql = args[0]

            assert "SELECT DISTINCT c.course_code" in sql
            assert "FROM Courses" in sql
            assert "WHERE l.department_id = %s" in sql
            assert args[1] == (77,)
            assert kwargs.get('fetch') == 'all'


        @patch('app_logic.db_connector.execute_query')
        def test_find_top_project_supervisor(self, mock_execute):
            app_logic.find_top_project_supervisor()
            args, kwargs = mock_execute.call_args
            assert "FROM Lecturers" in args[0]
            assert "ORDER BY students_supervised DESC LIMIT 1" in args[0]
            assert kwargs['fetch'] == 'one'

if __name__ == '__main__':
    unittest.main()