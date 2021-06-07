##                                      POLYMORPHISM
class Coffe():
    def milk(self):
        print('i prepared coffee for you')

class Tea():
    def milk(self):
        print('i prepared tea for you')

def Coffee_Vending_Machine(func):
    func.milk()
    
# Coffee_Vending_Machine(Coffe())
# Coffee_Vending_Machine(Tea())

#                                   POLYMORPHISM WITH INHERITANCE 'METHOD OVER-RIDING'
class Coffee_Vending_Machine():
    def __init__(self,fun):
        self.fun = fun
        print('i am ordered : ',self.fun)

    def milk(self):
        print('we can use milk for miltiple purpose')
class Coffe(Coffee_Vending_Machine):
    def __init__(self,item):
        self.item = item

    def milk(self):
        super().__init__(self.item)
        print('i prepared coffee for you')

class Tea(Coffee_Vending_Machine):
    def __init__(self,item):
        self.item = item

    def milk(self):
        super().__init__(self.item)
        print('i prepared tea for you')

def press(func):
    func.milk()
    
press(Coffee_Vending_Machine('milk'))
# objc = Coffe('coffee')   
# press(objc)
# press(Tea('tea'))

#                                   ENCAPSULATION
class Computer():
    def __init__(self):
        self.__maxprice = 900
        self.minprice = 500
    
    def sell(self):
        print(' selling max price : ',self.__maxprice)
        print(' selling min price : ',self.minprice)
    
    def setMaxprice(self,price):
        self.__maxprice = price
    
    def maxprice(self,price):
        self.minprice = price

    def __A(self):
        print('a')


# c = Computer()
# c._Computer__A()
# c.sell()
# c.minprice = 600
# c.__maxprice = 1000
# c.sell()
# c.setMaxprice(1000)
# c.sell()

#                                             INHERITANCE
# SIMPLE
# import datetime
class BankAccount():
    def __init__(self,name,acno,amount):
        self.name = name
        self.acno = acno
        self.amount = amount
    
    def balance(self):
        print('your balance is ',self.amount)

class Withdraw(BankAccount):
    def __init__(self,name,accno,amount,wamount):
        self.wamount = wamount
        super().__init__(name,accno,amount)
    
    def with_drawl(self):
        newamount = self.amount - self.wamount
        return newamount
        # print('your new balance is : ',newamount) 

        
    def balance(self):
        amt = self.with_drawl()
        print('your new balance is : ',amt) 

obj = BankAccount('jessy',123,10000)
obj.balance()
obj = Withdraw('jessy',123,10000,500)
# obj.with_drawl()
obj.balance()
