from random import randint

class Die( ):
    '''一次模拟骰子的简单尝试'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, frequency):
        self.frequency = frequency
        for i in range(1, frequency+1):
            side = randint(1, self.sides)
            print(str(i) + ' We got ' + str(side) + ' this time!')
        print('\n')
        
die = Die(6)    #投掷一个6面的骰子10次
die.roll_die(10)

die10 = Die(10)     #投掷一个10面的骰子10次
die10.roll_die(10)

die20 = Die(20)     #投掷一个20面的骰子10次
die20.roll_die(10)
