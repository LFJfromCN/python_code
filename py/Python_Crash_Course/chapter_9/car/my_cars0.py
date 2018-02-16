import car    #这里导入了整个car模块

my_beetle = car.Car('volkswagen', 'beetle', 2016)   #module_name.class_name来访问需要的类
print(my_beetle.get_descriptive_name( ) )

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name( ))
