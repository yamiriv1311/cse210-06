from xmlrpc.client import boolean
from game.scripting.pacmanMovement import PacmanMovement
from game.scripting.action import Action
from game.scripting.collision import Collision
from constants import *
class PacmansAction(Action):
    def __init__(self,pacman,charStorage):
        self._pacman = pacman
        self._char_storage = charStorage
        self._movement = PacmanMovement()
        self._collision = Collision()
    
    def execute(self):
        pacmanDirection = self._pacman.get_direction()
        walls = self._char_storage.get_character(WALL_GROUP)

        if pacmanDirection != "" and isinstance(pacmanDirection,str):  
            direction = self._movement.check_direction(pacmanDirection)

            for wall in walls:
                if direction == X_POSITION:
                    self.is_colliding_in_x(self._pacman,wall)
                elif direction == Y_POSITION:
                    self.is_colliding_in_y(self._pacman,wall)
        
        self._movement.movement(self._pacman)
    
    def is_colliding_in_x(self,pacman,wall):
        pacmanDirection = pacman.get_direction()
        if pacmanDirection == X_POSITIVE:
            xRight = self._collision.is_colliding_in_x_right(pacman,wall)
            if xRight:
                pacman.set_direction("")
        
        elif pacmanDirection == X_NEGATIVE:
            xLeft = self._collision.is_colliding_in_x_left(pacman,wall)    
            if xLeft:                        
                pacman.set_direction("")
    
    def is_colliding_in_y(self,pacman,wall):
        pacmanDirection = pacman.get_direction()
        if pacmanDirection == Y_POSITIVE:
            yDown = self._collision.is_colliding_in_y_down(pacman,wall)
            if yDown:
                pacman.set_direction("")

        elif pacmanDirection == Y_NEGATIVE:
            yUp = self._collision.is_colliding_in_y_up(pacman,wall)
            if yUp:
                pacman.set_direction("")