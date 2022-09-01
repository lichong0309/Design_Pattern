
class Library(object):
    # 框架开发者
    def step1(self):
        print('step1')

    def step3(self):
        print('step3')

    def step5(self):
        print('step5')

    def run_app(self):

        self.step1()
        if self.step2():
            self.step3()

        for i in range(3):
            self.step4()

        self.step5()

    def step2(self):
        # 需要子类重写
        pass

    def step4(self):
        # 需要子类重写
        pass


class Application(Library):
    # 应用开发者
    def step2(self):
        print('step2')
        return True

    def step4(self):
        print('step4')


class Application2(Library):
    # 应用开发者
    def step2(self):
        print('Application2 step2')
        return False

    def step4(self):
        print('Application2 step4')


if __name__ == '__main__':
    app = Application()
    app.run_app()

    print('-'*10)
    app2 = Application2()
    app2.run_app()
