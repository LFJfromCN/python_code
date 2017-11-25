favorite_languages = {
    'tom':'c',
    'bob':'ruby',
    'sarah':'python',
    'mark':'php',
    }
print("Sarah's favorite language is "
      + favorite_languages['sarah'].title() +
      '.')
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print('\n')
friends = ['tom','bob']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print('Hi, ' + name.title() + ' I see your favorite language is ' + favorite_languages[name].title() + '!')
print('\n')
if 'eric' not in favorite_languages.keys():
    print('Eric,please take our poll.')
print('\n')

names = {
    'tom':'c',
    'tim':'c++',
    'hellen':'python',
    'mark':'php',
    'lily':'c#',
    }
for name in favorite_languages.keys():
    if name in names.keys():
        print('Welcom ' + name + '!')
    else:
        print('Join us ' + name + '!')
    
