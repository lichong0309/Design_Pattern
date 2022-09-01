# 具体的产品类
class Computer():

    def __init__(self,cpu,power,graphics_card,memory_module):
        self.cpu = cpu
        self.power = power
        self.graphics_card = graphics_card
        self.memory_module = memory_module

    def deep_clone_computer(selfs):
        from copy import deepcopy
        return deepcopy(selfs)

if __name__ == '__main__':
    # 创建第1个对象。克隆自己的形式
    test = Computer("四核CPU",'X电源','X显卡','X内存条')
    # 创建第2个对象。克隆自己的形式
    print(test.cpu)
    print(test.power)
    print(test.graphics_card)
    print(test.memory_module)
    test2 = test.deep_clone_computer()
    print('='*20)
    test2.cpu='1核CPU'
    test2.memory_module = 'YYY内存条'
    print(test2.cpu)
    print(test2.power)
    print(test2.graphics_card)
    print(test2.memory_module)
