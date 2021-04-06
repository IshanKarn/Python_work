# ice_cream_stand.py

"""A module having class to model a resataurant."""
class Restaurant:
    """Simple model of a Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing attributes for restaurants."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.flavors = ['vanilla', 'chocolate', 'cookies N cream', 'mint chocolate chip', 'buttered pecon', 'strawberry']

    def describe_restaurant(self):
        """Describing restaurant name and cuisine type."""
        print(self.restaurant_name)
        print(self.cuisine_type)
        
    def open_restaurant(self):
        """Show the status of restaurant -i.e.- open/close."""
        print(f"The restaurant {self.restaurant_name} is open.")
        
    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        if number > self.number_served:
            self.number_served = number
        else:
            print("Number of customers cann't be rolled back.")
        
    def increment_number_served(self, increment):
        """Increment the number of customers who’ve been served."""
        if increment > 0:
            self.number_served += increment
        else:
            print("Number of customers cann't be decreased.")
            
    def displayIceCreamFlavors(self):
        """Display flavors of ice cream."""
        print("Following flavors are available:")
        for flavor in self.flavors:
            print(f'\t{flavor}')