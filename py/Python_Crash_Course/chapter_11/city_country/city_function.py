def city_country(city, country, population=''):
    '''指明一个城市在哪个国家'''
    if population:
        c_c_p= city.title( ) + ', ' + country.title( ) + ' - ' + 'population ' + str(population)
    else:
        c_c_p =city.title( ) + ', ' + country.title( )
    return  c_c_p
 
