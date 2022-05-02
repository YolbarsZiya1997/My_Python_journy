class User:
    """ make a user class """
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"\nFirst name: {self.first_name}, Last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        print(f"\nHello {self.username}, welcome back")
        
    def increment_logint_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    
ziya = User("Ziya", "Alim", "Şungkar", "ziyabay135@gmail.com", "Zeytinburnu")
ziya.increment_logint_attempts()
ziya.increment_logint_attempts()
ziya.increment_logint_attempts()
print(f"Total login attempts are: {ziya.login_attempts}")

ziya.reset_login_attempts()
print(f"How about now ? : {ziya.login_attempts}")
    