filename = 'reasons.txt'
with open(filename, 'a') as file_object:
    reason = ' '
    while(reason != 'q'):
        reason = input('Please enter your reasons why do you like programming: '+
                                   '(enter "q" to quit)\n')
        if reason != 'q':
            file_object.write(reason + '\n')
        else:
            break
        
