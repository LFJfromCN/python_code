magicians = ['liu qing','li fujing','li huaiqing']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician.title())
        
show_magicians(magicians)#修改之前
print('\n')

def great_magicians(magician_names):
    for i in range(3):
        magician_names[i] = 'the Great ' + magician_names[i]
    return magician_names
 
great_magicians(magicians)
show_magicians(magicians)#修改之后
        
