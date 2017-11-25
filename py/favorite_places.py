favorite_places = {
    'tom':['New York City','San Francisco'],
    'bob':['Los angeles','Tokyo','Seattle'],
    'Sophia':['Berkeley','London','Αθήνα'],
    }

for K,V in favorite_places.items():
    print(K.title() + " 's favorite places : ")
    for place in V:
        print(place)
    print('\n')
