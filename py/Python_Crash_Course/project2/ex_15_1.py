import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=30)

#设置图表的标题并给坐标轴加上标签
plt.title('Cube numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 5100, 0, 50000000000])

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show( )
