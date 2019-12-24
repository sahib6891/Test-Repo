import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass\n")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Sahib", "Singh", 50000)
        self.emp_2 = Employee("Davinder", "Singh", 60000)

    def tearDown(self):
        print("tearDown\n")

    def test_email(self):
        print("Test email")
        self.assertEqual(self.emp_1.email, "Sahib.Singh@email.com")
        self.assertEqual(self.emp_2.email, "Davinder.Singh@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Singh@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Singh@email.com")

    def test_fullname(self):
        print("Test FullName")
        self.assertEqual(self.emp_1.fullname, "Sahib Singh")
        self.assertEqual(self.emp_2.fullname, "Davinder Singh")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Singh")
        self.assertEqual(self.emp_2.fullname, "Jane Singh")

    def test_apply_raise(self):
        print("Test Raise Logic")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == "__main__":
    unittest.main()
