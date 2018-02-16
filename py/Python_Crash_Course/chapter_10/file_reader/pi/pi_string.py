filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines( )

pi_string = ' '
for line in lines:
    pi_string += line.strip( ) #使用一个循环将各行都加入其中

print(pi_string)
print(len(pi_string))
