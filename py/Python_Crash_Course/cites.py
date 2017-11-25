cities = {
    'beijing':{'country':'china','population':'21710k','area':'16k m^2'},
    'new york':{'country':'american','population':'8000k','area':'1.2k m^2'},
    'tokyo':{'country':'japan','population':'13500k','area':'1.34k m^2'},
    }
for K,V in cities.items():
    print(K.title())
    for K1,V1 in V.items():
        print(K1 + ' : ' + V1.title())
    print('\n')
