from game.scripting.action import Action
from constants import *
from game.scripting.phantomsAction import PhantomsAction

class UpdateController(Action):
    """ All the behaviors related with the update of inputs etc are managed here """
    def __init__(self,videoServices,charStorage):
        self._video_services = videoServices
        self._char_storage = charStorage
    
    def execute(self,isplaying):

        #-----------------Phantoms behavior----------------------#
        if isplaying:
            phantoms = self._char_storage.get_character(PHANTOM_GROUP)
            phantomsAction = PhantomsAction(phantoms,self._char_storage)
            phantomsAction.execute()