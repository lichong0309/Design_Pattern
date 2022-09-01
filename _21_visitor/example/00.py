class Finance:
    """财务数据结构类"""
    def __init__(self):
        self.salesvolume = None  # 销售额
        self.cost = None    # 成本
        self.history_salesvolume = None  # 历史销售额
        self.history_cost = None    # 历史成本

    def set_salesvolume(self, value):
        self.salesvolume = value

    def set_cost(self, value):
        self.cost = value

    def set_history_salesvolume(self, value):
        self.history_salesvolume = value

    def set_history_cost(self, value):
        self.history_cost = value

    def accept(self, visitor):
        pass


class Finance_year(Finance):
    """2018年财务数据类"""

    def __init__(self, year):
        Finance.__init__(self)
        # 存放所有的工作人员
        # 不同类别的工作人员对相同的数据做不同的处理
        self.work = []  # 安排工作人员列表
        self.year = year

    def add_work(self, work):
        self.work.append(work)

    def accept(self):
        # 遍历所有的工作人员
        for obj in self.work:
            obj.visit(self)


class Accounting:
    """会计类"""

    def __init__(self):
        self.ID = "会计"
        self.Duty = "计算报表"

    def visit(self, table):
        print('会计年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        print('本年度纯利润： {}'.format(table.salesvolume - table.cost))
        print('------------------')


class Audit:
    """财务总监类"""

    def __init__(self):
        self.ID = "财务总监"
        self.Duty = "分析业绩"

    def visit(self, table):
        print('会计总监年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if table.salesvolume - table.cost > table.history_salesvolume - table.history_cost:
            msg = "较同期上涨"
        else:
            msg = "较同期下跌"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Adviser:
    """战略顾问"""
    def __init__(self):
        self.ID = "战略顾问"
        self.Duty = "制定明年战略"

    def visit(self, table):
        print('战略顾问年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if table.salesvolume > table.history_salesvolume:
            msg = "行业上行，扩大生产规模"
        else:
            msg = "行业下行，减小生产规模"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Work:
    """工作类"""

    def __init__(self):
        self.works = []  # 需要处理的年度数据列表

    def add_work(self, obj):
        self.works.append(obj)

    def remove_work(self, obj):
        self.works.remove(obj)

    def visit(self):
        for obj in self.works:
            obj.accept()


if __name__ == '__main__':
    work = Work()  # 计划安排财务、总监、顾问对2018年数据处理
    # 实例化2018年数据结构
    finance_2018 = Finance_year(2018)
    finance_2018.set_salesvolume(200)
    finance_2018.set_cost(100)
    finance_2018.set_history_salesvolume(180)
    finance_2018.set_history_cost(90)
    accounting = Accounting()   # 实例化会计
    audit = Audit()  # 实例化总监
    adviser = Adviser()     # 实例化顾问
    finance_2018.add_work(accounting)   # 会计安排到2018分析日程中
    finance_2018.add_work(audit)    # 总监安排到2018分析日程中
    finance_2018.add_work(adviser)  # 顾问安排到2018分析日程中
    work.add_work(finance_2018) # 添加2018年财务工作安排
    work.visit()