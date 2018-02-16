class Employee( ):
    '''一个描述雇员的类'''

    def __init__(self, firstname, lastname, salary):
        self.first = firstname.title( )
        self.last = lastname.title( )
        self.salary = salary

    def give_raise(self, raiseup=5000):
        if raiseup == 5000:
            return raiseup
        else:
            raiseup = input('请输入薪水涨幅：')
            return raiseup

    
