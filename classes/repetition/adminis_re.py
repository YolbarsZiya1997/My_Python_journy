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


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("All the admin privileges:")
        for privilege in self.privileges:
            print(f'\t-{privilege}')


class Admin(User):
    """ A representation of the admin class"""

    def __init__(self, first_name, last_name, username, email, location):
        """ Initialize the class"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


ziya = Admin('Ziya', 'Alim', 'Şungkar', 'ziyabay135@gmail.com', 'Zeytinburnu')
ziya.privileges.privileges = ["can add post", "can delete post", "can ban user"]
ziya.privileges.show_privileges()
