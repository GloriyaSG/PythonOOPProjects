from unittest import TestCase, main

from project.student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Mart")
        self.student_full = Student("Alex", {"geo": ["note"]})

    def test_initialize(self):
        self.assertEqual("Mart", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"geo": ["note"]}, self.student_full.courses)

    def test_enrollment_if_course_name_in_courses(self):
        result = self.student_full.enroll("geo",["notes_two"])
        self.assertEqual(["note", "notes_two"], self.student_full.courses["geo"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enrollment_with_Y(self):
        result = self.student.enroll("c#", ["c#_fund"], "Y")

        self.assertEqual(["c#_fund"], self.student.courses["c#"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enrollment_new_course_without_notes(self):
        result = self.student.enroll("c#", ["c#_fund"], ".")

        self.assertEqual([], self.student.courses["c#"])
        self.assertEqual("Course has been added.", result)

    def test_enroll_method_check_if_add_course_notes_is_empty_string(self):
        result = self.student.enroll("Python", ["note1", "note2"])

        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)
        self.assertEqual(f"Course and course notes have been added.", result)

    def test_adding_notes_in_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("python", ["c#_fund"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_adding_notes_in_existing_course(self):
        result = self.student_full.add_notes("geo", ["cool"])

        self.assertEqual(["note", ["cool"]], self.student_full.courses["geo"])
        self.assertEqual("Notes have been updated", result)

    def test_leaving_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leaving_existing_course(self):
        result = self.student_full.leave_course("geo")
        self.assertEqual("Course has been removed", result)


if __name__ == "__main__":
    main()