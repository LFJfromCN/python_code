filename = 'little_women.txt'
with open(filename) as fo:
    contents = fo.read( )
    words = contents.split( )
 #方法一   
counter = 0
for word in words:
    if word.lower( ) == 'the':
        counter = counter + 1

print('在' + filename + ' 中，' + " 'the' 出现了 " + str(counter) + ' 次。') 
        
#方法二不适用于列表
count = contents.lower( ).count('the')
print(count)
