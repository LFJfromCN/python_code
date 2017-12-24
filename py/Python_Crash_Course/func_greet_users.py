def greet_users(names):
    '''Greet to each user in the list.'''
    for name in names:      #'names' is a list
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

users = ['lifujing','tom','lincoln']
greet_users(users)
    
