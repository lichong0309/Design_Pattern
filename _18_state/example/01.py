class Base:
    def executor(self, value):
        self.run(value)


class Low(Base):
    def __init__(self):
        self.name = "较低占用率状态"

    def run(self, value):
        print("当前：{} 值:{}".format(self.name, value))
        print("无应急情况执行")

class Large(Base):
    def __init__(self):
        self.name = "较高占用率状态"

    def run(self, value):
        print("当前：{} 值：{}".format(self.name, value))
        print("发送警报邮件")


class Statu:
    def __init__(self):
        self.value = 0.1
        self.low = Low()
        self.large = Large()
        self.ststu = None

    def monitor(self):
        if self.value <0.5:
            self.ststu = self.low
        else:
            self.ststu = self.large
        self.ststu.executor(self.value)


if __name__ == '__main__':
    test = Statu()
    test.monitor()
    test.value = 0.9
    test.monitor()
