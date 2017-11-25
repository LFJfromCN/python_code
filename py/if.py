number = 28
guess = int(input('Enter an integer please : '))
if guess == number:
    print('Congratulations,you got it!')
    print('But you do ont win any gift')
elif guess < number:
        print('No,it is a little higher than that.')

else :
    print('No,it is a little lower than that.')

print('done')
