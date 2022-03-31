
from game.characters.charaterStorage import CharacterStorage
from game.characters.pacman import PacMan
from game.manager.director import Director
from game.services.keyboard import KeyboardService
from game.scripting.pacmanMovement import PacmanMovement
from game.services.videoServices import VideoServices
from game.manager.scene_manager import SceneManager
from constants import GAME_NAME, PACMAN, FONT_SIZE, YELLOW, CELL_SIZE, FRAMES, WIDTH, HEIGHT

def main():

  #start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    director = Director(keyboard_service)
    director.start_game()


if __name__ == "__main__":
    main()