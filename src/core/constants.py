'''

@author: DannyUfonek
'''

import pygame
import os
import collections
from core.resourceLoader import ImageLoader

""" This class is to make the code more readable by replacing values with names in CAPITALS
and with _ and to make the code overall consistent and better :3
"""
print("loading game constants")

pygame.init()

"""----------------------------------PATHS & FILE NAMES-------------------------------"""
# file names
BUTTON_SPRITESHEET_NAME = 'buttonsprite'

# general paths
PROJECT_PATH = os.getcwd().rpartition(os.path.normcase('/src'))[0] #this splits the current directory and outputs first part of the 3-tuple
SCREENSHOT_PATH = os.path.join(PROJECT_PATH, os.path.normcase('screenshots'))

SPRITES_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/sprites'))
FONT_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/fonts'))
BACKGROUND_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/backgrounds'))
TEXTS_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/texts'))
SAVE_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/save'))
LEVELS_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/levels'))
SOUNDS_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/sfx'))

#@TODO: remove and replace with appropriate resourceLoaders
BUTTON_SPRITESHEET_PATH = os.path.join(SPRITES_PATH, 'buttonsprite.png')
MAIN_MENU_FONT_PATH = os.path.join(FONT_PATH, 'Smilecomix.ttf')
MAIN_TITLE_FONT_PATH = os.path.join(FONT_PATH, 'njnaruto.ttf')
MAIN_MENU_BACKGROUND_PATH = os.path.join(BACKGROUND_PATH, 'IMG_2905.PNG')
TIPDICT_PATH = os.path.join(TEXTS_PATH, 'tipDict')
SETTINGS_PATH = os.path.join(PROJECT_PATH, "settings")

"""----------------------------------COLOURS-------------------------------"""
#@TODO: Add some more colours
BLACK = pygame.Color(0,0,0,255)
TRANSPARENT_BLACK = pygame.Color(0,0,0,155)
WHITE = pygame.Color(255,255,255,255)
FULL_RED = pygame.Color(255,0,0,255)
FULL_GREEN = pygame.Color(0,255,0,255)
FULL_BLUE = pygame.Color(0,255,0,255)

FULL_MAGENTA = pygame.Color(255,0,255,255)

SHINY_CYAN = pygame.Color(100,240,255,255)
"""----------------------------------LEYRZ-LAYERS-------------------------------"""

PAUSE_LAYER = 4
DEBUG_LAYER = 6

"""----------------------------------RESOLUTION & RELATED-------------------------------"""
RES_MENU_WIDTH = 1000
RES_MENU_HEIGHT = 800
SCREEN_RECT_W1 = pygame.Rect(0,0,1200,1000)
SCREEN_RECT_W2 = pygame.Rect(0,0,1600,1000)
SCREEN_RECT_F1 = pygame.Rect(0,0,1280,1024)
SCREEN_RECT_F2 = pygame.Rect(0,0,1920,1080)
SCREEN_RECT_F3 = pygame.Rect(0,0,1920,1200)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
# playable area
GAME_SCREEN_RECT = pygame.Rect(0,0,900,1000)
PLAYABLE_RECT = pygame.Rect(0,0,GAME_SCREEN_RECT.width,350)
#coordinates of button column in menus
BUTTON_COLUMN_TOP = 200
BUTTON_COLUMN_LEFT = 200
"""----------------------------------SOUNDS-------------------------------"""
SFX_SELECT = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'select1.wav'))
SFX_CLICK = pygame.mixer.Sound(os.path.join(SOUNDS_PATH, 'click.wav'))

"""----------------------------------RESOURCES COLLECTIONS-------------------------------"""
def _backgroundCollectionInit():
    print ("creating background collection...")
    backgroundCollection = ImageLoader()
    # find all backgrounds and add them to collection
    for background in os.listdir(BACKGROUND_PATH):
        backgroundCollection.__setattr__(background.rpartition(os.path.normcase('.'))[0], os.path.join(BACKGROUND_PATH, background))
        # add name of file (without the .png suffix) and full path to dictionary
    print("created background collection that includes: ")
    print(backgroundCollection.names)
    return backgroundCollection

BACKGROUND_COLLECTION = _backgroundCollectionInit()

def _gameSpritesCollectionInit():
    print ("creating spritesheet collection...")
    gameSpritesCollection = ImageLoader()
    # find all spritesheets and add them to collection
    for spritesheet in os.listdir(SPRITES_PATH):
        gameSpritesCollection.__setattr__(spritesheet.rpartition(os.path.normcase('.'))[0], os.path.join(SPRITES_PATH, spritesheet))
        # add name of file (without the .png suffix) and full path to dictionary
    print("created spritesheet collection that includes: ")
    print(gameSpritesCollection.names)
    return gameSpritesCollection
    
GAME_IMAGE_COLLECTION = _gameSpritesCollectionInit()

#@TODO: sound and font collections!
"""----------------------------------SETTINGS - PRIVATE-------------------------------"""
''' these are set by settingsHandler. They're empty otherwise'''
_SETTINGS = {
'MUSIC_VOLUME':100,
'SOUND_VOLUME':100
}
'''
settingNumbers: 0:MOVE_UP, 1:MOVE_DOWN, 2:MOVE_LEFT, 3:MOVE_RIGHT, 4:PAUSE, 5:ATTACK, 6:MUSIC_VOLUME, 7:SOUND_VOLUME
'''
_ALLOWED_KEYS = []
"""----------------------------------EXCEPTIONS-------------------------------"""
class TipException(Exception):
    pass
class ExceptionalException(Exception):
    pass
"""----------------------------------MISC-------------------------------"""

TIP_FIELD_RECT = pygame.Rect(0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50)
GAME_FPS = 60
MAX_CLOUDS = 50
KEY_REPEAT_TIME = 10 #ms

print(" ")

