import abc
 
class Component(metaclass=abc.ABCMeta): #定义一个对象的接口，可以给这些对象动态地添加职责。
    @abc.abstractmethod
    def Operation(self):
        pass
 
class ConcreteComponent(Component): # 定义一个具体对象，可以给这个对象添加一些职责。
    def Operation(self):
        print("具体对象的操作")
 
class Decorator(Component): 
    # 抽象装饰类，继承了Component，从外类来扩展Component类的功能，但对于Component来说，无需知道Decorator的存在。
    def __init__(self):
        self._component = None
        
    def SetComponent(self,component):   # 设置Component
        self._component = component
        
    def Operation(self):                # 重写Operation()实际执行的市Component的Operation()
        if(self._component != None):
            self._component.Operation()            
 
class ConcreteDecoratorA(Decorator): # 具体的装饰对象，起到给Component添加职责的功能。
    def __init__(self):
        self.__addedState = None    # 本类独有的功能，区别于ConcreteDecoratorB
        
    def Operation(self):
        super(ConcreteDecoratorA,self).Operation()  # 先运行原Component的Operation（），再执行本类功能。
        self.__addedState = "New State"
        print("具体装饰对象A的操作")
 
class ConcreteDecoratorB(Decorator):    # 具体的装饰对象，起到给Component添加职责的功能。
    def Operation(self):
        super(ConcreteDecoratorB,self).Operation()
        self.AddedBehavior()
        print("具体装饰对象A的操作")
        
    def AddedBehavior(self):    # 本类独有的功能，区别于ConcreteDecoratorA
        pass
 
if __name__ == '__main__':
    c = ConcreteComponent()
    d1 = ConcreteDecoratorA()
    d2 = ConcreteDecoratorB()
    d1.SetComponent(c)
    d2.SetComponent(d1)
    d2.Operation()

