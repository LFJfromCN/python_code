listone = [2,3,4,4,7,5,8,1]
listtwo = [2*i for i in listone if i>2]
list3 = [i**2 for i in listtwo if i>10]

print(listtwo)
print(list3)
