from vehicle import Vehicle
from random import randint

class Truck(Vehicle):
    '''Class to represent truck vehicle
        - Inherits from vehicle class
    '''

    def __init__(self):
        '''Calls super init to initialize truck class'''
        super().__init__("Behemoth Truck", 'T', 4, 8)

    
    def description_string(self):
        '''Returns a description string for truck'''
        return "Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles)."
    

    def special_move(self, dist):
        '''Allows truck to move at 2x speed and smash through obstacles'''
        if self._energy >= 15:
            spaces = randint(self._min_speed * 2, self._max_speed * 2)
            self._energy -= 15
            self._position += spaces

            if spaces >= dist:
                return self._name + f" rams forward bashing through the Obstacle to go {spaces} units!"
            
            return self._name + f" rams forward {spaces} units" 
        
        else:
            return self._name + f" did not have enough energy, so it did not move."