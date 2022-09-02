import threading
import time

class Custom():

    def __init__(self, name):
        import time
        time.sleep(1)
        self.name = name

    # 通过类方法创建实例
    @classmethod
    def creat_class(cls, *args, **kwargs):
        # 如果没有对象
        if not hasattr(Custom, "_instance"):
            Custom._instance = Custom(*args, **kwargs)
        return Custom._instance


def task(arg):
    obj = Custom.creat_class('test')
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
