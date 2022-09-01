
#现金收费抽象类
class CashSuper(object):

    def accept_cash(self,money):
        pass
    
#正常收费子类
class CashNormal(CashSuper):

    def accept_cash(self,money):
        return money

#打折收费子类
class CashRebate(CashSuper):

    def __init__(self,discount=1):
        self.discount = discount

    def accept_cash(self,money):
        return money * self.discount

#返利收费子类
class CashReturn(CashSuper):

    def __init__(self,money_condition=0,money_return=0):
        self.money_condition = money_condition
        self.money_return = money_return

    def accept_cash(self,money):
        if money>=self.money_condition:
            return money - (money / self.money_condition) * self.money_return
        return money

#具体策略类
class Context(object):

    def __init__(self,csuper):
        self.csuper = csuper

    def GetResult(self,money):
        return self.csuper.accept_cash(money)




if __name__ == '__main__':
    money = input("原价: ")
    strategy = {}
    strategy[1] = Context(CashNormal())
    strategy[2] = Context(CashRebate(0.8))
    strategy[3] = Context(CashReturn(100,10))
    mode = input("选择折扣方式: 1) 原价 2) 8折 3) 满100减10: ")
    if mode in strategy:
        csuper = strategy[mode]
    else:
        print ("不存在的折扣方式")
        csuper = strategy[1]
    print ("需要支付: ",csuper.GetResult(money))