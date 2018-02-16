import json

def print_num( ):
    '''向用户显示他或她最喜欢的数字'''
    filename = 'favorite_num.json'
    try:
        with open(filename) as f_obj:
            fn = json.load(f_obj)
    except FileNotFoundError:
        print('我找了好久，文件不存在啊！')
    else:
          print("I know your favorite number! It's " + fn + " . ")

print_num( )
