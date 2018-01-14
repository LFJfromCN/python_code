magicians = ['liu qin','li fujing','li huaiqing']
a = []

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician.title())

def great_magicians(magician_names,a):
    while magician_names:
        b = 'the Great ' + magician_names.pop()
        a.append(b)                     #这里列表a即是列表magicians 的副本
        
show_magicians(magicians)
print('\n')
great_magicians(magicians[ : ],a)#为了不改变列表magicians，使用切片向函数传递副本
show_magicians(magicians)
print('\n')
show_magicians(a)


        
    
    
