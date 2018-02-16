filename = 'guestbook.txt'
with open(filename, 'a') as file_object:
    guest = 1
    while(guest != '0'):  #输入0时退出
        guest = input('Please enter your name:[输入0退出] \n')
        if guest != '0':
            file_object.write(guest.title( ) + '\n')
        else:
            break
        
