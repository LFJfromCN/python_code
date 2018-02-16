class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0
        self.privileges = ['can add post','can delete post','can ban user']

    def describe_user(self):
        print("\nThis user's first name is " + self.first_name + " . ")
        print("This user's last name is " + self.last_name + " . ")

    def greet_user(self):
        print('Hello, ' + self.first_name + ' ' + self.last_name + ' . ')

    def increment_login_attempts(self, attempt):
        self.login_attempts = self.login_attempts + attempt
        print('You have attempted ' + str(self.login_attempts) + ' time(or times) to login in. ')

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    '''一次模拟管理员的简单尝试'''
    def __init__(self, first_name, last_name):
        super( ).__init__(first_name, last_name)

    def show_privileges(self):
        print(self.first_name + ' ' +  self.last_name + " ,your privileges are as follows: ")
        for privilege in self.privileges:
            print(privilege)

Admin0 = Admin('fujing','li')
Admin0.describe_user( )
Admin0.greet_user( )
Admin0.increment_login_attempts(4)
Admin0.show_privileges( )
