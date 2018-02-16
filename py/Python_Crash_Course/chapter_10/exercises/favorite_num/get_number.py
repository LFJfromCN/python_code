import json

def get_num( ):
    '''获取用户最喜欢的数字'''
    favorite_num = input('What is your favorite number?')
    filename = 'favorite_num.json'
    with open(filename, 'w') as f_obj:
        json.dump(favorite_num,f_obj)
        print('Got it! ')

get_num( )
        
