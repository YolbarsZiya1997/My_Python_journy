class Restaurant:
    """ A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
            print(f"The name of this restaurant is {self.name}")
            print(f"It serves {self.cuisine_type} cuisine")
            
            
    def set_number_served(self, servings):
            self.number_served = servings
    
    def service_reader(self):
        print(f"Number of service is {self.number_served}")
                
    def increment_number_served(self, plates):
            self.number_served += plates
        
fav_restaurant = Restaurant("Zafer", "Uighur")
fav_restaurant.describe_restaurant()
fav_restaurant.set_number_served(731)
fav_restaurant.increment_number_served(420)
print("*"*40)
fav_restaurant.service_reader()