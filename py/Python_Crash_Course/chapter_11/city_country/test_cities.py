import unittest
from city_function import city_country

class CitiesTestCase(unittest.TestCase):
    '''测试city_function.py'''
    def test_city_county(self):
        '''能够正确处理像Santiago, Chile这样的字符串吗？'''
        c0_c1 = city_country('santiago', 'chile')
        self.assertEqual(c0_c1, 'Santiago, Chile')

    def test_city_country_population(self):
        '''能够正确处理像Santiago, Chile - population 5000000这样的字符串吗？'''
        c_c_p = city_country('santiago', 'chile', 5000000)
        self.assertEqual(c_c_p, 'Santiago, Chile - population 5000000')

unittest.main( )
