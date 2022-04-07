""" from asyncio import constants
from tkinter.tix import CELL """
from constants import *
from game.manager.scene_manager import SceneManager
from game.characters.charaterStorage import CharacterStorage
from game.scripting.script import Script
from game.services.videoServices import VideoServices

class Director:
    def __init__(self):
        self._scene_manager = SceneManager()
        self._video_service = VideoServices(WIDTH,HEIGHT,GAME_NAME,FRAMES,CELL_SIZE)
        self._character_storage = CharacterStorage()
        self._script = Script()
        self._is_playing = False
        self._is_game_over = False

    def start_game(self):
        
        self.prepare_scenario()
        self._video_service.open_window()
        while self._video_service.is_playing():

            input = self._script.get_actions(INPUT)
            update = self._script.get_actions(UPDATE)
            output = self._script.get_actions(OUTPUT)

            self._video_service.start_drawing()
            self._execute_actions(input,self._is_playing,self._is_game_over)
            self._execute_actions(update,self._is_playing)
            self._execute_actions(output,self._is_playing,self._is_game_over)

            self._video_service.stop_drawing()
        self._video_service.close_window()
    
    def _execute_actions(self,actions,isplaying,isGameOver=False):  
        for action in actions:
            response = action.execute(isplaying,isGameOver) 
            if response is not None and response:
                self._is_playing = True

            if response == GAME_OVER:
                self._is_game_over = True
                self._is_playing = False
            
            if response == RESTART:
                self._character_storage = []
                self._character_storage = CharacterStorage()
                self._script = []
                self._script = Script()
                self._is_playing = True
                self._is_game_over = False
                self.prepare_scenario()

    def prepare_scenario(self):
        self._scene_manager.prepare_scene(self._video_service,self._character_storage,self._script)