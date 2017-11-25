#encoding=UTF-8

class ShortInputException(Exception):
    '''A exception defined by users'''
    def __init__(self,length,atleast): 
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something-->')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
    #Other work can be done well
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException:The input was ' + '{0} long,excepted at least {1}').format(ex.length,ex.atleast))
else:
    print('No exception was raised.')
