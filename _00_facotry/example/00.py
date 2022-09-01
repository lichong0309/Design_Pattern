class Factory(object):
    """定义工厂类"""
 
    def create_fruit(self, fruit):
        """定义创建水果方法"""
        if fruit == "apple":
            return Apple()
        elif fruit == "peach":
            return Peach()
 
 
class Fruit(object):
    """创建水果类"""
 
    def __str__(self):
        return "fruit"
 
class Apple(Fruit):
    """创建苹果类"""
    def __str__(self):
        return "apple"
 
 
class Peach(Fruit):
    """创建桃子类"""
 
    def __str__(self):
        return "peach"
 
 
if __name__ == "__main__":
    # 工厂实例化
    factory = Factory()
    # 使用工厂创建水果
    fruit = factory.create_fruit("apple")
    print(fruit)