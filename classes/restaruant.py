class Restaurant:
    """ A simple attempt to model a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and its cuisine"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe what type of delicacy the restaurant offers """
        print(f'The name of the restaurant is {self.name}')
        print(f'It serves {self.cuisine_type} cuisine')

    @staticmethod
    def open_restaurant():
        print('The restaurant is open')


fav_restaurant = Restaurant('Zafer', 'Uighur')
fav_restaurant.describe_restaurant()
fav_restaurant.open_restaurant()

best_chicken = Restaurant('Saruhan', 'Turkish')
best_chicken.describe_restaurant()
best_chicken.open_restaurant()

kelle_pacha = Restaurant('Ziyafet', 'Middel Eastern')
kelle_pacha.describe_restaurant()
kelle_pacha.open_restaurant()
