dict1 = {
    'first_name':'fujing',
    'last_name':'li',
    'location':'dali',
    }
dict2 = {
    'first_name':'huiqing',
    'last_name':'li',
    'location':'dali',
    }

people = [dict1,dict2]

for dic in people:
    for K,V in dic.items():
        print(K + ':'  + V.title())
    print('\n')
