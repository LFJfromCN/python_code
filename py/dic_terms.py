voca = {
    'list':'A list is a data structure that holds an ordered collection of items.',
    'tuple':'Tuples are used to hold together multiple objects.',
    'for':'The for...in loop statement is another looping statement which iterates over a sequence of objects.',
    'if':'The if statement is used to check a conditon:if the condition is true,we run a block of statements,else we process another block of statements.',
    'string':'A string is a sequence of characters.Strings are basically just a bunch of words.',
    }

for item in voca:
    print(item + ' : ' + voca[item])
    print('\n')

for K,V in voca.items():
    print(K + ' : ' +V)
    print('\n')
