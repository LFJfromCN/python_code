filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip( ))   #使用方法rstrip( )来除去空行
        

