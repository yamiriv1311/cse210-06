class Position:
    
    def __init__(self,x,y,scale = 0):
      self._x = x
      self._y = y  
      self._scale = scale
    
    def set_x_position(self,x):
        """ Sets the x position """
        self._x = x
    
    def set_y_position(self,y):
        """ Sets the x position """
        self._y = y
    
    def get_x_position(self):
        """ Gets the x position 
            return: int
        """
        return self._x
    
    def get_y_position(self):
        """ Gets the x position 
            return: int
        """
        return self._y
    
    def get_position(self):
        """ Gets the position
            return: Position
        """
        return Position(self._x,self._y)
            
    def scale_x_position(self,xdirection):
        """ Scales the position according to the direcction 
            return: int
        """
        if xdirection > 0:
            return self._scale
        elif xdirection < 0:
            return - self._scale