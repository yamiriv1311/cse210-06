from constants import *

class PacmanMovement:
    def __init__(self):
      pass
    
    def movement(self,pacman):
        direction = self.check_direction(pacman.get_direction())
        positionValue = self.calculate_new_position(pacman,direction)
        self.__set_new_position(pacman,direction,positionValue)

    def check_direction(self,direction):
        response = ""
        if direction == X_NEGATIVE or direction == X_POSITIVE:
            response = X_POSITION
        elif direction == Y_NEGATIVE or direction == Y_POSITIVE:
            response = Y_POSITION
        return response

    def calculate_new_position(self,pacman,direction):
        pacmansDirection = pacman.get_direction()
        x = pacman.get_x_position()
        y = pacman.get_y_position()

        if direction == X_POSITION:
            if pacmansDirection == X_POSITIVE:
                calculation = int(((x + 20)) % WIDTH)
            else:
                calculation = int(((x - 20)) % WIDTH)

        else:
            if pacmansDirection == Y_POSITIVE:
                calculation = int(((y + 20)) % HEIGHT)
            else:
                calculation = int(((y - 20)) % HEIGHT)
        
        return calculation

    def __set_new_position(self,pacman,direction,positionValue):
        if direction == X_POSITION:
            pacman.set_x_position(positionValue)
        elif direction == Y_POSITION:
            pacman.set_y_position(positionValue)