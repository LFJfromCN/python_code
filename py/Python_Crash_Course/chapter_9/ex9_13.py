from collections import OrderedDict

vocabulary = OrderedDict( )

vocabulary['list'] = 'A list is a date structure that holds on an ordered collection of items.'
vocabulary['tuple'] = 'Tuples are used to hold together multiple objects.'
vocabulary['for'] = 'The for ... in loop statement is another looping statement which iterates over a sequence of objects.'
vocabulary['if'] = 'The if statement is used to check a condition:if the conition is true, we run a block of statements, else we just jump over them.'
vocabulary['string'] = 'A string is a seqeunce of character. Strings are basically just a bunch of words.'

for term in vocabulary:
    print(term.title( ) + "  : " + vocabulary[term])
    
    
