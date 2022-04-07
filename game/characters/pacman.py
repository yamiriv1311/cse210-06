from tokenize import group
from game.characters.character import Character
from game.characters.game_item import GameItem

class PacMan(Character, GameItem):
    def __init__(self,groupName, pacman, x, y, fontSize, color=""):
       super().__init__(pacman, x, y, fontSize, 0, color)
       self._group_name = groupName
       self._direction = ""
        
    def passing_over_item(self, over=False):
       return super().passing_over_item(over)
    
    def get_group_name(self):
       return self._group_name

    def set_direction(self, direction):
       self._direction = direction

    def get_direction(self):
       return self._direction


