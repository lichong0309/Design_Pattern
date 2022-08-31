
from typing import Any
# 使用类装饰器的方法创建单例模式
class singleton(object):
    def __init__(self, cls) -> None:
        self.cls = cls
        self._instance = {}         # 初始化为空，记录单例模式中的类是否已经被实例化
    
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # 如果单例模式中的类没有被实例化，则在self._instance中添加
        if self.cls not in self._instance:
            self._instance[self.cls] = self.cls()
        return self._instance[self.cls]
            


@singleton
class singleton_test(object):
    def __init(self):
        self.test = "test"
    
if __name__ == "__main__":
    test_a = singleton_test()
    test_b = singleton_test()

    # 判断对于singleton_test类所创建的两个实例，是否是同一个
    # 如果返回为True，则为同一个
    # 如果返回为False，则不为同一个
    res = (id(test_a) == id(test_b))

    print(res)
