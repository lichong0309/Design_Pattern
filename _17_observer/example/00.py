# 当客户减少到阀值时，销售通知工厂减少生产、人力资源开始裁人，反之则增加

class Observer:
    """观察者核心：销售人员，被观察者number数据"""
    # observer 包含了观察者模式所有的对象，通过遍历对象来同时改变这些对象对应的值
    def __init__(self):
        self._number = None
        self._department = []           # 记录包含观察者模式下所有的对象

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
        print('当前客户数：{}'.format(self._number))
        for obj in self._department:
            obj.change(value)
        print('------------------')

    # 添加观察者模式下所有的对象
    def notice(self, department:object):
        """相关部门"""
        self._department.append(department)


class Hr:
    """人事部门"""
    def change(self, value):
        if value < 10:
            print("人事变动：裁员")

        elif value > 20:
            print("人事变动：扩员")

        else:
            print("人事不受影响")


class Factory:
    """工厂类"""
    def change(self, value):
        if value < 15:
            print("生产计划变动：减产")
        elif value > 25:
            print("生产计划变动：增产")
        else:
            print("生产计划保持不变")


if __name__ == '__main__':
    observer = Observer()
    hr = Hr()
    factory = Factory()
    observer.notice(hr)
    observer.notice(factory)
    observer.number = 10
    observer.number = 15
    observer.number = 20
    observer.number = 25
