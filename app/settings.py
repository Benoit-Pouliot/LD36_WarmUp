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
