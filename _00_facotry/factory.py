from abc import ABC, abstractclassmethod, ABCMeta

# 创建抽象工厂类
class abstractFactory(object, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    # 抽象类
    # 定义产品
    @abstractclassmethod
    def makeProduct(self):
        pass
    
    # 其他操作
    def test(self):
        print("抽象工厂类")
        

# 抽象产品类
class abstractProduct(object, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    # 抽象类
    # 产品的属性和行为
    @abstractclassmethod
    def operatorProduct(self):
        pass
    
    # 其他操作
    def test(self):
        print("抽象产品类")

# 抽象工厂的子类1
class factory_1(abstractFactory):
    def __init__(self) -> None:
        super().__init__()
        
    def makeProduct(self):
        return f1Production()           # 返回产品实例
    

# 抽象工厂的子类2
class factory_2(abstractFactory):
    def __init__(self) -> None:
        super().__init__()
    
    # 实现抽象类   
    def makeProduct(self):
        return f2Production()           # 返回产品实例
    

# facotry_1工厂的产品
class f1Production(abstractProduct):
    def __init__(self) -> None:
        super().__init__()
    
    # 实现抽象类
    def operatorProduct(self):
        print("factory_1工厂产品")
        
    
# factory_2工厂的产品
class f2Production(abstractProduct):
    def __init__(self) -> None:
        super().__init__()
        
    # 实现抽象类
    def operatorProduct(self):
        print("factory_2工厂产品")
    
 
 
 
if __name__ == "__main__":
    # p1：factory_1工厂的产品
    p1 = factory_1().makeProduct()   
    # p2: factory_2工厂的产品
    p2 = factory_2().makeProduct()
    
    p1.operatorProduct()
    p2.operatorProduct()    



