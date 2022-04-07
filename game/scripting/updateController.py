from game.scripting.action import Action
from constants import *
from game.scripting.phantomsAction import PhantomsAction
from game.scripting.pacmansAction import PacmansAction

class UpdateController(Action):
    """ All the behaviors related with the update of inputs etc are managed here """
    def __init__(self,videoServices,charStorage):
        self._video_services = videoServices
        self._char_storage = charStorage
        self._is_playing = False
    
    def execute(self,isplaying,isGameOver=False):
        
        #-----------------Phantoms and Pacman behavior----------------------#
        if isplaying:
            if isplaying:
                self._is_playing = True
            phantoms = self._char_storage.get_character(PHANTOM_GROUP)
            pacman = self._char_storage.get_character(PACMAN_GROUP)[0]
            score = self._char_storage.get_character(SCORE_GROUP)[0]
            life = self._char_storage.get_character(LIFE_GROUP)[0]
            coins = self._char_storage.get_character(COIN_GROUP)
            
            phantomsAction = PhantomsAction(phantoms,self._char_storage)
                
            pacmansAction = PacmansAction(pacman,self._char_storage,score,life)
            pacmansAction.execute()
            phantomsAction.execute()
            if life.get_life_number() < 1:
                return GAME_OVER
            
            if int(len(coins)*COIN_VALUE) == score.get_score():
                return WINNER
    
    def get_game_state(self):
        return self._is_playing