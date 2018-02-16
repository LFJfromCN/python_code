import json

def greet_user( ):
    '''代码的重构。问候用户，并指出其名字'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input('What is your name? ')
        with open(filename, 'w') as f_obj:
            json.dunp(username, f_obj)
            print('We will remember you when you come back, ' +
                  username + ' ! ')
    else:
        print('Welcome back, ' + username + ' ! ')

greet_user( )

        
