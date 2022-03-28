from constants import *
from game.manager.scene_manager import SceneManager
from game.characters.charaterStorage import CharacterStorage
from game.scripting.script import Script
from game.services.videoServices import VideoServices

class Director():
    def __init__(self):
        self._scene_manager = SceneManager()
        self._video_service = VideoServices(WIDTH,HEIGHT,GAME_NAME,FRAMES,CELL_SIZE)
        self._character_storage = CharacterStorage()
        self._script = Script()

    def start_game(self):
        self._scene_manager.prepare_scene(self._video_service,self._character_storage,self._script)
        
        #self._video_service = self._scene_manager.get_video_services()

        self._video_service.open_window()
        while self._video_service.is_playing():
            self._video_service.start_drawing()
            self._script.get_actions(OUTPUT)[0].execute()
            self._video_service.stop_drawing()

        self._video_service.close_window()
    
