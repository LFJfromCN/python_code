#创建一个空列表用来储存外星人
aliens = [ ]
#创建30个绿色的外星人
for alien_num in range(30):
    new_alien = {'color':'green','points':'5','speed':'slow'}
    new = {'color':'yellow','points':10,'speed':'medium'}
    aliens.append(new_alien)
    aliens.append(new)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
#显示前10个外星人
for alien in aliens[0:10]:
    print(alien)
print('...')
