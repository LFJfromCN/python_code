ordinal_nums = [1,2,3,4,5,6,7,8,9]
for o in ordinal_nums:
    a = str(o)
    if o == 1:
        print(a+'st')
    elif o == 2:
        print(a+'nd')
    elif o == 3:
        print(a+'rd')
    else:
        print(a+'th')
