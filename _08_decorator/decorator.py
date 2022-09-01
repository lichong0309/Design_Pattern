from abc import ABCMeta, abstractmethod


class Person():
    def __init__(self, name):
        self.name = name

    def decorator(self, component):
        self.component = component

    def show(self):
        print ('%s开始穿衣' % self.name)
        self.component.show()


class Finery():
    def __init__(self, metaclass=ABCMeta):
        self.component = None

    def decorator(self, component):
        self.component = component


    @abstractmethod
    def show(self):
        if self.component:
            self.component.show()


class TShirt(Finery):
    def show(self):
        Finery.show(self)
        print ('穿TShirst')


class Trouser(Finery):
    def show(self):
        Finery.show(self)
        print ('穿裤子')


class Shoe(Finery):
    def show(self):
        Finery.show(self)
        print ('穿鞋子')


class Tie(Finery):
    def show(self):
        Finery.show(self)
        print ('穿领带')


if __name__ == '__main__':
    person = Person('kevin')
    tshirt = TShirt()
    trouser = Trouser()
    shoe = Shoe()
    tie = Tie()

    trouser.decorator(tshirt)
    shoe.decorator(trouser)
    tie.decorator(shoe)
    person.decorator(tie)
    person.show()
