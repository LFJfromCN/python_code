filename = 'learning_python.txt'

with open(filename) as fo:
    lines = fo.readlines( )

for line in lines:
    print(line.rstrip( ))
