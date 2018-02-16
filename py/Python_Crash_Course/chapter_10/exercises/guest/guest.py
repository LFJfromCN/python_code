guest = input('Please enter your name: ')
filename = 'guests.txt'
with open(filename, 'a') as file_object:
    file_object.write(guest)
