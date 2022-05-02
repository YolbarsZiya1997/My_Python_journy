class User:
    """ make a user class """
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        
    def describe_user(self):
        print(f"\nFirst name: {self.first_name}, Last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        print(f"\nHello {self.username}, welcome back")
        
        
babur = User("Ziya", "Alim", "Kökböre", "ziyabay135@gmail.com", "Zeytinburnu")
babur.describe_user()
babur.greet_user()
    
    