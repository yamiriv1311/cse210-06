import random 

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

        if self.is_colliding_in_x_right(charA,charB):
            x = "+x"
        
        elif self.is_colliding_in_x_left(charA,charB):
            x = "-x"
        
        if self.is_colliding_in_y_up(charA,charB):
            y = "-y"
        
        if self.is_colliding_in_y_down(charA,charB):
            y = "+y"
        
        if randomNum == 1:
            return x
        else: 
            return y

    def is_colliding_in_x(self,charA,charB):

        if (charA.get_x_position() + 20) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return "-x"
        elif (charA.get_x_position() - 20) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return "+x"
        
    def is_colliding_in_y(self,charA,charB):
        if (charA.get_y_position() + 20) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return "-y"
        elif (charA.get_y_position() - 20) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return "+y"

    def is_colliding_in_x_right(self,charA,charB):
        
        if (charA.get_x_position() + 20) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return True
        else:
            return False
    
    def is_colliding_in_x_left(self,charA,charB):

        if (charA.get_x_position() - 20) ==  (charB.get_x_position()) and charA.get_y_position() ==  (charB.get_y_position()):
            return True
        else:
            return False

    def is_colliding_in_y_up(self,charA,charB):
        
        if (charA.get_y_position() - 20) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return True
        else:
            return False

    def is_colliding_in_y_down(self,charA,charB):
        if (charA.get_y_position() + 20) ==  (charB.get_y_position()) and charA.get_x_position() ==  (charB.get_x_position()):
            return True
        else:
            return False