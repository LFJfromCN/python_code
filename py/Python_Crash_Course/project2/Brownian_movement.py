import matplotlib.pyplot as plt
from random_walk import RandomWalk

#只要程序处于活跃状态，就不断地模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(  )
    rw.fill_walk( )

    #设置绘制窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(500))
    plt.plot(rw.x_values, rw.y_values, c='purple', linewidth=0.8)

    #隐藏坐标轴
    plt.axes( ).get_xaxis( ).set_visible(False)
    plt.axes( ).get_yaxis( ).set_visible(False)
    plt.show( )

    keep_running = input('Make another walk?(y/n): ')
    if keep_running == 'n':
        break
