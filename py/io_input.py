def reverse(text):
    return text[ : :-1]#ȫ��Ƭ��������

def is_palindrome(text):
    return text == reverse(text)
"""���������ת�󻹺�ԭ�����ַ�����ͬ����ô�����ǻ���"""
something = input('Enter text:')
if is_palindrome(something):
    print('Yes,it is a palindrome')
else:
    print('No,it is not a palindrome')
