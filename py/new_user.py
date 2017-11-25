current_users = ['Tom','Bob','Adam','Rose','Kate','John']
print('Enter a username which you like: ')
new_user = input()
new_user = new_user .upper()
for current_user in current_users:
    current_user = current_user.upper()
    if new_user == current_user:
        print('Sorry, '+new_user+' was occupied,please try again.')
    else:
        print('Welcome '+new_user.title()+'.')
        break
