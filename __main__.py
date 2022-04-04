
from game.characters.charaterStorage import CharacterStorage
from game.manager.director import Director
from game.services.keyboard import KeyboardService
from constants import CELL_SIZE, FONT_SIZE, PACMAN, YELLOW
from game.scripting.pacmanMovement import pacmanMovement
from game.services.position import Position

def main():

  keyboard_service = KeyboardService
  director = Director(keyboard_service)
  director.start_game()


main()