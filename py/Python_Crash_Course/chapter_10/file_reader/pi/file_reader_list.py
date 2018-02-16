filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines( )    #方法readlines( )逐行读取文件，并将其储存在一个列表中

for line in lines:
    print(line.rstrip())
