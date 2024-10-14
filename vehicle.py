import abc
import random
import math

class Vehicle(abc.ABC):
    '''
        Vehicle class represents an abstract vehicle
        
        Attributes:
            _name: str
            _initial: int
            _min_speed: int
            _max_speed: int
    '''
    def __init__(self, name, initial, min_speed, max_speed):
        '''intialize the name, initial, min_speed, max_speed, position = 0, energy = 100'''
        self._name = name
        self._initial = initial
        self._min_speed = min_speed
        self._max_speed = max_speed
        self._position = 0
        self._energy = 100


    @property
    def initial(self):
        '''Accesses the initial property'''
        return self._initial
    
    @property
    def position(self):
        '''Accesses the position property'''
        return self._position
    
    @property
    def energy(self):
        '''Accesses the energy property'''
        return self._energy


    def fast(self, dist):
        '''Makes vehicle move fast in game'''
        # Checks if energy is high enough
        if self._energy >= 5:
            spaces = random.randint(self._min_speed, self._max_speed)
            self._energy -= 5

            if spaces >= dist:
                self._position += dist - 1
                return self._name + f" CRASHES into an obstacle"
            
            self._position += spaces
            return self._name + f" quickly moves {spaces} units!" 
        
        else:
            # Returns if not enough energy
            return self._name + " did not have enough energy, so it did not move."
    

    def slow(self, dist):
        '''Makes vehicle move slow in game'''
        spaces = random.randint(math.floor(self._min_speed * 0.5), math.floor(self._max_speed * 0.5))
        self._position += spaces

        if spaces >= dist:
            return self._name + f" slowly and safely moves around the obstable {spaces} units!"
        
        return self._name + f" slowly moves {spaces} units!"
    

    def __str__(self):
        '''Returns vehicle as a string'''
        return self._name + f" [Position - {self._position}, Energy - {self._energy}]"
    

    @abc.abstractmethod
    def description_string(self):
        '''Returns a description string for a specific vehicle subclass'''
        pass


    @abc.abstractmethod
    def special_move(self, dist):
        '''Allows a vehicle subclass to use its special move'''
        pass
    