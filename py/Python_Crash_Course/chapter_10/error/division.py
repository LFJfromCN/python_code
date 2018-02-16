print("Give me two numbers, and I'll divide them. ")
print('Enter "q" to quit. ')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    try:    #try里面的代码块是可能出错的代码块，如果没有出错则执行else
       answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
