# 装饰者模式类似与python和c++中封装，更规范

class Equipment(object):
 
    def __init__(self):
        self.name = ''
        self.state = 'open'
 
    def turn_off(self):
        if self.state == 'open':
            print('%s has been shut down' % self.name)
        else:
            self.state = 'closed'
            print('%s is closed' % self.name)
 
 
class Lamp(Equipment):
 
    def __init__(self):
        super().__init__()
        self.name = 'lamp'
 
 
class AirConditioner(Equipment):
 
    def __init__(self):
        super().__init__()
        self.name = 'air_conditioner'
 
 
class OldClient(object):
 
    def __init__(self, lamp:Lamp, air_conditioner:AirConditioner):
        self.lamp = lamp
        self.air_conditioner = air_conditioner
 
    def leave_home(self):
        self.lamp.turn_off()
        self.air_conditioner.turn_off()
 
 
class FacadeEquipment(object):
    def __init__(self, lamp:Lamp, air_conditioner:AirConditioner):
        self.lamp = lamp
        self.air_conditioner = air_conditioner
 
    def close(self):
        self.lamp.turn_off()
        self.air_conditioner.turn_off()
 
 
class FacadeClient(object):
    def __init__(self, equipments:FacadeEquipment):
        self.equipments = equipments
 
    def leave_home(self):
        self.equipments.close()
 
 
if __name__ == '__main__':
    print('old pattern')
    lamp = Lamp()
    air_conditioner = AirConditioner()
    old_client = OldClient(lamp, air_conditioner)
    old_client.leave_home()
    print('facade pattern')
    facade_equipment = FacadeEquipment(lamp, air_conditioner)
    facade_client = FacadeClient(facade_equipment)
    facade_client.leave_home()
