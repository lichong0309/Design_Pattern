from abc import ABC, abstractmethod


# 支付接口
class Payment(ABC):
    @abstractmethod
    def do_pay(self):
        pass


# 银行类：真实主题
class Bank(Payment):
    def check_account(self):
        print("账户检查中...")
        return True

    def do_pay(self):
        self.check_account()
        print("银行结算完成")


# 银行类的代理
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        print("借记卡即将去银行支付")
        self.bank.do_pay()
        print("借记卡完成银行支付")


# 客户端，没有权限做支付
class Client(object):
    def __init__(self):
        self.debit_card = DebitCard()

    def make_payment(self):
        print("借记卡支付开始")
        self.debit_card.do_pay()
        print("借记卡支付结束")


if __name__ == '__main__':
    client = Client()
    client.make_payment()
