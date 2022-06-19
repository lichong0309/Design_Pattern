from abc import ABC, ABCMeta, abstractclassmethod

# 定义抽象工厂
class abstractFactory(object, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
       
    # 抽象类
    # 定义产品1
    @abstractclassmethod
    def makeProduct1(self):
        pass
    
    # 抽象类
    # 定义产品2
    @abstractclassmethod
    def makeProduct2(self):
        pass
    
    # 其他操作
    def test(self):
        print("抽象工厂类")    
        


# 抽象产品类1
class abstractProduct1(object, metaclass=ABCMeta):
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
        
# 抽象产品类2
class abstractProduct2(object, metaclass=ABCMeta):
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
        
    def makeProduct1(self):
        return f1Production_1()           # 返回产品实例
    
    def makeProduct2(self):
        return f1Production_2()           # 返回产品实例
    

# 抽象工厂的子类2
class factory_2(abstractFactory):
    def __init__(self) -> None:
        super().__init__()
    
    # 实现抽象类   
    def makeProduct1(self):
        return f2Production_1()            # 返回产品实例
    
    def makeProduct2(self):
        return f2Production_2()            # 返回产品实例
    

# facotry_1工厂的产品1
class f1Production_1(abstractProduct1):
    def __init__(self) -> None:
        super().__init__()
    
    # 实现抽象类
    def operatorProduct(self):
        print("factory_1工厂产品1")
        

# facotry_1工厂的产品2
class f1Production_2(abstractProduct2):
    def __init__(self) -> None:
        super().__init__()
    
    # 实现抽象类
    def operatorProduct(self):
        print("factory_1工厂产品2")
        
    
# factory_2工厂的产品1
class f2Production_1(abstractProduct1):
    def __init__(self) -> None:
        super().__init__()
        
    # 实现抽象类
    def operatorProduct(self):
        print("factory_2工厂产品1")


# factory_2工厂的产品2
class f2Production_2(abstractProduct2):
    def __init__(self) -> None:
        super().__init__()
        
    # 实现抽象类
    def operatorProduct(self):
        print("factory_2工厂产品2")


if __name__ == '__main__':
    f1_p1 = factory_1().makeProduct1()
    f1_p2 = factory_1().makeProduct2()
    f1_p1.operatorProduct()
    f1_p2.operatorProduct()
    
    
    
    f2_p1 = factory_2().makeProduct1()
    f2_p2 = factory_2().makeProduct2()
    f2_p1.operatorProduct()
    f2_p2.operatorProduct()