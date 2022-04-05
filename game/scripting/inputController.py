from constants import CELL_SIZE, INPUT, PACMAN, PACMAN_GROUP
from game.scripting.action import Action
from game.services.keyboard import KeyboardService
from game.characters.charaterStorage import CharacterStorage
from game.scripting.pacmanMovement import pacmanMovement


class InputController(Action):
    """ all the behaviors related to the input of a player are managed here """
    def __init__(self, storage):
        self._keyboard_service = KeyboardService()
        self._char_storage = storage
        
        
    def execute(self):
        pacman = pacmanMovement()
        velocity = self._keyboard_service.get_direction()
        pacman.set_velocity(velocity) 
        
        