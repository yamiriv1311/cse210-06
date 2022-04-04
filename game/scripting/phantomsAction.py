from game.scripting.action import Action
from game.scripting.phantomsMovement import PhantomsMovement
from game.scripting.collision import Collision
from constants import *

class PhantomsAction(Action):
    def __init__(self,phantoms,charStorage):
        self._phantoms = phantoms
        self._char_storage = charStorage
        self._movement = PhantomsMovement()

    def execute(self):
        collision = Collision()
        walls = self._char_storage.get_character(WALL_GROUP)
        self.__set_direction(collision,walls)
        self.__is_colliding_with_walls(collision,walls)
        self.__move_phantom(self._phantoms)

    

    def __move_phantom(self,phantoms):
        for phantom in phantoms:
            if phantom.get_direction() != "" and phantom.get_direction() != None:
                self._movement.movement(phantom)
        
    
    def __has_direction(self,phantom):
        if phantom.get_direction() is not None:
            response = True
            if phantom.get_direction() == "":
                response = False

            return response

    def __set_phantom_direction(self,phantom,direction):
        phantom.set_direction(direction)

    def __set_direction(self,collision,walls):
        direction = ""
        
        for phantom in self._phantoms:
            for wall in walls:
                if not self.__has_direction(phantom):    
                    direction = collision.calculate_noncollision_direction(phantom,wall)
                    self.__set_phantom_direction(phantom,direction)

    def __is_colliding_with_walls(self,collision,walls):
        for phantom in self._phantoms:
            phDirection = phantom.get_direction()
            direction = ""
            newDirection = ""
            if self.__has_direction(phantom):
                direction = self.check_direction(phDirection)
                for wall in walls:
                    if direction == X_POSITION:
                        
                        if collision.is_colliding_in_x(phantom,wall) is not None:
                            newDirection = collision.is_colliding_in_x(phantom,wall)
                            self.__set_phantom_direction(phantom,newDirection)
                    else:
                        if collision.is_colliding_in_y(phantom,wall) is not None:
                            newDirection = collision.is_colliding_in_y(phantom,wall)        
                            self.__set_phantom_direction(phantom,newDirection)

    def check_direction(self,direction):
        return self._movement.check_direction(direction)