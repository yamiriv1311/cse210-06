class Collision():
    def __init__(self):
        pass

    def is_colliding(self,charA,charB):
        if charA.get_x_position() == charB.get_x_position() and charA.get_y_position() == charB.get_y_position():
            return True

    def is_colliding_in_x(self,charA,charB):
        if charA.get_x_position() == charB.get_x_position():
            return True

    def is_colliding_in_y(self,charA,charB):
        if charA.get_y_position() == charB.get_y_position():
            return True