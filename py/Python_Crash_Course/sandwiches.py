sandwich_orders = ['Cemita','Doubles','Fischbrötchen','Dagwood']
finished_sandwiches = [ ]
while sandwich_orders:
    san = sandwich_orders.pop()
    finished_sandwiches.append(san)

for sandwich in finished_sandwiches:
    print('We made your ' + sandwich + ' sandwich.')

print(sandwich_orders)
print(finished_sandwiches)

