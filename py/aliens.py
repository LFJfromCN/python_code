alien_0 = {'color':'green','points':5}
alien_1 = {'color':'red','points':10}
alien_2 = {'coolr':'yellow','points':3}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#创建一个用于储存外星人的空列表
alien = [ ]

#创建30个绿色的外星人
for alien_num in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:5]:
    print(alien)
print('.........')

print('Total number of aliens: ' + str(len(aliens)))
