"""A module containing user, privileges and admin model classes."""

class User:
    """Model of a user."""
    def __init__(self, first_name, last_name):
        """Initializing attributes of user."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = 'india'
        self.gender = 'male'
        self.age = 18
        self.login_attempts = 0
    
    def describe_user(self):
        """Print a summary of user's introduction."""
        print(f"User: {self.first_name.title()} {self.last_name.title()}\n\tLocation: {self.location.title()}\
        \n\tGender: {self.gender.title()}\n\tAge: {self.age} years")
    
    def greet_user(self):
        """Greet the user."""
        print(f"\nHi {self.first_name.title()} {self.last_name.title()}. Welcome with us.")
        
    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0
        
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
          