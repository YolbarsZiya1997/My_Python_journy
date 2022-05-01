class Restaurant:
    """ Describe a restaurant""" 
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """ Describe the restaurant"""
        discrition = f"{self.name} serves wonderful {self.cuisine_type} cuisine"
        print(f"{discrition}")
        
    def open_restaurant(self):
        """ Invites the guests in"""
        invitation = f"{self.name} is opened, come on in"
        print(f'{invitation}')
        
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize the class"""
        super().__init__(name, cuisine_type)
        self.flavor = []
        
    def display_flavor(self):
        print(f'Those are the flavors:')
        for flavor in self.flavor:
            print(f'\t-{flavor}')
        
my_fav = IceCreamStand('Zafer', 'ice_cream')
my_fav.flavor = ['Cream', 'Chocolate', 'Cramberry', 'Lemon', 'Strawberry']
my_fav.display_flavor()
