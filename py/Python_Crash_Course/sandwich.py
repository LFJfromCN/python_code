def sandwich(*includings):
    '''对客户要求在三明治中添加的食材进行概述'''
    print('\nYour sandwich includes the followings materials: ')
    for including in includings:
        print('- ' + including)

sandwich('fish')
sandwich('fish', 'mushrooms', 'cheese', 'lettuce')
