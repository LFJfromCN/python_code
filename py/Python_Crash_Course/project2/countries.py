from pygal.maps.world import COUNTRIES      #pygal-2.0.0中移除了i18n

for country_code in sorted(COUNTRIES.keys( )):
    print(country_code, COUNTRIES[country_code])
