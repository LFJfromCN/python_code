def count_words(filename):
    '''计算一个文件大致包含多少个单词，包括标点符号'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read( )
    except FileNotFoundError:
        pass    #出现异常时直接跳过，而不告诉用户
    else:
        #计算文件大致包含多少个单词
        words = contents.split( )
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) +
                  'words. ')

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'Chinese_new']
for filename in filenames:
    count_words(filename)
