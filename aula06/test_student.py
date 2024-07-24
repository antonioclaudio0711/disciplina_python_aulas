from unittest import TestCase

from student import Student


class TestStudent(TestCase):
    def test_calculate_average(self):
        student1 = Student(name='Renan', grades=[70, 80, 90])
        student2 = Student(name='Jorge', grades=[50, 70, 60])
        student3 = Student(name='Portela', grades=[])

        self.assertEqual(student1.calculate_average(), 80)
        self.assertEqual(student2.calculate_average(), 60)
        self.assertEqual(student3.calculate_average(), 0)

    def test_is_passing(self):
        student1 = Student(name='Renan', grades=[70, 80, 90])
        student2 = Student(name='Jorge', grades=[50, 70, 60])
        student3 = Student(name='Portela', grades=[])

        self.assertTrue(student1.is_passing())
        self.assertTrue(student2.is_passing())
        self.assertFalse(student3.is_passing())
