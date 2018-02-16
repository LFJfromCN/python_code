filename = 'cats.txt'
filename0 = 'dogs.txt'

try:
    with open(filename) as fo:
        lines = fo.readlines( )
except FileNotFoundError:
    print(filename +  ' 不存在啊！')
else:
    print('我们的猫：')
    for line in lines:
        print(line)

try:
    with open(filename0) as fo0:
        lines0 = fo0.readlines( )
except FileNotFoundError:
    print(filename0 + ' 不存在啊！')
else:
    print('我们的狗：')
    for line0 in lines0:
        print(line0)
