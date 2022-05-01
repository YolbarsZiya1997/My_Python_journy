class Restaurant:
    """ Describe a restaurant""" 
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """ Describe the restaurant"""
        discrition = f"{self.name} serves wonderful {self.cuisine_type} cuisine"
        print(f"{discrition}")
        
    def open_restaurant(self):
        """ Invites the guests in"""
        invitation = f"{self.name} is opened, come on in"
        print(f'{invitation}')
        
    def set_number_served(self, servings):
        """ Update the served servings"""
        self.number_served = servings
        print(f"The restaurant have served {self.number_served} services.")
        
    def increment_number_served(self, serves):
        """ Increments the servings"""
        self.number_served += serves
        
my_favorite =  Restaurant('Zafer', 'Uighur')
my_favorite.describe_restaurant()
my_favorite.set_number_served(75)
my_favorite.increment_number_served(4000)
print(f"Total number of service : {my_favorite.number_served}")

        
    