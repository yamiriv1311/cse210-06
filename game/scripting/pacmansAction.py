from xmlrpc.client import boolean
from game.scripting.pacmanMovement import PacmanMovement
from game.scripting.action import Action
from game.scripting.collision import Collision
from constants import *
class PacmansAction(Action):
    def __init__(self,pacman,charStorage,score):
        self._pacman = pacman
        self._char_storage = charStorage
        self._movement = PacmanMovement()
        self._collision = Collision()
        self._score = score
    
    def execute(self):

        pacmanDirection = self._pacman.get_direction()
        walls = self._char_storage.get_character(WALL_GROUP)
        coins = self._char_storage.get_character(COIN_GROUP)
        
        if pacmanDirection != "" and isinstance(pacmanDirection,str):  
        #--------------collision with a wall-----------#    

            direction = self._movement.check_direction(pacmanDirection)
            for wall in walls:
                if direction == X_POSITION:
                    response = self.is_colliding_in_x(self._pacman,wall)
                    if response == "-x" or response == "+x":
                        self._pacman.set_direction("")

                elif direction == Y_POSITION:
                    response = self.is_colliding_in_y(self._pacman,wall)
                    if response == "+y" or response == "-y":
                        self._pacman.set_direction("")
                    
        #-------------------------------------------------#
        
        #------------collision with a coin----------------#
            for i,coin in enumerate(coins):
                if direction == X_POSITION:
                    xCollision = self.is_colliding_in_x(self._pacman,coin)
                    if xCollision == "+x" or xCollision == "-x":
                        coin.passing_over_item(coins,i)
                        self.add_to_score(coin.get_coin_value())
                elif direction == Y_POSITION:
                    yCollision = self.is_colliding_in_y(self._pacman,coin)
                    if yCollision == "+y" or yCollision == "-y":
                        coin.passing_over_item(coins,i)
                        self.add_to_score(coin.get_coin_value())
                        
        #-------------------------------------------------#
        self._movement.movement(self._pacman)
        
    def is_colliding_in_x(self,pacman,character):
        response = ""
        pacmanDirection = pacman.get_direction()
        if pacmanDirection == X_POSITIVE:
            xRight = self._collision.is_colliding_in_x_right(pacman,character)
            if xRight:
                response = "+x"
        elif pacmanDirection == X_NEGATIVE:
            xLeft = self._collision.is_colliding_in_x_left(pacman,character)    
            if xLeft:                        
                response = "-x"
        return response
    
    def is_colliding_in_y(self,pacman,character):
        response = ""
        pacmanDirection = pacman.get_direction()
        if pacmanDirection == Y_POSITIVE:
            yDown = self._collision.is_colliding_in_y_down(pacman,character)
            if yDown:
                response = "+y"

        elif pacmanDirection == Y_NEGATIVE:
            yUp = self._collision.is_colliding_in_y_up(pacman,character)
            if yUp:
                response = "-y"
        return response
    
    def add_to_score(self,value):
        self._score.add_to_score(value)