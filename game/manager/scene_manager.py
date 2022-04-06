from constants import *
import csv
from game.characters.wall import Wall
from game.characters.pacman import PacMan
from game.scripting.outputController import OutputController
from game.scripting.inputController import InputController
from game.scripting.updateController import UpdateController
from game.characters.banner import Banner
from game.characters.phantom import Phantom
from game.characters.coin import Coin
from game.characters.score import Score

class SceneManager():
    def __init__(self):
        self._video_services = ""
        self._char_storage = ""
        self._scripts = ""
        self._is_playing = False

    def set_video_services(self,video):
        self._video_services = video

    def set_char_storage(self,storage):
        self._char_storage = storage

    def set_scripts(self,scripts):
        self._scripts = scripts

    def prepare_scene(self,video,storage,scripts):
        
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

        #prepare start game menu
        self.__prepare_start_game_menu()

        #set the state of the game
        self.set_game_state()

        #prepare game over view
        self.__prepare_game_over()

    def __prepare_game_background(self):
        #prepare the score banner
        self.__prepare_score_banner()

        #prepare life
        self.__prepare_lives()

        #prepare score
        self.__prepare_score()

        with open(LEVEL_FILE,'r') as file:
            reader = csv.reader(file)
            for row,val in enumerate(reader):
                for col,v in enumerate(val):
                    self.__add_walls(row,col,v)
                    self.__add_pacman(row,col,v)
                    self.__add_phantoms(row,col,v)
                    self.__add_coins(row,col,v)

    
    def __prepare_scripts(self):
        self._scripts.add_action(INPUT,InputController(self._char_storage))
        self._scripts.add_action(UPDATE,UpdateController(self._video_services,self._char_storage))
        self._scripts.add_action(OUTPUT,OutputController(self._video_services,self._char_storage))
        

    def __add_walls(self,row,col,item):
        
        if int(item) == 1:            
            newWall = Wall(WALL_GROUP,WALL,int(col*CELL_SIZE),int(row*CELL_SIZE),FONT_SIZE,BLUE)
            self.__add_to_char_storage(WALL_GROUP,newWall)
    
    def __add_pacman(self, row, col, item):
        if int(item) == 2:            
            pacman_char = PacMan(PACMAN_GROUP,PACMAN,int(col*CELL_SIZE),int(row*CELL_SIZE),FONT_SIZE,YELLOW)
            self.__add_to_char_storage(PACMAN_GROUP,pacman_char)

    def __add_phantoms(self,row,col,item):
        if int(item) == 3:
            phantom = Phantom(PHANTOM_GROUP,PHANTOM,int(col*CELL_SIZE),int(row*CELL_SIZE),FONT_SIZE)
            self.__add_to_char_storage(PHANTOM_GROUP,phantom)

    def __prepare_score_banner(self):
        scoreBanner = Banner(0,0,FONT_SIZE,WHITE,SCORE_BANNER_GROUP)
        scoreBanner.set_text(SCORE_TEXT)
        self.__add_new_score_banner(scoreBanner)

    def __add_new_score_banner(self,scoreBanner):
        self._char_storage.add_new_character(SCORE_BANNER_GROUP,scoreBanner)

    def __add_to_char_storage(self,groupName,character):
        self._char_storage.add_new_character(groupName,character)
    
    def __add_coins(self,row,col,item):
        if int(item) == 4:
            coin = Coin(COIN_GROUP,COIN,int(col*CELL_SIZE),int(row*CELL_SIZE),FONT_SIZE,WHITE)
            coin.set_coin_value(COIN_VALUE)
            self.__add_to_char_storage(COIN_GROUP,coin)

    def __prepare_lives(self):
        lifeBanner = Banner(int((WIDTH/2) + (WIDTH/4)) ,0,FONT_SIZE,WHITE,LIFE_GROUP)
        lifeBanner.set_text(LIFE_TEXT+" "+str(LIVES_NUM))
        self.__add_new_lives(lifeBanner)

    def __add_new_lives(self,livesBanner):
        self._char_storage.add_new_character(LIFE_GROUP,livesBanner)
    
    def __prepare_start_game_menu(self):
        startBanner = Banner(int((WIDTH/2) - (WIDTH/3)) - (CELL_SIZE *3) ,int(HEIGHT/3),FONT_SIZE,WHITE,START_GROUP)
        instructionBanner = Banner(int((WIDTH/2) - (WIDTH/3)) ,int(HEIGHT/3) + CELL_SIZE,FONT_SIZE,WHITE,START_GROUP)
        startBanner.set_text(START_TEXT)
        instructionBanner.set_text(INSTRUCTION_TEXT)
        self.__add_start_banner(instructionBanner)
        self.__add_start_banner(startBanner)
    
    def __add_start_banner(self,startBanner):
        self._char_storage.add_new_character(START_GROUP,startBanner)
    
    def set_game_state(self):
        state = self._scripts.get_actions(INPUT)[0]
        self._is_playing = state.get_game_state()
    
    def __prepare_game_over(self):
        banner = Banner(int((WIDTH/2) - (WIDTH/3)) - (CELL_SIZE *3) ,int(HEIGHT/3),FONT_SIZE,WHITE,GAME_OVER_GROUP)
        banner.set_text(GAME_OVER_TEXT)
        self.__add_start_banner(banner)

    def __prepare_score(self):
        score = Score(0,SCORE_GROUP)
        self._char_storage.add_new_character(SCORE_GROUP,score)