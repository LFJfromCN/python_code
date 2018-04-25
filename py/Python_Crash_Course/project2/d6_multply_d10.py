import pygal
from die import Die

#创建一个D6和一个D10实例
die_1 = Die( )
die_2 = Die(10)

#投掷色子多次，并将结果储存在一个空列表中
results = [ ]
for roll_num in range(1000000):
    result = die_1.roll( ) * die_2.roll( )
    results.append(result)

sore_results = sorted(set(results))

#分析结果
frequencies = [ ]
max_num = die_1.num_sides * die_2.num_sides
for result in sore_results:
    frequency = results.count(result)
    frequencies.append(frequency)

#结果可视化
hist = pygal.Bar( )

hist.title = 'Results of rolling a D6 and a D10 1000000 times, and multiply their results'
hist.x_labels = [result for result in sore_results]

hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6*D6', frequencies)
hist.render_to_file('D6_multply_D6.svg')
    
