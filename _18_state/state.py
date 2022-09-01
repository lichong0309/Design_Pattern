from abc import ABC, abstractmethod

class Context(ABC):
    """
    Contex类，是client端调用的入口。该类需要接收State对象，指示当前State状态的上下文，并且维护各种State对象的引用
    """
    _state = None

    def __init__(self, state):
        """接收state对象，并且指向该对象"""
        self.transition_to(state)

    def transition_to(self, state):
        """程序运行中切换state对象, 将输入对象的上下文切换为当前state对象"""
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    ##当前对象的行为
    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()

class State(ABC):
    """State抽象类，声明各个子类需要实现的方法。并且提供到Context对象的回溯引用，该引用可用来根据context上下文切换到指定的state"""
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class StateA(State):
    def handle1(self) -> None:
        print(f"{type(self).__name__} handle request1")
        print(f"{type(self).__name__} wants to change the state of the context.")
        self.context.transition_to(StateB())

    def handle2(self) -> None:
        print(f"{type(self).__name__} handle request2")

class StateB(State):
    def handle1(self) -> None:
        print(f"{type(self).__name__} handle request1")
        
    def handle2(self) -> None:
        print(f"{type(self).__name__} handle request2")
        print(f"{type(self).__name__} wants to change the state of the context.")
        self.context.transition_to(StateA())


if __name__ == "__main__":
    context = Context(StateA())
    context.request1()
    context.request2()

