class User:
    "Create an user profile "
    def __init__(self, user_name, first_name, last_name, email, location):
        self.user_name  = user_name
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email
        self.location   = location
        self.login_attempts = 0
    
        
    def descrine_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"User name: {self.user_name}")
        print(f"Email Address: {self.email}")
        print(f"Location: {self.location}")
        
    def greet_user(self):
        print(f"\nWelcome back {self.user_name}")
    
    def read_attempts(self):
        print(f"Attempt to login: {self.login_attempts}")
        
    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
my_account = User("Kökböre", "Ziya", "Şungkar", "ziyabay135@gmail.com", "Zeytinburnu")
my_account.descrine_user()    
my_account.increment_login_attempts(50)
my_account.increment_login_attempts(120)
my_account.read_attempts()
my_account.reset_login_attempts()
my_account.read_attempts()
        
    