names = ['Eric','Tom','Bob','Admin','Mary','Lily']
if names:
    for name in names:
        if name == 'Admin':
            print('Hi,Admin,would you like to see a status report?')

        else:
            print('Hello,'+name+'.')
else:
    print('We need add some names.')
