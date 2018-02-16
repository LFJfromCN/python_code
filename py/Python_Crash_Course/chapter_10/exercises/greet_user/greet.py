import json

       
def get_stored_user( ):
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
       return username

    
def get_new_user( ):
    '''提示用户输入用户名'''
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
            

def greet_user( ):
    '''问候用户，并指出其名字'''
    username = get_stored_user( )
    if username:
        print('Are you ' + username + ' ?(y/n) ')
        answer = input( )
        if answer =='y':
            print('Welcome back, ' + username + ' ! ')
        else:
            username = get_new_user( )
            print('We will remember you when you come back, ' +
                 username + ' ! ')
    else:
            username = get_new_user( )
            print('We will remember you when you come back, ' +
                 username + ' ! ')


greet_user( )
