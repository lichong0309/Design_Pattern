from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def send(self, message, colleague):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleague1 = None
        self.colleague2 = None

    def send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.notify(message)
        else:
            self.colleague1.notify(message)


class Colleague(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class ConcreteColleague1(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print('ConcreteColleague1', message)


class ConcreteColleague2(Colleague):
    def send(self, message):
        self.mediator.send(message, self)

    def notify(self, message):
        print('ConcreteColleague2', message)


class Client:
    @staticmethod
    def main():
        mediator = ConcreteMediator()
        colleague1 = ConcreteColleague1(mediator)
        colleague2 = ConcreteColleague2(mediator)
        mediator.colleague1 = colleague1
        mediator.colleague2 = colleague2
        colleague1.send('colleague1')
        colleague2.send('colleague2')


if __name__ == '__main__':
    Client.main()