from game.scripting.action import Action
from game.scripting.phantomsMovement import PhantomsMovement
from game.scripting.collision import Collision
from constants import *

class PhantomsAction(Action):
    def __init__(self,phantoms,charStorage):
        self._phantoms = phantoms
        self._char_storage = charStorage
    
    def execute(self):
        movement = PhantomsMovement()
        collision = Collision()
        walls = self._char_storage.get_character(WALL_GROUP)

        for phantom in self._phantoms:
            for wall in walls:
                if collision.is_colliding(phantom,wall):
                    print(True)
                    #self.__move_phantom(self._phantoms,movement)
    

    def __move_phantom(self,phantoms,movement):

        for p in phantoms:
            movement.movement(p)
