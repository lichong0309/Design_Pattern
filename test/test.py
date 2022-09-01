class Person(object):
    _defaults = {
        "name"  : "alex",
        "age"   : 18,
        "city"  : "Sydney"
    }
 
    def __init__(self):
        self.__dict__.update(self._defaults)
        self.a = 10
 
    def printName(self):
        print(self.name)
 
    def printAge(self):
        print(self.age)

    def printa(self):
        print(self.a)
        
        
x = Person()
x.printa()
x.printAge()
x.printName()
