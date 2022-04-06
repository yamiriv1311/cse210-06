from game.scripting.action import Action
from constants import *

class OutputController(Action):

    def __init__(self,videoServices,charStorage):
        self._video_services = videoServices
        self._char_storage = charStorage

    def execute(self,isPlaying):
        #-----------score banner variables-----------#
        score = self._char_storage.get_character(SCORE_GROUP)[0]
        scoreBanner = self._char_storage.get_character(SCORE_BANNER_GROUP)[0]
        scoreBanner.set_text(SCORE_TEXT +" "+ str(score.get_score()))
        #--------------------------------------------#
        if isPlaying:
            self._video_services.draw_all_characters(self._char_storage.get_character(WALL_GROUP))
            self._video_services.draw_all_characters(self._char_storage.get_character(COIN_GROUP))
            self._video_services.draw_all_characters(self._char_storage.get_character(PHANTOM_GROUP))
            
            self._video_services.draw_character(self._char_storage.get_character(PACMAN_GROUP)[0])
            self._video_services.draw_banner(scoreBanner)
            self._video_services.draw_banner(self._char_storage.get_character(LIFE_GROUP)[0])

        else:
            self._video_services.draw_all_characters(self._char_storage.get_character(WALL_GROUP))
            self._video_services.draw_banner(scoreBanner)
            self._video_services.draw_banner(self._char_storage.get_character(START_GROUP)[0])
            self._video_services.draw_banner(self._char_storage.get_character(START_GROUP)[1])
