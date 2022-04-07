class Life():
    def __init__(self,number,groupName):
        self._life_number = number
        self._group_name = groupName
    
    def set_life_number(self,number):
        self._life_number = number

    def get_life_number(self):
        return self._life_number

    def add_to_life(self,life):
        self._life_number = self._life_number + life 
    
    def substract_from_life(self,life):
        self._life_number = self._life_number - life 

    def get_group_name(self):
       return self._group_name