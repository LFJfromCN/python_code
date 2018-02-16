import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    '''一个用于测试Employee类的方法'''
    def setUp(self):
        '''创建一个姓名为Fujing Li, salary的公用实例'''
        self.employee = Employee('fujing', 'li', 40000)

    def test_give_default_raise(self):
        '''测试默认的薪水增加'''
        raiseup = self.employee.give_raise( )
        self.assertEqual(raiseup, 5000)

    def test_give_custom_raise(self):
        '''测试自定义的薪水增加'''
        print('用于该测试时请输入10000')
        raiseup = int(self.employee.give_raise(10000))
        self.assertEqual(raiseup, 10000)
        
unittest.main( )
