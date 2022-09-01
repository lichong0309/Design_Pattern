from abc import ABC, abstractmethod

class AbsAlgorithm(ABC):
    """
    抽象类定义了一个模板方法，其中通常会包含某个由抽象原语操作调用组成的算法框架。
    具体子类会实现这些操作，但是不会对模板方法做出修改。
    """

    def template_skeleton(self):
        """
        定义算法的框架
        :return: None
        """
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()

    #某些步骤可在基类中直接实现
    def base_operation1(self):
        print("算法公用方法1，初始化操作逻辑")

    def base_operation2(self):
        print("算法公用方法2，可被子算法类重写")

    #某些可定义为抽象类型，子算法必须实现
    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    #hook，子类既可以overwrite，实现各自的功能，也可以直接使用默认方法。这些hook可作为子算法额外的扩展点

    def hook1(self):
        pass

#具体类必须实现基类中的所有抽象操作，但是它们不能重写模板方法自身
class Algorithm1(AbsAlgorithm):

    def required_operations1(self):
        print(f'子算法{type(self).__name__}执行函数required_operations1')

    def required_operations2(self):
        print(f'子算法{type(self).__name__}执行函数required_operations2')


class Algorithm2(AbsAlgorithm):

    def required_operations1(self):
        print(f'子算法{type(self).__name__}执行函数required_operations1')

    def required_operations2(self):
        print(f'子算法{type(self).__name__}执行函数required_operations2')

    def hook1(self):
        print(f'子算法{type(self).__name__}扩展了功能hook1')

def client(abstract_class):
    abstract_class.template_skeleton()

if __name__ == "__main__":
    print("同样的客户端代码可以使用子算法1")
    client(Algorithm1())
    print()
    print("同样的客户端代码可以使用子算法2")
    client(Algorithm2())
