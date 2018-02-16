try:
    print(5/0)  #如果try中的代码块没有错误则跳过except中的代码块
except ZeroDivisionError:
    print("You can't divide by zero! ")

print(4/0)
