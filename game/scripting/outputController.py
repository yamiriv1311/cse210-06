from game.scripting.action import Action
from constants import *

class OutputController(Action):

    def __init__(self,videoServices,charStorage):
        self._video_services = videoServices
        self._char_storage = charStorage

    def execute(self,isPlaying,isGameOver=False):
        #-----------score banner variables-----------#
        score = self._char_storage.get_character(SCORE_GROUP)[0]
        scoreBanner = self._char_storage.get_character(SCORE_BANNER_GROUP)[0]
        scoreBanner.set_text(SCORE_TEXT +" "+ str(score.get_score()))
        life = self._char_storage.get_character(LIFE_GROUP)[0]
        #print(len(self._char_storage.get_character(LIFE_GROUP)))
        lifeBanner = self._char_storage.get_character(LIFE_BANNER_GROUP)[0]
        lifeBanner.set_text(LIFE_TEXT+" "+str(int(life.get_life_number()/2)))
        #--------------------------------------------#
        if isPlaying and not isGameOver:
            self._video_services.draw_all_characters(self._char_storage.get_character(WALL_GROUP))
            self._video_services.draw_all_characters(self._char_storage.get_character(COIN_GROUP))
            self._video_services.draw_all_characters(self._char_storage.get_character(PHANTOM_GROUP))
            self._video_services.draw_character(self._char_storage.get_character(PACMAN_GROUP)[0])
            self._video_services.draw_banner(scoreBanner)
            self._video_services.draw_banner(lifeBanner)

        elif not isPlaying and not isGameOver:
            self._video_services.draw_all_characters(self._char_storage.get_character(WALL_GROUP))
            self._video_services.draw_banner(scoreBanner)
            self._video_services.draw_banner(self._char_storage.get_character(START_GROUP)[0])
            self._video_services.draw_banner(self._char_storage.get_character(START_GROUP)[1])
        elif isGameOver and not isPlaying:
            self._video_services.draw_banner(scoreBanner)
            self._video_services.draw_banner(lifeBanner)
            self._video_services.draw_all_characters(self._char_storage.get_character(WALL_GROUP))
            self._video_services.draw_banner(scoreBanner)
            self._video_services.draw_banner(self._char_storage.get_character(GAME_OVER_GROUP)[0])
            self._video_services.draw_banner(self._char_storage.get_character(START_GROUP)[0])
        
        elif isGameOver and isPlaying:
            
            self._video_services.draw_all_characters(self._char_storage.get_character(WALL_GROUP))
            self._video_services.draw_banner(self._char_storage.get_character(WIN_GROUP)[0])
