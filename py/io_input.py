def reverse(text):
    return text[ : :-1]#全切片，负步长

def is_palindrome(text):
    return text == reverse(text)
"""如果将它翻转后还和原来的字符串相同，那么他就是回文"""
something = input('Enter text:')
if is_palindrome(something):
    print('Yes,it is a palindrome')
else:
    print('No,it is not a palindrome')
