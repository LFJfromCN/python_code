def build_person(firstname,lastname,age = ' '):
    '''返回一个包含一个人信息的字典'''
    person = {'first':firstname,'last':lastname}
    if age:
        person['age'] =age  #age是一个可选的参数，没有给定的话默认值为空字符
    return person       #返回一个字典
musician = build_person('jimi','hendrix',age = 27)
print(musician)
ceo = build_person('steve','jobs')
print(ceo)
