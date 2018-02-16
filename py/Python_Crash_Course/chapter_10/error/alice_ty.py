filename = 'alice.txt'

try:    #错误是由open( )引起的，故将其放在try代码块中
    with open(filename) as f_obj:
        contents = f_obj.read( )
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist. '
    print(msg)
else:
    #计算文件中大致包含多少个单词，仅在try中的代码块顺利执行后才执行else中的代码
    words = contents.split( )
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) + ' words. ')
    
    
