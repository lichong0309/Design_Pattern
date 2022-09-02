class FlyweightBase:
    """享元基类"""
    def offer(self):
        pass


class Flyweight(FlyweightBase):
    """共享享元类"""
    def __init__(self, name):
        self.name = name

    def get_price(self, price):
        print('产品类型：{} 详情：{}'.format(self.name, price))


class FactoryFlyweight:
    """享元工厂类"""
    def __init__(self):
        self.product = {}

    def Getproduct(self, key):
        if not self.product.get(key, None):
            self.product[key] = Flyweight(key)
        return self.product[key]


if __name__ == '__main__':
    test = FactoryFlyweight()
    A = test.Getproduct("高端")
    A.get_price("香水：80")
    B = test.Getproduct("高端")
    B.get_price("面膜：800")
