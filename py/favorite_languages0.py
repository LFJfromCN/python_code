favorite_languages0 = {
    'jen':['python','ruby','C'],
    'sarah':['C','ruby','FORTRAN'],
    'edward':['go','c++'],
    'phil':['python','ADA','Lisp'],
    'tom':['go'],
    }

for name,languages in favorite_languages0.items():
    if len(languages) != 1:
        print('\n' + name.title() + " 's favorite languages are: ")
        for language in languages:
            print('\t' + language.title())
    else:
        print('\n' + name.title() + " 's favorite language is: " )
        for language in languages:
            print('\t' + language.title())
