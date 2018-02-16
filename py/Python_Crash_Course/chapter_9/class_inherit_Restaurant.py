class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.type = cuisine_type
        self.num_served = 0
        self.flavors = ['chocolate','vanilla','strawberry','blueberry','teaberry']

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.name + ' . ')
        print('The cuisine type is ' + self.type + ' . ')
        print('We have served ' + str(self.num_served) + ' people. ')

    def open_restaurant(self):
        print('We are opening now![from 9:00AM~10:00PM] ')

    def set_num_served(self, num):
        self.num_served = num

    def increment_num_served(self, number):
        self.num_served = self.num_served + number
        

class IceCreamStand(Restaurant):
    '''一次对冰淇淋小店的简单模拟的尝试'''
    def __init__(self, restaurant_name, cuisine_type):
        '''初始化父类的属性'''
        super( ).__init__(restaurant_name, cuisine_type)

    def show_flavors(self):
        print('We have following flavors: ')
        for flavor in self.flavors:
            print(flavor)
        print('Which one do you like? ')


icecream = IceCreamStand("billy's",'for all')
icecream.show_flavors( )
icecream.set_num_served(50)
icecream.describe_restaurant( )
icecream.open_restaurant( )
icecream.increment_num_served(100)
icecream.describe_restaurant( )
icecream.open_restaurant( )
