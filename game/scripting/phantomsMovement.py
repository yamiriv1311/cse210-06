from game.scripting.movement import Movement
from constants import *

class PhantomsMovement(Movement):
    def __init__(self):
        pass
    
    def movement(self,phantom):

        phantomsDirection = phantom.get_direction()
        direction = self.check_direction(phantomsDirection)
        calculation = 0
        
        if direction == X_POSITION:
            if phantomsDirection == X_POSITIVE:
                calculation = int(((phantom.get_x_position() + 1)) % WIDTH)
            else:
                calculation = int(((phantom.get_x_position() - 1)) % WIDTH)

            self.__set_new_position(phantom,direction,calculation)

        else:
            if phantomsDirection == Y_POSITIVE:
                calculation = int(((phantom.get_y_position() + 1)) % HEIGHT)
            else:
                calculation = int(((phantom.get_y_position() - 1)) % HEIGHT)
                
            self.__set_new_position(phantom,direction,calculation)

    def check_direction(self,direction):
        response = ""
        if direction == X_NEGATIVE or direction == X_POSITIVE:
            response = X_POSITION
        else:
            response = Y_POSITION
        return response
    
    def __set_new_position(self,phantom,direction,positionValue):
        if direction == X_POSITION:
            phantom.set_x_position(positionValue)
        else:
            phantom.set_y_position(positionValue)
