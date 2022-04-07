from distutils.command.upload import upload
from constants import *
from game.scripting.action import Action
from game.services.keyboard import KeyboardService

class InputController(Action):
    """ all the behaviors related to the input of a player are managed here """
    def __init__(self,charStorage):
        self._keyboard_service = KeyboardService()
        self._char_storage = charStorage
        self._is_playing = False
        
    def execute(self,isPlaying,isGameOver=False):
        
        if isPlaying:
            pacman = self._char_storage.get_character(PACMAN_GROUP)[0]
            self.set_direction(pacman)
        
        if not isPlaying and not isGameOver:
            if self._keyboard_service.get_key_pressed() == 257:
                return True
        elif not isPlaying and isGameOver:
            if self._keyboard_service.get_key_pressed() == 257:
                return RESTART

    def set_game_state(self, state):
        self._is_playing = state

    def get_game_state(self):
        return self._is_playing
    
    def set_direction(self,character):
        
        keyboardDirection = self._keyboard_service.get_direction()
        pacmanDirection = character.get_direction()
            
        if isinstance(pacmanDirection,str) or pacmanDirection == "": 
            if keyboardDirection != "":
                character.set_direction(keyboardDirection)
                
    

