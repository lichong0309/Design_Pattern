from typing import Any

"""
一个电脑产品创建者，cpu是必须的
风扇和gpu是不一定需要的
"""

class Cpu():
    def __init__(self):
        self.type = ""
        self.price = 0

    def do_some_function(self):
        print('cpu用来计算')

    def __repr__(self):
        return 'cpu'


class InterCpu(Cpu):
    def __init__(self):
        super(Cpu, self).__init__()
        self.type = "英特尔i7"
        self.price = 3000


class AMDCpu(Cpu):
    def __init__(self):
        super(Cpu, self).__init__()
        self.type = "TR 2990WX"
        self.price = 13599


class Gpu():
    def __init__(self):
        self.type = ""
        self.price = 0

    def do_some_function(self):
        print('gpu用来渲染图形')

    def __repr__(self):
        return 'gpu'


class MsiGpu(Gpu):
    def __init__(self):
        super(Gpu, self).__init__()
        self.type = "微星2070"
        self.price = 3000


class Fan():
    def __init__(self):
        self.type = ""
        self.price = 0

    def do_some_function(self):
        print('风扇用来散热')

    def __repr__(self):
        return 'fan'


class ScytheFan(Fan):
    def __init__(self):
        super(Fan, self).__init__()
        self.type = "大镰刀"
        self.price = 600


class ComputerBuilder():
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Computer()

    @property
    def product(self):
        """
        调用产品的响应方法
        :return:
        """
        product = self._product
        return product

    def produce_cpu(self, cpu: Cpu) -> None:
        self._product.add(cpu)

    def produce_gpu(self, gpu: Gpu) -> None:
        self._product.add(gpu)

    def produce_fan(self, fan: Fan) -> None:
        self._product.add(fan)


class Computer():
    """
    定义好具体的产品，写上具体能实现的方法，比如该电脑类可以列出配置的具体型号
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts_type(self) -> None:
        parts_type = '\n'.join([repr(part) + ':' + part.type for part in self.parts])
        print('电脑配置如下:\n{}'.format(parts_type))

    def total_parts_price(self):
        total_price = sum([part.price for part in self.parts])
        print('电脑总价:{}'.format(total_price))
        return total_price


class Director:
    """
    负责以特定的顺序来执行建造步骤
    该类是可选的
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> ComputerBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ComputerBuilder) -> None:
        """
        使builder属性可赋值
        """
        self._builder = builder

    def build_minimal_computer(self) -> None:
        self.builder.produce_cpu(InterCpu())

    def build_full_computer(self) -> None:
        self.builder.produce_cpu(InterCpu())
        self.builder.produce_gpu(MsiGpu())
        self.builder.produce_fan(ScytheFan())


if __name__ == '__main__':
    director = Director()
    computer_builder = ComputerBuilder()
    director.builder = computer_builder
    print('配置功能齐全的电脑')
    director.build_full_computer()
    computer_builder.product.total_parts_price()
    computer_builder.product.list_parts_type()
    print('-' * 20)

    # 先将创建者重置
    computer_builder.reset()
    print('配置简陋的电脑')
    director.build_minimal_computer()
    computer_builder.product.total_parts_price()
    computer_builder.product.list_parts_type()

    print('-' * 20)

    # 自定义装机
    computer_builder.reset()
    print('自定义装机')
    computer_builder.produce_cpu(AMDCpu())
    computer_builder.produce_fan(ScytheFan())
    computer_builder.produce_gpu(MsiGpu())
    computer_builder.product.total_parts_price()
    computer_builder.product.list_parts_type()
