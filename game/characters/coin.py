from game.characters.character import Character

class Coin(Character):
    def __init__(self,groupName, appearance, x, y, fontSize, color=""):
        super().__init__(appearance, x, y, fontSize, 0, color)
        self._group_name = groupName
        self._direction = ""
        self._value = 0

    def passing_over_item(self, coinStorage,index):
        coinStorage.pop(index)
        return self._value
    
    def get_group_name(self):
        return self._group_name
    
    def set_direction(self, direction):
        self._direction = direction

    def get_direction(self):
        return self._direction

    def set_coin_value(self,value):
        self._value = value

    def get_coin_value(self):
        return self._value