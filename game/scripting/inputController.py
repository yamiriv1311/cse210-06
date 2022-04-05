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
        self._is_playing = False
        
        
        
    def execute(self,isPlaying):
        """ pacman = CharacterStorage.get_character(PACMAN, PACMAN_GROUP)
        velocity = self._keyboard_service.get_direction()
        pacman = pacmanMovement()
        self._char_storage = CharacterStorage()
        pacman.set_velocity(velocity)  """
        
        if not isPlaying:
            if self._keyboard_service.get_key_pressed() == 257:
                self._is_playing = True
    
    def set_game_state(self, state):
        self._is_playing = state

    def get_game_state(self):
        return self._is_playing
