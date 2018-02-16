from car0 import Car    #ElectricCar需要访问其父类Car，因此我们直接将Car类导入该模块中

class Battery( ):
    '''一次模拟电动汽车电瓶的简单尝试'''

    def __init__(self, battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的信息'''
        print('This car has ' + str(self.battery_size) + '-KWh battery. ')

    def get_range(self):
        '''打印一条描述电瓶续航里程的信息'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge. '
        print(message)

class ElectricCar(Car):
    '''模拟电动车的独特之处'''
    def __init__(self, make, model, year):
        '''
        初始化父类的属性，再初始化电动汽车特有的属性
        '''
        super().__init__(make, model, year)
        self.battery = Battery( )
        
