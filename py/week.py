# printing a weekday depends on users' input
week = "一二三四五六日"
w = eval(input())
print("星期" + week[w - 1])
while 0<w<8:
    w = eval(input())
    print("星期" + week[w - 1])
