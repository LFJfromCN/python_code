poem ='''\
Programming is fun
When the work is done
If you wanna make your work also fun:
    use python!
'''
f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line#python3.xÖÐÎªprint(line,end=' ')
f.close()
