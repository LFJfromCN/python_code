import json

def get_stored_username( ):
    '''如果储存了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None    #如果filename不存在则不返回任何东西，让get_new_username( )
                                    #去获取新的用户名，各司其职
    else:
        return username
        

def get_new_username( ):
    '''提示用户输入用户名'''
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
    return username    #why

def greet_user( ):
    '''问候用户，并指出其名字'''
    username = get_stored_username( )   #在greet_user( )中调用gsu( )
    if username:
        print('Welcome back, ' + username + ' ! ')
    else:
        username = get_new_username( )  #在greet_user( )中调用gny( )
        print('We will remember you when you come back, ' + username + ' ! ')

greet_user( )
         
