def make_pizza(*toppings):
    '''打印客户点的所有配料，并概述要制作的比萨'''
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
