filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')   #当该文件不存在时将自动创建
    file_object.write('I love creating new apps.\n') #就像在屏幕上打印一样，输出到文件中时也可以使用各种转义字符
