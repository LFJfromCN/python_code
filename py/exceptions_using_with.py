import time
with open('poem.txt') as f:
    for line in f:
        time.sleep(1)
        print line
