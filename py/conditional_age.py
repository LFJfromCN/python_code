print('Please input an age: ')
input0 = int(input())
if input0 < 2:
    print('He is a baby.')
elif input0 < 4:
    print('He is learning to walk.')
elif input0 < 13:
    print('He is a child')
elif input0 < 20:
    print('He is a teenager.')
elif input0 < 65:
    print('He is an adult')
else:
    print('He is an old man.')
