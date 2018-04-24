from die import Die
import pygal

#创建一个D6和一个D10
die_1 = Die( )
die_2 = Die(10)

#投掷色子多次，并将结果储存在一个列表中
results = [ ]
for roll_num in range(50000):
    result = die_1.roll( ) + die_2.roll( )
    results.append(result)

#分析结果
frequencies = [ ]
max_num = die_1.num_sides + die_2.num_sides
for value in range(2, max_num+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#可视化结果
hist = pygal.Bar( )

hist.title = 'Results of rolling a D6 and a D10 50000 times'
hist.x_labels = [x for x in range(2, max_num+1)]
##for i in range(2, max_num+1):
##    hist.x_labels.append(i)

hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('D6_and_D10.svg')
