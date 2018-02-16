class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

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

user0 = User('tom', 'brain')
user0.describe_user()
user0.greet_user()

user1 = User('tony', 'jackman')
user1.describe_user()
user1.greet_user()

user2 = User('fujing', 'li')
user2.describe_user()
user2.greet_user()

user3 = User('tingting', 'xu')
user3.describe_user()
user3.greet_user()

user4 = User('huiqing', 'li')
user4.increment_login_attempts(1)
user4.describe_user()
user4.greet_user()
user4.reset_login_attempts()    #将user4的登录尝试次数重设为0
print('User4 的登录尝试次数被重设为：' + str(user4.login_attempts))
