number = 21
running = True

while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('yes')

        running = False
    elif guess < number:
        print('no,too small')
    else:
        print('no,too big')

print('Done')
