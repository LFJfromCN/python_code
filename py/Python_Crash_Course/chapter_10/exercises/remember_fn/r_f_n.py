import json

def get_num( ):
    '''获取用户最喜欢的数字'''
    favorite_num = input('What is your favorite number?')
    filename = 'favorite_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(favorite_num,f_obj)
        print('Got it! ')

def print_num( ):
    '''向用户显示他或她最喜欢的数字'''
    filename = 'favorite_num.json'
    try:
        with open(filename) as f_obj:
            fn = json.load(f_obj)
    except FileNotFoundError:
        get_num( )
        with open(filename) as f_obj:
            fn = json.load(f_obj)

    print("I know your favorite number! It's " + fn + " . ")

print_num( )
