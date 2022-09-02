from abc import ABC, abstractclassmethod, ABCMeta
# 创建抽象类
class Shape(object, metaclass=ABCMeta):
    def __init__(self, name, *param) -> None:
        self.name = name 
        self.param = param
        
    def get_name(self):
        return self.name

    def get_param(self):
        return self.param
    

class Pen(object, metaclass=ABCMeta):
    def __init__(self, shape:Shape) -> None:
        self.shape = shape
    
    def get_shape(self):
        return (self.shape.get_name, self.shape.get_param)
    
    # 抽象方法
    @abstractclassmethod
    def draw(self):
        pass

# 抽象类的子类
# Shape
class Rectange(Shape):
    def __init__(self, name, *param) -> None:
        super().__init__(name, *param)
        print("创建一个rectange的实例，name为：{0}，参数为：{1}".format(self.name, self.param))
        
class Circle(Shape):
    def __init__(self, name, *param) -> None:
        super().__init__(name, *param)
        print("创建一个circle的实例，name为：{0}，参数为：{1}".format(self.name, self.param))
        
        
# Pen
class NormalPen(Pen):
    def __init__(self, shape: Shape) -> None:
        super().__init__(shape)
        self.type = "noraml"
        
    # 实现抽象类中的函数
    def draw(self):
        print("创建一个normal pen 创建一个{0}，参数为{1}".format(self.shape.get_name(), self.shape.get_param()))
        
class BrushPen(Pen):
    def __init__(self, shape: Shape) -> None:
        super().__init__(shape)
        self.type = "brush"
        
    # 实现抽象类中的函数
    def draw(self):
        print("创建一个brush pen 创建一个{0}，参数为{1}".format(self.shape.get_name(), self.shape.get_param()))
        

if __name__ == "__main__":
    normal_pen = NormalPen(Rectange("rectange",10, 20))
    brush_pen = BrushPen(Circle("circle", 15))
    
    normal_pen.draw()
    brush_pen.draw()
    
    

