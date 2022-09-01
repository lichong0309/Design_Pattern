from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_element_a(self, element_a):
        pass

    @abstractmethod
    def visit_element_b(self, element_b):
        pass


class ConcreteVisitor1(Visitor):
    def visit_element_a(self, element_a):
        print('ConcreteVisitor1', 'element_a')

    def visit_element_b(self, element_b):
        print('ConcreteVisitor1', 'element_b')


class ConcreteVisitor2(Visitor):
    def visit_element_a(self, element_a):
        print('ConcreteVisitor2', 'element_a')

    def visit_element_b(self, element_b):
        print('ConcreteVisitor2', 'element_b')


class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)


class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)


class ObjectStructure:
    def __init__(self):
        self.elements = [ElementA(), ElementB()]


class Client:
    @staticmethod
    def main():
        object_structure = ObjectStructure()
        visitor = ConcreteVisitor1()
        for element in object_structure.elements:
            element.accept(visitor)
        visitor = ConcreteVisitor2()
        for element in object_structure.elements:
            element.accept(visitor)


if __name__ == '__main__':
    Client.main()