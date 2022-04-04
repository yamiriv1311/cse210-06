import pyray
from constants import CELL_SIZE
from game.services.position import Position


class KeyboardService():
  """Detects player input."""

  

  def get_direction(self):
    dx = 0
    dy = 0

    if pyray.is_key_down(pyray.KEY_LEFT):
      dx = -1
        
    if pyray.is_key_down(pyray.KEY_RIGHT):
      dx = 1
        
    if pyray.is_key_down(pyray.KEY_UP):
      dy = -1
        
    if pyray.is_key_down(pyray.KEY_DOWN):
      dy = 1

    direction = Position(dx, dy)
        
    return direction

  def get_key_pressed(self):
    return pyray.get_key_pressed()
