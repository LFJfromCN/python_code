for n in range(1,1001):
    sum0 = 0
    for i in range(1,n):
        if n%i == 0:
            sum0 = sum0 + i
    if sum0 == n:
        print(n)
            
    
