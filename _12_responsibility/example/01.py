import abc


# 抽象处理者
class Handler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, day):
        pass


# 具体处理者，作为链条节点之一。
class GeneralManager(Handler):
    def handle(self, day):
        if day <= 10:
            print(f"总经理准假{day}天")
        else:
            print("休假太长，不予准假！")


# 具体处理者，作为链条节点之一。
class DivisionManager(Handler):
    def __init__(self):
        self.next = GeneralManager()  # 链接到下一级

    def handle(self, day):
        if day <= 5:
            print(f"部门经理准假{day}天")
        else:
            print("部门经理准假职级不足")
            self.next.handle(day)


# 具体处理者，作为链条节点之一。
class ProjectManager(Handler):
    def __init__(self):
        self.next = DivisionManager()  # 链接到下一级

    def handle(self, day):
        if day <= 3:
            print(f"项目经理准假{day}天")
        else:
            print("项目经理准假职级不足")
            self.next.handle(day)


if __name__ == "__main__":
    handler = ProjectManager()
    handler.handle(4)