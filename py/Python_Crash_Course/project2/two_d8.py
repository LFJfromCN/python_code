import pygal
from die import Die

#创建两个个D8
die_1 = Die(8)
die_2 = Die(8)

#投掷色子多次，并将结果储存在一个列表中
results = [ ]
for roll_num in range(1000):
    result = die_1.roll( ) + die_2.roll( )
    results.append(result)

#结果分析
frequencies = [ ]
max_num = die_1.num_sides + die_2.num_sides
for value in range(2, max_num+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#结果可视化
hist = pygal.Bar( )
hist.title = 'Results of rolling two D8 1000 times.'
hist.x_labels = [x for x in range(2, max_num+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D8+D8', frequencies)
hist.render_to_file('two_d8.svg')
