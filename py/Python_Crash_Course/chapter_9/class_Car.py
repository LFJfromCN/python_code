class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0    #在此处为属性赋值时则无需声明该形参

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' +self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条汽车的里程信息'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it. ')

    def update_odometer(self, mileage):    #使用方法来修改属性的值，方法二
        '''将里程表读数设置为指定的值，并且禁止将里程表读数往回调'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll back an odometer! ')

    def increment_odometer(self, miles):    #使用方法对属性的值进行递增，方法三
         '''将里程表的读数增加特定的增量'''
         if miles >=0:
             self.odometer_reading += miles
         else:
             print('You cannot roll back an odometer! ')
            

my_new_car = Car('audi', 'a6l', 2014)
print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 23    修改属性的值的方法一
my_new_car.update_odometer(45)
my_new_car.read_odometer()
print('\n')
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
