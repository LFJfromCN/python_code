with open('pi_digits.txt') as file_object:  #with能够在不需要文件时将其自动关闭
    contents = file_object.read( )
    print(contents)
