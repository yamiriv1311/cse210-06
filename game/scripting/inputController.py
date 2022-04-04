from constants import CELL_SIZE, INPUT, PACMAN, PACMAN_GROUP
from game.scripting.action import Action
from game.services.keyboard import KeyboardService
from game.characters.charaterStorage import CharacterStorage
from game.scripting.pacmanMovement import pacmanMovement


class InputController(Action):
    """ all the behaviors related to the input of a player are managed here """
    def __init__(self):
        self._keyboard_service = KeyboardService()
        self._char_storage = CharacterStorage()
        
        
    def execute(self):
        pacman = CharacterStorage.get_character(PACMAN, PACMAN_GROUP)
        velocity = self._keyboard_service.get_direction()
        pacman.set_velocity(velocity) 
        
        