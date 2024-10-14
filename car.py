from vehicle import Vehicle
import random
import math
class Car(Vehicle):
    '''Class to represent car vehicle
        - Inherits from vehicle class
    '''

    def __init__(self):
        '''init the attributes from Vehicle'''
        super().__init__("Lightning Car", 'C', 6, 8)


    def description_string(self):
        '''Returns a description string for a specific vehicle subclass'''
        return f"{self._name} - a fast car ({self._min_speed} - {self._max_speed} units). Special: Nitro Boost (1.5x speed)"
    

    def special_move(self, dist):
        '''Allows a vehicle subclass to use its special move with 1.5x speed'''
        if self._energy >= 15:
            spaces = random.randint(math.floor(self._min_speed * 1.5), math.floor(self._max_speed * 1.5))
            self._energy -= 15

            if spaces >= dist:
                self._position += dist - 1
                return  f"{self._name} uses nitro boost and crashes into an obstacle"
            
            self._position += spaces
            return f"{self._name} uses nitro boost and move {spaces} units!"
        
        else:
            return self._name + " did not have enough energy, so it did not move."
        
     