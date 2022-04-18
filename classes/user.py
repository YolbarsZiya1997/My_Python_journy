class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Create a user profile"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location.title()
        
    def describe_user(self):
        """Display a summary of the user's information"""
        print(f" \n {self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
        
    def greet_user(self):
        """Display a personalize greeting to the user"""
        print(f"\nWelcome back, {self.username}!")
        
ziya = User('Ziya', 'Alim', 'Kökböre', 'ziyabay135@gmail.com', 'Zeytinburnu')
ziya.describe_user()
ziya.greet_user()
        