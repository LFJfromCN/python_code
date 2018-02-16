from user import User

class Privileges( ):
    '''一个模拟管理员权限的类'''
    def __init__(self, privileges=['can add post','can delete user','can ban user']):
        self.privileges = privileges

    def show_privileges(self):
            print("Your privileges are as follows: ")
            for privilege in self.privileges:
                print(privilege)

class Admin(User):
    '''一次模拟管理员的简单尝试'''
    def __init__(self, first_name, last_name):
        super( ).__init__(first_name, last_name)
        self.privilege = Privileges( )  #将一个Privileges( )类的实例作为Admin( )的属性

