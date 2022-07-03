import copy
from typing import List, Optional


# 类
class Entity(object):
    def __init__(self, item:int) -> None:
        self.item = item 
    
    
# 创建原型模式的类
class Prototype(object):
    def __init__(
                    self, 
                    component_int:int, 
                    component_list:List[int], 
                    component_class:Optional[Entity]
                 ) -> None:
        
        self.component_int = component_int
        self.component_list = component_list
        self.component_class = component_class
        
    # copy     
    # 重写python提供的 __copy__ 魔法函数
    def __copy__(self):
        component_int = copy.copy(self.component_int)
        component_list = copy.copy(self.component_list)
        component_class = copy.copy(self.component_class)
        
        new = self.__class__(
            component_int,
            component_list,
            component_class
        )
        
        return new
    
    # deepcopy
    # 重写python提供的 __deepcopy__ 魔法函数
    def __deepcopy__(self, memo):
        if memo == None:
            memo = {}
            
        component_int = copy.deepcopy(self.component_int, memo)
        component_list = copy.deepcopy(self.component_list, memo)
        component_class = copy.deepcopy(self.component_class, memo)
        new = self.__class__(
            component_int,
            component_list,
            component_class
        )
        
        return new
    
    

if __name__ == "__main__":
    # 创建Entity实例 
    entity = Entity(5)
    
    # 创建变量
    component_int = 1
    component_list = [[1,2,3], 4, 5]
    component_class = entity
    # 创建 Prototype实例
    prototype = Prototype(
        component_int=component_int,
        component_list=component_list,
        component_class=component_class
    )

    # copy
    copy_prototype = copy.copy(prototype)
    
    # deepcopy
    deepcopy_prototype = copy.deepcopy(prototype) 
    
    # test
    # 修改component_list[0]的值, 看是否改变
    print("prototype component_list:", prototype.component_list)
    copy_prototype.component_list[0][1] = 1
    print("copy_prototype component_list:", copy_prototype.component_list)
    
    print("prototype component_list:", prototype.component_list)
    deepcopy_prototype.component_list[0][1] = 3
    print("deepcopy_prototype component_list:", deepcopy_prototype.component_list)
          
        

