class Score():
    def __init__(self,value,groupName):
        self._score = value
        self._group_name = groupName
    
    def set_score(self,score):
        self._score = score
    
    def get_score(self):
        return self._score

    def get_group_name(self):
       return self._group_name
    
    def add_to_score(self,point):
        self._score = self._score + point
    
    def substract_to_score(self,point):
        self._score = self._score - point