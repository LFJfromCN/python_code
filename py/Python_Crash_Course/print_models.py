unprinted_designs = ['iphone case','robot pendant','dodecahedron','spaceship']
completed_models = [ ]
print(unprinted_designs)
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print('\nPrinting model: ' + current_design)
    completed_models.append(current_design)

print('\nThe following models have been printed: ')
for completed_model in completed_models:
    print(completed_model)
