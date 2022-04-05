
# Game specification
WIDTH = 600
HEIGHT = 600
GAME_NAME = "Pacman"
FRAMES = 20
CELL_SIZE = 20
COLS = 30
ROWS = 30
FONT_SIZE = 20
X_POSITION = "x"
Y_POSITION = "y"
X_POSITIVE = "+x" 
Y_POSITIVE = "+y"
Y_NEGATIVE = "-y"
X_NEGATIVE = "-x"

#Level file
#LEVEL_FILE = "assets/data/level{:1}" temporally commented for development purposes
LEVEL_FILE = "game/assets/data/level1.txt"

#color
BLUE = (0,0,139,250)
WHITE = (255,255,255,250)
YELLOW = (255,255,0,250)
#group Names
WALL_GROUP = "wall"
SCORE_GROUP = "score"
PACMAN_GROUP = "pacman"
PHANTOM_GROUP = "phantom"
COIN_GROUP = "coin"
LIFE_GROUP = "life"
START_GROUP = "start"
GAME_OVER_GROUP = "over"
#script actions
OUTPUT = "output"
INPUT = "input"
UPDATE = "update"

#texts
SCORE_TEXT = "Player score:"
LIFE_TEXT = "Life:"
START_TEXT = "Ready to play pakman?!! press enter and have fun."
INSTRUCTION_TEXT = "Remeber to get as much coins as possible"
GAME_OVER_TEXT = "Game over!! to try again press enter"

#characters
#PACMAN = "#$%"
PACMAN = "#0%"
WALL = "#X%"
#WALL = "X>"
PHANTOM = "-0m-"
COIN = "°"
#coin
COIN_VALUE = 10
LIVES_NUM = 3