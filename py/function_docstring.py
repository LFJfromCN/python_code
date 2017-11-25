def print_max1(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.''' 
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    elif x == y:
        print('x is equal to y')
    else :
        print(y,'is maximum')

print_max1(3, 5)
print(print_max1.__doc__)    
