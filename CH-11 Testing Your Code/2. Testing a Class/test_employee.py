# test_employee.py

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test of Employee class."""
    
    def setUp(self):
        """Create instance for use by all test methods."""
        self.test_employee = Employee('achintya', 'tyagarajan', 50000)
    
    def test_give_default_raise(self):
        """Is default raise of $5000 given properly?"""
        salary = self.test_employee.annual_salary
        self.test_employee.give_default_raise()
        self.assertEqual((salary + 5000), self.test_employee.annual_salary)
        
    def test_give_custom_raise(self):
        """Is custom raise to annual salary given properly?"""
        salary = self.test_employee.annual_salary
        increment = 12000
        self.test_employee.give_custom_raise(increment)
        self.assertEqual((salary + increment), self.test_employee.annual_salary)
        
if __name__ == '__main__':
    unittest.main()