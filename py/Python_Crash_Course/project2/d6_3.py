import pygal
from die import Die

#创建三个D6
die_1 = Die( )
die_2 = Die( )
die_3 = Die( )

#投掷多次这三个色子，并统计结果
results = [ ]
for roll_num in range(10000):
    result = die_1.roll( ) + die_2.roll( ) + die_3.roll( )
    results.append(result)

#分析结果
frequencies = [ ]
max_num = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_num+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#结果可视化
hist = pygal.Bar( )

hist.title = 'Result of rolling 3 D6 10000 times.'
hist.x_labels = [x for x in range(3, max_num+1)]

hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('3 D6', frequencies)
hist.render_to_file('d6_3.svg')
