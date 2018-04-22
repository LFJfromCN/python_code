from random import randint

class Die():
    """一个对骰子进行模拟的类"""

    def __init__(self, num_sides=6):
        """这是一个六个面的普通骰子"""
        self.num_sides = num_sides

    def roll(self):
        """摇色子，返回一个位于1至色子面数之间的随机整数"""
        return randint(1, self.num_sides)
    
