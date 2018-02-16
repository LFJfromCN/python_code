class Dog( ):     #在Python中类名约定为首字母大写
    '''初识类，一次模拟小狗的简单尝试'''   #描述该类的作用

    def __init__(self, name, age):      #定义一个方法，是一个特殊的函数
        '''初始化属性name和age''' #这里的形参self必不可少，且一定要在最前面。
        self.name = name                #self是一个指向实例本身的引用，让实例能够访问类中的属性和方法
        self.age = age                      #这里的name和age我们称之为属性

    def sit(self):
        '''模拟小狗蹲下'''
        print(self.name.title() + ' is now sitting. ')

    def roll_over(self):
        '''模拟小狗打滚'''
        print(self.name.title() + ' rolled over! ') #这里的两个函数的形参都是self，以self为前缀的变量都可以供类中的所有方法使用。
                                                                            #我们还可以通过类的任何实例来访问这些变量

my_dog = Dog('bibble', 3)   #这是一个实例，给Dog类赋予个性

print("My dog's name is " + my_dog.name.title() + ' . ')    #这里使用点句表示法访问属性
print("My dog is " + str(my_dog.age) + ' years old.')
my_dog.sit()
my_dog.roll_over()    #调用方法

your_dog = Dog('tom', 2)  #可以同时创建多个实例
print("\nYour dog's name is " + your_dog.name.title())
print('Your dog is ' + str(your_dog.age) + ' years old. ')
your_dog.sit()
your_dog.roll_over()
