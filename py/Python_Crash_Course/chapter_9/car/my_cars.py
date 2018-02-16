from car import Car, ElectricCar    #可以从一个文件中同时导入多个类，用逗号分隔

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name( ))

my_tesla1 = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla1.get_descriptive_name( ) )
