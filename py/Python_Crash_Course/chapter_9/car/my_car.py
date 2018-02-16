from car import Car    #让Python打开模块car，并导入其中的类Car。
                                        #将类移入模块中可以使主程序简洁易于阅读

my_new_car = Car('audi','a6l', 2017)
print(my_new_car.get_descriptive_name( ))

my_new_car.odometer_reading = 23
my_new_car.read_odometer( )
