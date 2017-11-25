available_toppings = ['mushroom','olives','green peppers','pepperoni','pineapple',
		      'extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Add '+ requested_topping +'.')
    else:
        print('Sorry we do not have '+requested_topping+'.')

print('\nFinished your pizza.')
