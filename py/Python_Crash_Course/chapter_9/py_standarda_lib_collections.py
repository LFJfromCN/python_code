from collections import OrderedDict    #这是一个有序字典类

favorite_languages = OrderedDict( )

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
favorite_languages['fujing li'] = 'python'

for name, language in favorite_languages.items():
    print(name.title( ) + " 's favorite language is " +
          language.title( ) + " . ")
    
