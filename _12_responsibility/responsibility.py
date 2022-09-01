# 可以使用了链表创建责任链


class Handler:
    """
    抽象接口
    """

    def __init__(self):
        pass

    def successor(self, successor):
        self.successor = successor

    def handle(self, request):
        pass


class ConcreteHandler1(Handler):
    """
    接口实现方法handler1
    """

    def handle(self, request):
        if 0 < request <= 10:
            print("in handler1")
        else:
            self.successor.handle(request)


class ConcreteHandler2(Handler):
    """
    接口实现方法handler2
    """
    def handle(self, request):
        if 10 < request <= 20:
            print("in handler2")
        else:
            self.successor.handle(request)


class ConcreteHandler3(Handler):
    """
    接口实现方法handler3
    """
    def handle(self, request):
        if 20 < request <= 30:
            print("in handler3")
        else:
            self.successor.handle(request)


class FinalHandler(Handler):
    """
    最终处理handler
    """
    def handle(self, request):
        print('end of chain, no handler for {}'.format(request))


class Client(object):
    def __init__(self):
        h1 = ConcreteHandler1()
        h2 = ConcreteHandler2()
        h3 = ConcreteHandler3()
        final = FinalHandler()
        # 这里再实例化完成之后进行任务的传递过程设置
        h1.successor(h2)
        h2.successor(h3)
        h3.successor(final)

        requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
        for request in requests:
            h1.handle(request)


if __name__ == "__main__":
    client = Client()

