"""         
class User:
    #Create an user profile#
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
        
class Admin(User):
    #Create an admin user#
    def __init__(self, user_name, first_name, last_name, email, location):
        #Initialize the Admin class#
        super().__init__(user_name, first_name, last_name, email, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print("The privileges are:")
        for priv in self.privileges:
            print(f"- {priv}")
            
admin_user = Admin("Barskhan", "Ziya Alim", "Şungkar", "ziyabay135@gmail.com", "Zeytinburnu")
admin_user.show_privileges()
"""

"""Admin class with privileges as a separate class"""
class User:
    #Create an user profile#
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
        
class Privileges:
    #Initialize the privilege class#
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        #privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges
        
        
    def show_privileges(self):
        print("The privileges of being an admin are: ")
        for priv in self.privileges:
            print(f"- {priv}")

class Admin(User):
    #Create an admin user#
    def __init__(self, user_name, first_name, last_name, email, location):
        #Initialize the Admin class#
        super().__init__(user_name, first_name, last_name, email, location)
        self.privilege = Privileges()
        
        
admin_user = Admin("Barskhan", "Ziya Alim", "Şungkar", "ziyabay135@gmail.com", "Zeytinburnu")
admin_user.privilege.show_privileges()