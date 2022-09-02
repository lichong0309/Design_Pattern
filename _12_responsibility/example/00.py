
class Event(object):
    def __init__(self, name):
        self.name = name
 
    def __str__(self):
        return self.name
 
class Widget(object):
    """
    handle()方法使用动态分发，通过hasattr()和getattr()决定一个特定请求（event）应该由谁来处理。
    如果被请求处理事件的控件并不支持该事件，则有两种回退机制。如果控件有parent，则执行parent的handle()方法。
    如果控件没有parent，但有handle_default()方法，则执行handle_default()
    """
    def __init__(self, parent=None):
        self.parent = parent
 
    def handle(self, event):
        handler = f'handel_{event}'
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)
 
class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))
    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))
 
class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))
 
class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))
 
 
def main():
    """
    main()函数展示如何创建一些控件和事件，以及控件如何对那些事件作出反应。所有事件都会被发送给所有控件。
    注意其中每个控件的父子关系。sd对象（SendDialog的一个实例）的父对象是mw（MainWindow的一个实例）。
    然而，并不是所有对象都需要一个MainWindow实例的父对象。例如，msg对象（MsgText的一个实例）是以sd作为父对象。
    """
    mw = MainWindow()
    sd = SendDialog(mw)    # parent是mw
    msg = MsgText(sd)
 
    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)
 
if __name__ == "__main__":
    main()
