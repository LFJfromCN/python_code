def des_pet(pet_name,animal_type = 'dog'):
    print('\nI have a ' + animal_type + ' . ')
    print("My " + animal_type + " 's name is " + pet_name.title() +" . ")

des_pet(pet_name = 'white')
des_pet('white')
des_pet('white','cat')
