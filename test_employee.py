import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee("Sahib", "Singh", 50000)
        emp_2 = Employee("Davinder", "Singh", 30000)

        self.assertEqual(emp_1.email, "Sahib.Singh@email.com")
        self.assertEqual(emp_2.email, "Davinder.Singh@email.com")

        emp_1.first = "John"
        emp_2.first = "Jane"

        self.assertEqual(emp_1.email, "John.Singh@email.com")
        self.assertEqual(emp_2.email, "Jane.Singh@email.com")

    def test_fullname(self):
        emp_1 = Employee("Sahib", "Singh", 50000)
        emp_2 = Employee("Davinder", "Singh", 30000)

        self.assertEqual(emp_1.fullname, "Sahib Singh")
        self.assertEqual(emp_2.fullname, "Davinder Singh")

        emp_1.first = "John"
        emp_2.first = "Jane"

        self.assertEqual(emp_1.fullname, "John Singh")
        self.assertEqual(emp_2.fullname, "Jane Singh")

    def test_apply_raise(self):
        emp_1 = Employee("Sahib", "Singh", 50000)
        emp_2 = Employee("Davinder", "Singh", 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == "__main__":
    unittest.main()
