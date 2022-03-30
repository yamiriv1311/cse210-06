from game.services.position import Position
from game.characters.game_item import GameItem

class Banner(Position,GameItem):

    """
    Banner class is going to be another child class from Characters class. 
    It will create the character that the player two will be using (red)

    Attributes:

    Author:Samuel
    """
    def __init__(self, x, y,fontSize,color,groupName):
        super().__init__(x = x,y = y, scale = 0)
        self._text = ""
        self._font_size = fontSize
        self._color = color
        self._group_name = groupName
    
    def set_text(self,text):
        self._text = text

    def get_text(self):
        return self._text
    
    def get_color(self):
        return self._color

    def get_group_name(self):
        return self._group_name

    def get_font_size(self):
        return self._font_size