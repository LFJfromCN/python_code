from random import choice

class RandomWalk( ):
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=50000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        #所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """一个用于确定每次漫步的方向和距离的方法"""
        #决定前进方向以及沿着这个方向前进的距离
        direction = choice([1, -1])   #1向右走，-1向左走
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])    #随机地在该列表中选择一个数
        step = direction * distance

        return step
        

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            x_step = RandomWalk.get_step(self)
            y_step = RandomWalk.get_step(self)

            #拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue

            #计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


