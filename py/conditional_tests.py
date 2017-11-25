car = 'Audi'
print(car =='audi')
print(car.lower()=='audi')

print(1>3)
print(1<10)
print(1!=8)

print((1<4) and (1!=6))
print((3<7) or (4>=9))

names=['Lily','mary','bob','lincoln']
name='Lily'
if name in names:
    print(name.title())

new='rose'
if new not in names:
    names.append(new)
    print(names)
