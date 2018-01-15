def build_profile(first, last, **user_info):
    '''创建一个字典，其中包含我们知道的关于用户的一切'''
    profile = {}                    #创建一个名为profile的空字典
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()

    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                                                 location = 'princeton',
                                                 field = 'physics') #调用build_profile()函数将字典profile返回,
                                                                                #存储在user_profile中

print(user_profile)

user = build_profile('fujing', 'li',
                                    location = 'dali',
                                     file = 'computer science',
                                     hobby = 'biking',
                                     age = '21')        #关于我，习题8-13
print(user)
