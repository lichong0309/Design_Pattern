# 使用队列实现多个操作流程的执行

from abc import ABCMeta, abstractmethod


class Receiver:
    """Receiver：定义各种方法以便执行不同的操作"""
    def action1(self):
        print('Execute action1...')

    def action2(self):
        print('Execute action2...')


class Command(metaclass=ABCMeta):
    """命令对象接口：定义统一的命令执行方法"""
    @abstractmethod
    def execute(self):
        pass


class Action1(Command):
    """命令1：用于执行操作action1"""
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action1()


class Action2(Command):
    """命令2：用于执行操作action2"""
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action2()


class Invoker:
    """创建命令队列，调用并执行队列中的命令"""
    def __init__(self):
        self.actions = []

    def append_action(self, action):
        self.actions.append(action)

    def execute_actions(self):
        for action in self.actions:
            action.execute()


if __name__ == '__main__':
    receiver = Receiver()
    action1 = Action1(receiver)
    action2 = Action2(receiver)

    invoker = Invoker()
    invoker.append_action(action1)
    invoker.append_action(action2)
    invoker.execute_actions()