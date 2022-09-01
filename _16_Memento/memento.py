# 备忘录类
class Memento(object):

    def __init__(self, state):
        self.state = state
        

class Originator(object):

    def __init__(self, state):
        self.state = state

    # 记录状态
    def create_memento(self):
        return Memento(self.state)

    # 可复原状态
    def set_memento(self, memento:Memento):
        self.state = memento.state

    def show(self):
        print ("当前状态 ", self.state)


# 管理者类
class Caretaker(object):

    def __init__(self,memento:Memento):
        self.memento = memento


if __name__ == "__main__":
    # 初始状态
    originator = Originator(state='On')
    originator.show()
    # 备忘录
    caretaker = Caretaker(originator.create_memento())
    # 修改状态
    originator.state = 'Off'
    originator.show()
    # 复原状态
    originator.set_memento(caretaker.memento)
    originator.show()