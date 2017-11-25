favorite_fruits = ['banana','apple','cherry','orange']
if 'banana' in favorite_fruits:
    print('You really like bananas.')

if 'cherry' in favorite_fruits:
    print('You really like cherrys.')

if 'apple' in favorite_fruits :
    print('You really like apples.')

if 'orange' in favorite_fruits:
    print('You really like oranges.')
    
print('\nThis is faster.\n')

for f in favorite_fruits:
    print('You really like '+f)
