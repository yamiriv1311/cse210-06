from game.scripting.action import Action
from constants import *
from game.scripting.phantomsAction import PhantomsAction
from game.scripting.pacmansAction import PacmansAction

class UpdateController(Action):
    """ All the behaviors related with the update of inputs etc are managed here """
    def __init__(self,videoServices,charStorage):
        self._video_services = videoServices
        self._char_storage = charStorage
    
    def execute(self,isplaying):

        #-----------------Phantoms and Pacman behavior----------------------#
        if isplaying:
            phantoms = self._char_storage.get_character(PHANTOM_GROUP)
            pacman = self._char_storage.get_character(PACMAN_GROUP)[0]
            score = self._char_storage.get_character(SCORE_GROUP)[0]

            phantomsAction = PhantomsAction(phantoms,self._char_storage)
            pacmansAction = PacmansAction(pacman,self._char_storage,score)
            pacmansAction.execute()
            phantomsAction.execute()