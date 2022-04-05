from hashlib import new

from pyray import KEY_Y
from constants import *
import csv
from game.characters.wall import Wall
from game.characters.pacman import PacMan
from game.scripting.outputController import OutputController
from game.scripting.inputController import InputController
from game.scripting.updateController import UpdateController
from game.characters.banner import Banner


class SceneManager():
    def __init__(self):
        self._video_services = ""
        self._char_storage = ""
        self._scripts = ""
        self._keyboard_service = ""

    def set_video_services(self,video):
        self._video_services = video

    def set_char_storage(self,storage):
        self._char_storage = storage

    def set_scripts(self,scripts):
        self._scripts = scripts

    def set_keyboard_services(self, keyboard):
        self._keyboard_service = keyboard

    def prepare_scene(self,video,storage,scripts, keyboard):
        #Vide service
        self.set_video_services(video)

        #Storage
        self.set_char_storage(storage)

        #Scripts
        self.set_scripts(scripts)

        #preparation of the game background
        self.__prepare_game_background()

        #preparation of scripts
        self.__prepare_scripts()

        #prepare the score banner
        self.__prepare_score()

        #Keyboard services
        self.set_keyboard_services(keyboard)


    def __prepare_game_background(self):
        
        with open(LEVEL_FILE,'r') as file:
            reader = csv.reader(file)
            for row,val in enumerate(reader):
                for col,v in enumerate(val):
                    self.__add_walls(row,col,v)
                    self.__add_pacman(row,col,v)

    
    def __prepare_scripts(self):
        self._scripts.add_action(INPUT,InputController(self._keyboard_service,self._char_storage))
        self._scripts.add_action(UPDATE,UpdateController())
        self._scripts.add_action(OUTPUT,OutputController(self._video_services,self._char_storage))
        

    def __add_walls(self,row,col,wall):
        
        if int(wall) == 1:            
            newWall = Wall(WALL_GROUP,"X",int(col*CELL_SIZE),int(row*CELL_SIZE),FONT_SIZE,BLUE)
            self._char_storage.add_new_character(WALL_GROUP,newWall)
    
    def __add_pacman(self, row, col, wall):
        if int(wall) == 2:            
            pacman_char = PacMan(PACMAN_GROUP,PACMAN,int(col*CELL_SIZE),int(row*CELL_SIZE),FONT_SIZE,YELLOW)
            self._char_storage.add_new_character(PACMAN_GROUP,pacman_char)


    def __prepare_score(self):
        scoreBanner = Banner(0,0,20,WHITE,SCORE_GROUP)
        scoreBanner.set_text(SCORE_TEXT)
        self.__add_new_score(scoreBanner)

    def __add_new_score(self,scoreBanner):
        self._char_storage.add_new_character(SCORE_GROUP,scoreBanner)