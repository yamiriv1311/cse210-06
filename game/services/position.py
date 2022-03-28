class Position:
    """ 
    this will set the position of a character 
    Atributes:
        _X (int) : this is the position in x
        _y (int) : this is the position in y
        _scale (int) : the scale of the position
    Author:Karras
    """
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

    def equals(self,charcterA,charcterB):
        """ Compares positions between two characters
            return: bool
        """
        if charcterA.get_x_position() == charcterB.get_x_position() and charcterA.get_y_position() == charcterB.get_y_position():
            return True
            
    def scale_x_position(self,xdirection):
        """ Scales the position according to the direcction 
            return: int
        """
        if xdirection > 0:
            return self._scale
        elif xdirection < 0:
            return - self._scale