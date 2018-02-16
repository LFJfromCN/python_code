class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.type = cuisine_type
        self.num_served = 0

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
        

restaurant = Restaurant('big bro', 'Chinese food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

res0 = Restaurant('little lee', 'Chinese food')
res0.describe_restaurant()
res0.open_restaurant()

res1 = Restaurant('Gaga', 'Tai food')
res1.describe_restaurant()
res1.open_restaurant()

res2 = Restaurant('haha', 'Japan food')
res2.num_served = 100    #方法一
res2.describe_restaurant( )
res2.open_restaurant( )

res3 = Restaurant('pizza papa', 'USA')
res3.set_num_served(200)    #方法二
res3.describe_restaurant( )
res3.open_restaurant( )

res4 = Restaurant('xixi', 'Mexico food')
res4.increment_num_served(150)    #方法三
res4.describe_restaurant( )
res4.open_restaurant( )

