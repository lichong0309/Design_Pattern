class ComponentBases:
    """部门抽象出来的基类"""
    def __init__(self, name):
        self.name = name

    def add(self, obj):
        pass

    def remove(self, obj):
        pass

    def display(self, number):
        pass


class Node(ComponentBases):

    def __init__(self, name, duty):
        self.name = name
        self.duty = duty
        self.children = []

    def add(self, obj):
        self.children.append(obj)

    def remove(self, obj):
        self.children.remove(obj)

    def display(self, number=1):
        print("部门：{} 级别：{} 职责：{}".format(self.name, number, self.duty))
        n = number+1
        for obj in self.children:
            obj.display(n)


if __name__ == '__main__':
    root = Node("总经理办公室", "总负责人")
    node1 = Node("财务部门", "公司财务管理")
    root.add(node1)
    node2 = Node("业务部门", "销售产品")
    root.add(node2)
    node3 = Node("生产部门", "生产产品")
    root.add(node3)
    node4 = Node("销售事业一部门", "A产品销售")
    node2.add(node4)
    node5 = Node("销售事业二部门", "B产品销售")
    node2.add(node5)
    root.display()
