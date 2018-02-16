e = 1
while(e):
    try:
        a = input('请输入一个数字：')
        if int(a) != 0:
            e = 0
        else:
            break
    except ValueError:
        print('您输入的好像不是数字哦！请重试。')

f = 1
while(f):
    try:
        b = input('请输入另一个数字：')
        if int(b) != 0 :
            f = 0
        else:
            break
    except ValueError:
        print("您输入的好像不是数字啊！请重试。")

c = int(a) + int(b)
print('这两个数之和为：' + str(c))

