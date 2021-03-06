# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BACKGROUND_COLOR = (255,255,255)

COLOR_MENU_1 = (242,214,136)
COLOR_MENU_2 = (0, 0, 0)
COLOR_MENU_FONTS = (0, 0, 0)

COLOR_MENU_SELECT_1 = (83, 45, 2)
COLOR_MENU_SELECT_2 = (255, 255, 255)
COLOR_MENU_FONTS_SELECT = (255,255,255)

#Main font
FONT_NAME = 'arial'

FPS = 60

#DIMENSION
# http://gamedevelopment.tutsplus.com/articles/quick-tip-what-is-the-best-screen-resolution-for-your-game--gamedev-14723
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
TILE_WIDTH = 32
TILE_HEIGHT = 32

# Development mode, DEV or OPT
DEV_MODE = 1
OPT_MODE = 0
MODE = DEV_MODE

#Scenes self.nextScene commands, used to tell SceneHandler what next scene to run after this one ends
TITLE_SCREEN = 0
WORLD_MAP = 1
PET_SCREEN = 2
WIN_SCREEN = 3
FOUND_ALL_PET_SCREEN = 4
PLATFORM_SCREEN = 42

# Sprite Layer
SPRITE_LAYER = 4

#Facing Sides
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

#Collisions
COLLISION_LAYER = 0
SOLID = 1 #Booléen de GID pour collision
SPIKE = 3
SPRING = 2

#Player jump states
GROUNDED = 0
JUMP = 1

#Physics
GRAVITY = 1
FRICTION = 0.8


# Dimension tile base for icon
TILEDIMX = 32
TILEDIMY = 32

# Animal type
NORMAL = 0
KEY_ANIMAL = 1
DEAD_END = 2
WINNER = 3

# If you add a Tag for debugging, you MUST set it here at 0 for everyone
# You can turn your tag on in your own settings_local.py for personal use

TAG_BP = 0
TAG_MARIE = 0

# Load settings_local.py if exist
try:
    app_info = __import__('imp').find_module('app')
    app = __import__('imp').load_module('app', *app_info)
    __import__('imp').find_module('settings_local', app.__path__)
    settingsLocalFound = True
except ImportError:
    settingsLocalFound = False

if settingsLocalFound:
    from app.settings_local import *
