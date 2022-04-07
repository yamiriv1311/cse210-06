from xmlrpc.client import boolean
from game.scripting.pacmanMovement import PacmanMovement
from game.scripting.action import Action
from game.scripting.collision import Collision
from constants import *
class PacmansAction(Action):
    def __init__(self,pacman,charStorage,score,life):
        self._pacman = pacman
        self._char_storage = charStorage
        self._movement = PacmanMovement()
        self._collision = Collision()
        self._score = score
        self._life = life
    
    def execute(self):

        pacmanDirection = self._pacman.get_direction()
        walls = self._char_storage.get_character(WALL_GROUP)
        coins = self._char_storage.get_character(COIN_GROUP)
        phantoms = self._char_storage.get_character(PHANTOM_GROUP)
        if pacmanDirection != "" and isinstance(pacmanDirection,str):  
        #--------------collision with a wall-----------#    

            direction = self._movement.check_direction(pacmanDirection)
            for wall in walls:
                if direction == X_POSITION:
                    response = self.is_colliding_in_x(self._pacman,wall,20)
                    if response == X_NEGATIVE or response == X_POSITIVE:
                        self._pacman.set_direction("")

                elif direction == Y_POSITION:
                    response = self.is_colliding_in_y(self._pacman,wall,20)
                    if response == Y_POSITIVE or response == Y_NEGATIVE:
                        self._pacman.set_direction("")
                    
        #-------------------------------------------------#
        
        #------------collision with a coin----------------#
            for i,coin in enumerate(coins):
                if direction == X_POSITION:
                    xCollision = self.is_colliding_in_x(self._pacman,coin,20)
                    if xCollision == X_POSITIVE or xCollision == X_NEGATIVE:
                        coin.passing_over_item(coins,i)
                        self.add_to_score(coin.get_coin_value())
                elif direction == Y_POSITION:
                    yCollision = self.is_colliding_in_y(self._pacman,coin,20)
                    if yCollision == Y_POSITIVE or yCollision == Y_NEGATIVE:
                        coin.passing_over_item(coins,i)
                        self.add_to_score(coin.get_coin_value())
                        
        #-------------------------------------------------#

        #------------collision with phantom----------------#
            
        for phantom in phantoms:
            phantomDirection = self._movement.check_direction(phantom.get_direction())
            
            isTouched = ""  
            phaCollision = self._collision.is_colliding(phantom,self._pacman)
            if phaCollision:
                isTouched = True

            if phantomDirection == X_POSITION :
                xPhaCollision = self.is_colliding_in_x(phantom,self._pacman,20)
                if xPhaCollision == X_POSITIVE or xPhaCollision == X_NEGATIVE:
                    isTouched = True
                
            elif phantomDirection == Y_POSITION:    
                yPhaCollision = self.is_colliding_in_y(phantom,self._pacman,20)
                if yPhaCollision == Y_POSITIVE or yPhaCollision == Y_NEGATIVE:
                    isTouched = True
            if isTouched:
                self._life.substract_from_life(phantom.passing_over_item())
            
        #-------------------------------------------------#

        self._movement.movement(self._pacman)
        
    def is_colliding_in_x(self,character1,character2,scale):
        response = ""
        pacmanDirection = character1.get_direction()
        if pacmanDirection == X_POSITIVE:
            xRight = self._collision.is_colliding_in_x_right(character1,character2,scale)
            if xRight:
                response = X_POSITIVE
        elif pacmanDirection == X_NEGATIVE:
            xLeft = self._collision.is_colliding_in_x_left(character1,character2,scale)    
            if xLeft:                        
                response = X_NEGATIVE
        return response
    
    def is_colliding_in_y(self,character1,character2,scale):
        response = ""
        pacmanDirection = character1.get_direction()
        if pacmanDirection == Y_POSITIVE:
            yDown = self._collision.is_colliding_in_y_down(character1,character2,scale)
            if yDown:
                response = Y_POSITIVE

        elif pacmanDirection == Y_NEGATIVE:
            yUp = self._collision.is_colliding_in_y_up(character1,character2,scale)
            if yUp:
                response = Y_NEGATIVE
        return response
    
    def add_to_score(self,value):
        self._score.add_to_score(value)