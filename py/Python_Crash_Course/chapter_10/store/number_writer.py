import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj: #这里我们新建一个名为numbers.json的文件
    json.dump(numbers, f_obj)   #这里我们使用json.dump( )将列表numbers中的数据存储到numbers.json中
