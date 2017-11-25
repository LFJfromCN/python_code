x = 50



def func( ):
    global x    #用来声明x是一个全局变量

    print('x is', x)
    x = 2
    print('Changed global x to', x)



func( )
print('Value of x is', x)
