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
        
        if self.is_colliding_in_x(charA,charB) is not None:
            x = self.is_colliding_in_x(charA,charB)
        
        if self.is_colliding_in_y(charA,charB) is not None:
            y = self.is_colliding_in_y(charA,charB)
        
        
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