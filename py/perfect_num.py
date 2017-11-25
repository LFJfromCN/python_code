a = range(1,1001)
b = []
for n in a:
    i = range(1,n+1)
    for i0 in i:
        if (n%i0 ==0 ):
            b = [i]

s = 0
for i in b:
    s=s+i0

if(s==n):
    print('%d is a perfet number')
