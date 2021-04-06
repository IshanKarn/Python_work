# employee.py

class Employee:
    """A simple employee class."""
    
    def __init__(self, first, last, salary):
        """Initialize attributes of the Employee class."""
        self.first_name = first.title()
        self.last_name = last.title()
        self.annual_salary = salary
        
    def give_default_raise(self):
        """Give a default raise of $5000 to the annual salary.."""
        self.annual_salary += 5000
            
    def give_custom_raise(self, increment):
        """Give a custom raise to the annual salary."""
        self.annual_salary += increment