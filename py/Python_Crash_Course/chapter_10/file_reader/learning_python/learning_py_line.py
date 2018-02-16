filename = 'learning_python.txt'

with open(filename) as fo:
    for line in fo:
        print(line.rstrip( ))
