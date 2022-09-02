# 接口实现类
class Implementor:
    def Operation(self):
        raise NotImplementedError
 
class ConcreteImplementorA(Implementor):
    def Operation(self):
        print("实现 A的方法")
 
class ConcreteImplementorB(Implementor):
    def Operation(self):
        print("实现 B的方法")
# 抽象类
class Abstraction():
    def __init__(self,implementor:Implementor):
        self.implementor = implementor
    def Operation(self):
        raise NotImplementedError
 
class RefineAbstraction(Abstraction):
    def Operation(self):
        self.implementor.Operation()
 
if __name__ == "__main__":
    a = ConcreteImplementorA()
    b = ConcreteImplementorB()
    aa = RefineAbstraction(a)
    ab = RefineAbstraction(b)
    aa.Operation()
    ab.Operation()