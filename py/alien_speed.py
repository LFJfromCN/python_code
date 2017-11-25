alien_1 = {'x_position':0,'y_position':25,'speed':'fast'}
print('Original x_position:  ' + str(alien_1['x_position']))


if alien_1['speed'] == 'slow':
	x_increment = 1
elif alien_1['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

	
alien_1['x_position'] = alien_1['x_position'] + x_increment
print('New x_position '+ str(alien_1['x_position']))
