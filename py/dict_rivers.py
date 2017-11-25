rivers = {
    'the Yangtse River' : 'China',
    'Mekong' : 'China,Vietnam,Laos,Tailand,Burma and Cambodia',
    'Ganges' : 'Idian',
    'Amazon' : 'Brazil',
    'Mississippi' : 'Amarica',
    }
for R,C in rivers.items():
    print(R + ' runs through ' + C + '.')
print('\n')
for river in rivers.keys():
    print(river)
print('\n')
for country in rivers.values():
    print(country)
