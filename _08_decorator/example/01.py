class Car(object):
    """
    一个汽车类
    """
    def __init__(self):
        self.logo = "奔驰" # 车标
        self.oil = 2 # 油耗
        self.ornamental = None # 装饰品

    # 安装空调
    def air_conditioner(self):
        print("空调真舒服！")

    def decorator(self, component):
        """用来额外添加装饰方法的"""
        self.ornamental = component

# 由于汽车的装饰品会发生变化
class Cushion(object):
    """
    坐垫
    """
    def __init__(self):
        self.name = "席梦思"

class Flower(object):
    """
    装饰花
    """
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    car = Car()
    cushion = Cushion()
    flower = Flower("玫瑰")
    # 汽车添加一个坐垫
    car.decorator(cushion)
    print(car.ornamental)
    # 添加一个花
    car.decorator(flower)
    print(car.ornamental)
