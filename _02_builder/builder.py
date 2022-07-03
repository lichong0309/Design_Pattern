from abc import ABC, ABCMeta, abstractclassmethod



# 建造者 （抽象类）
class Builder(object, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass
    
    # 生成产品 abstract class method
    @abstractclassmethod
    def reset_product(self) -> None:
        pass
    
    # 产品第一部分 abstrac class method 
    @abstractclassmethod
    def product_part_1(self) ->None: 
        pass

    # 产品第二部分 abstrac class method
    @ abstractclassmethod
    def product_part_2(self) -> None:
        pass
    
    
      
# 产品类
class Production(object):
    def __init__(self) -> None:
        pass
    
    # 产品特性 1
    def feature_1(self) -> None:
        print("Production feature 1 call.")    
        
    # 产品特性 2
    def feature_2(self) -> None:
        print("Production feature 2 call.")
    


# 抽象类 实例化的子类 1
class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        super().__init__()
        self.reset_product()
        
    # 生成产品
    def reset_product(self) -> None:
        self.__proeduction = Production()
    
    # 产品第一部分
    def product_part_1(self) -> None:
        print("Production part 1.")
        self.__proeduction.feature_1()
        
    # 产品第二部分
    def product_part_2(self) -> None:
        print("Production part 2.")
        self.__proeduction.feature_2()
      
      
      
      
class Direction():
    """
    负责特定的顺序来建造production的类.
    可以省略，在客户端代码中直接调用direction中创建不同产品种类的函数 builder_minimal_feature_production builder_full_feature_production
    """
    def __init__(self) -> None:
        self.builder = None
    
    # 创建第一个产品 种类
    def build_minimal_feature_production(self):
        self.builder.product_part_1()
    
    # 创建第二个产品 种类
    def build_full_feature_production(self):
        self.builder.product_part_1()
        self.builder.product_part_2()
        


if __name__ == "__main__":
    direction = Direction()
    builder = ConcreteBuilder1()
    direction.builder = builder 
    
    # 创建第一个产品 种类
    print("Create the minimal feature production.")
    direction.build_minimal_feature_production()
    
    
    print('\n')
    
    # 创建第二个产品 种类
    print("Create the full feature production.")
    direction.build_full_feature_production()
    




        


