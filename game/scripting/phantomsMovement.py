from game.scripting.movement import Movement

class PhantomsMovement(Movement):
    def __init__(self):
        pass
    
    def movement(self,character,direction = False):
        print("x: ",character.get_x_position())