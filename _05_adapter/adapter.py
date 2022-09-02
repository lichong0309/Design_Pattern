from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass


class Adaptee:
    def operation1(self):
        str(self)
        print('adaptee.operation1')


class Adapter(Adaptee, Target):
    def __init__(self):
        self.adaptee = Adaptee()

    def operation2(self):
        print('adaptee.operation2')


if __name__ == '__main__':
    adapter = Adapter()
    adapter.operation1()
    adapter.operation2()