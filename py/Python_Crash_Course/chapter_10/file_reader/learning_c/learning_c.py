filepath = 'learning_python.txt'

with open(filepath) as fo:
    lines = fo.readlines( )

for line in lines:
    new = line.replace('python', 'C')
    print(new.rstrip( ))
    
