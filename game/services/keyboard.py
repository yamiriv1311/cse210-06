import pyray
from constants import CELL_SIZE
from game.services.position import Position
from constants import *

class KeyboardService():
  """Detects player input."""
  
  def get_direction(self):
    direction = ""
    if pyray.is_key_down(pyray.KEY_LEFT):
      direction = X_NEGATIVE
        
    if pyray.is_key_down(pyray.KEY_RIGHT):
      direction = X_POSITIVE
        
    if pyray.is_key_down(pyray.KEY_UP):
      direction = Y_NEGATIVE
        
    if pyray.is_key_down(pyray.KEY_DOWN):
      direction = Y_POSITIVE
        
    return direction

  def get_key_pressed(self):
    return pyray.get_key_pressed()
