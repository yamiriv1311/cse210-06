import random 
from constants import *
class Collision():
    def __init__(self):
        pass

    def is_colliding(self,charA,charB):
        if charA.get_x_position() == charB.get_x_position() and charA.get_y_position() == charB.get_y_position():
            return True

    def calculate_noncollision_direction(self,charA,charB):
        randomNum = random.randint(1,2)
        x = ""
        y = ""

        if self.is_colliding_in_x_right(charA,charB,20):
            x = X_POSITIVE
        
        elif self.is_colliding_in_x_left(charA,charB,20):
            x = X_NEGATIVE
        
        if self.is_colliding_in_y_up(charA,charB,20):
            y = Y_NEGATIVE
        
        if self.is_colliding_in_y_down(charA,charB,20):
            y = Y_POSITIVE
        
        if randomNum == 1:
            return x
        else: 
            return y

    def is_colliding_in_x(self,charA,charB):

        if (charA.get_x_position() + 20) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return X_NEGATIVE
        elif (charA.get_x_position() - 20) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return X_POSITIVE
        
    def is_colliding_in_y(self,charA,charB):
        if (charA.get_y_position() + 20) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return Y_NEGATIVE
        elif (charA.get_y_position() - 20) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return Y_POSITIVE

    def is_colliding_in_x_right(self,charA,charB,scale):
        
        if (charA.get_x_position() + scale) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return True
        else:
            return False
    
    def is_colliding_in_x_left(self,charA,charB,scale):

        if (charA.get_x_position() - scale) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return True
        else:
            return False

    def is_colliding_in_y_up(self,charA,charB,scale):
        
        if (charA.get_y_position() - scale) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return True
        else:
            return False

    def is_colliding_in_y_down(self,charA,charB,scale):
        if (charA.get_y_position() + scale) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return True
        else:
            return False