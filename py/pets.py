dog_tom = {
'type':'dog',
'master':'jim linclon',
'name':'tom',
}

cat_lily = {
'type':'cat',
'master':'rose reily',
'name':'lily',
}

pets = [dog_tom,cat_lily]
for pet in pets:
        for K,V in pet.items():
                print(K + ' : ' + V.title())
        print('\n')
