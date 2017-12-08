while True: 
    age =input('Please enter your age, then I will give you the price, enter "q" to quit: ')
    if age == 'q':
        break
            
    if int(age)< 3:
        print('Your ticket is free!')
    elif int(age) >= 3 and int(age) <= 12:
        print('Your ticket is 10 dollars.')
    else:
        print('Your ticket is 15 dollars.')

  
