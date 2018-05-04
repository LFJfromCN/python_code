from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''根据指定的的国家，返回pygal使用的两个字母的国别码'''
    for code, name in COUNTRIES.items( ):
        if name == country_name:
            return code
        if country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Dominica':
            return 'do'
        elif country_name == 'Congo':
            return 'cg'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
    #如果没有找到指定的国别码，就返回None
    return None
