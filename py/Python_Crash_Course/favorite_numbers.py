favorite_numbers = {
    'adam':[1,5,78],
    'cooper':[2,5,45],
    'anna':[4,5,666],
    }
for K,V in favorite_numbers.items():
    print(K.title() + " 's favorite numbers are: ")
    for num in V:
          print(num)
    print('\n')
