class SubSystemA:
    def methodA(self):
        pass
    
class SubSystemB:
    def methodB(self):
        pass
    
class SubSystemC:
    def methodC(self):
        pass
 
class Facade:
    objA=None
    objB=None
    objC=None
 
    def __init__(self):
        self.objA=SubSystemA()
        self.objB=SubSystemB()
        self.objC=SubSystemC()
 
 
    def method(self):
        self.objA.methodA()
        self.objB.methodB()
        self.objC.methodC()
 
def clientUI():
    facade=Facade()
    facade.method()
 
if __name__=='__main__':
    clientUI()