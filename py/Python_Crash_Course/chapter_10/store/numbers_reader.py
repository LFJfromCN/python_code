import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)  #这里我们使用json.load( )将numbers.json中的数据加载到内存中

print(numbers)
