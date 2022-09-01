# 封装的接口
from sqlite3 import adapters
from telnetlib import DO


class Car(object):
    def __init__(self) -> None:
        self.name = "car"
    def make_noise(self):
        print("car make_noise call.")
        

# 需要使用适配器adapter的类
class Dog(object):
    def __init__(self) -> None:
        self.name = "dog"
    
    def bark(self):
        print("dog bark call.")
        

class Cat(object):
    def __init__(self) -> None:
        self.name = "cat"
    def meow(self):
        print("cat meow call.")

class Human(object):
    def __init__(self) -> None:
        self.name = "human"
    def speak(self):
        print("human speark call.")

# class cat(car):
#     def __init__(self) -> None:
#         super().__init__()


# adapter 类
class Adapter(object):
    def __init__(self, obj, adapter_method) -> None:
        self.obj = obj
        # 1. 将adapater_method转化为字典
        # 2. 将字典类型的数据批量构建为adapter的属性
        self.__dict__.update(adapter_method)
        
    # 对于不需要使用适配器的属性的调用，使用getattr从obj类中直接获取
    # 调用python内置魔法函数__getattr__:如果找不到对象的属性会调用这个方法
    def __getattr__(self, attr):
        return getattr(self.obj, attr)
        
        
        
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    human = Human()
    dog_adapter = Adapter(dog, dict(make_noise=dog.bark))
    cat_adapter = Adapter(cat, dict(make_noise=cat.meow))
    human_adapter = Adapter(human, dict(make_noise=human.speak))
    
    dog_adapter.make_noise()
    cat_adapter.make_noise()
    human_adapter.make_noise()
    
