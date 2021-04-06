"""Module containing classes for admin and his privileges."""


"""Importong User class."""
from onlyuser import User

class Privileges:
    """A simple model of Privileges."""
    def __init__(self):
        """Initilize the attributes."""
        self.privileges = ["can add post", "can delete post", "can ban user", "can access root directory", "can configure network"]
        
    def show_privileges(self):
        """Show privileges of Admin."""
        print("Following are privileges of Admin:")
        for privilege in self.privileges:
            print(f'\t{privilege.title()}')
            
class Admin(User):
    """A simple attempt to model a Admin."""
    def __init__(self, first_name, last_name):
        """
        Initialize attributes of the parent class.
        Then, initialize attributes specific to the Admin class.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
          