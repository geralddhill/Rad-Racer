from vehicle import Vehicle
from random import randint
from math import floor

class Motorcycle(Vehicle):
    '''Class to represent motorcycle vehicle
        - Inherits from vehicle class
    '''

    def __init__(self):
        '''Calls super init to initialize motorcycle class'''
        super().__init__("Swift Bike", 'M', 6, 8)

    def slow(self, dist):
        '''Overrides slow method to let motorcycle move at 75% speed instead of 50%'''
        spaces = randint(floor(self._min_speed * 0.75), floor(self._max_speed * 0.75))
        self._position += spaces

        if spaces >= dist:
            return self._name + f" slowly and safely moves around the obstable {spaces} units!"
        
        return self._name + f" slowly moves {spaces} units!"

    def description_string(self):
        '''Returns a description string for motorcycle'''
        return f"Swift Bike - a speedy motorcycle ({self._min_speed}-{self._max_speed} units). Special: Wheelie (2x speed but there's a chance you'll crash)."
    
    def special_move(self, dist):
        '''Allows mortorcycle to have a 75% chance of moving at 2x speed'''
        if self._energy >= 15:
            self._energy -= 15

            # Rolls to see if special move succeeds
            roll = randint(0, 4)
            if roll == 0:
                self._position += 1
                return self._name + "pops a wheelie and falls over!"
            
            spaces = randint(self._min_speed * 2, self._max_speed * 2)

            if spaces >= dist:
                self._position += dist - 1
                return self._name + f" pops a wheelie and crashes into an obstacle!"
            
            self._position += spaces
            return self._name + f" pops a wheelie and moves {spaces} units!!"
        
        else:
            return self._name + f" did not have enough energy, so it did not move."