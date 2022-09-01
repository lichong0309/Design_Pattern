from abc import ABC, abstractmethod

class LiftState(ABC):
    """
    State抽象类，声明子类必须实现的方法
    """
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass



#实现具体的状态流转控制
class OpenState(LiftState):

    def open(self):
        print(f"{type(self).__name__}: The door is opened...")
        return self

    def close(self):
        print(f"{type(self).__name__}: The door start to close")
        print(f"{type(self).__name__}: The door closed, will run")
        return RunState()

    def run(self):
        print(f"{type(self).__name__}: Run Forbidden ")
        return self

    def stop(self):
        print(f"{type(self).__name__}: Stop Forbidden ")
        return self

class CloseState(LiftState):

    def open(self):
        print(f"{type(self).__name__}: The door start to open")
        print(f"{type(self).__name__}: The door opened")
        return OpenState()

    def close(self):
        print(f"{type(self).__name__}: The door is already closed")
        return self

    def run(self):
        print(f"{type(self).__name__}: The door start to run")
        print(f"{type(self).__name__}: The door is running")
        return RunState()

    def stop(self):
        print(f"{type(self).__name__}: Stop Forbidden ")
        return self


class RunState(LiftState):

    def open(self):
        print(f"{type(self).__name__}: Open Forbidden")
        return self

    def close(self):
        print(f"{type(self).__name__}: Close Forbidden ")
        return RunState()

    def run(self):
        print(f"{type(self).__name__}: lift is running ")
        return self

    def stop(self):
        print(f"{type(self).__name__}: Start to stop ")
        print(f"{type(self).__name__}: lift Stoped ")
        return StopState()


class StopState(LiftState):

    def open(self):
        print(f"{type(self).__name__}: Start to open ")
        print(f"{type(self).__name__}: lift is opened ")
        return OpenState()

    def close(self):
        print(f"{type(self).__name__}: Close Forbidden ")
        return self

    def run(self):
        print(f"{type(self).__name__}: Run Forbidden ")
        return self

    def stop(self):
        print(f"{type(self).__name__}: Run Forbidden ")
        return self

##记录状态流转上下文，控制流转调度
class Context(object):
    _lift_state = None

    def __init__(self, state):
        self.transition_to(state)

    def get_state(self):
        return self._lift_state

    def transition_to(self, state):
        """程序运行中切换state对象, 将输入对象的上下文切换为当前state对象"""
        print(f"Context: Transition to {type(state).__name__}")
        self._lift_state = state
        self._lift_state.context = self

    def open(self):
        self.transition_to(self._lift_state.open())

    def close(self):
        self.transition_to(self._lift_state.close())

    def run(self):
        self.transition_to(self._lift_state.run())

    def stop(self):
        self.transition_to(self._lift_state.stop())

if __name__ == "__main__":
    ctx = Context(StopState())
    ctx.open()
    ctx.close()
    ctx.run()
    ctx.stop()
    ctx.run()

