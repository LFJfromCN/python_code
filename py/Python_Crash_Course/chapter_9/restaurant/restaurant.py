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
        
