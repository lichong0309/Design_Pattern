class Originator(object):
    
    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def set_memento(self, memento):
        self.state = memento.state

    def show(self):
        print("当前状态 ", self.state)


# 备忘录
class Memento(object):

    def __init__(self, state):
        self.state = state


# 管理者
class Caretaker(object):

    def __init__(self, memento):
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