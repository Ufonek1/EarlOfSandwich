'''

@author: DannyUfonek
'''

import pygame
import os
from resourceLoader import ImageLoader

""" This class is to make the code more readable by replacing values with names in CAPITALS
and with _ and to make the code overall consistent and better :3
"""
print("loading game constants")

pygame.init()

"""----------------------------------PATHS & FILE NAMES-------------------------------"""
# file names
BUTTON_SPRITESHEET_NAME = 'buttonspritewhite'


# general paths
PROJECT_PATH = os.getcwd().rpartition(os.path.normcase('/src'))[0] #this splits the current directory and outputs first part of the 3-tuple

SPRITESHEET_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/spritesheets'))
FONT_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/fonts'))
BACKGROUND_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/backgrounds'))

# specific paths (deprecated, to be removed in next version)
#@TODO: remove!
BUTTON_SPRITESHEET_PATH = os.path.join(SPRITESHEET_PATH, 'buttonsprite.png')
MAIN_MENU_FONT_PATH = os.path.join(FONT_PATH, 'Polentical Neon Regular.ttf')
MAIN_MENU_BACKGROUND_PATH = os.path.join(BACKGROUND_PATH, 'IMG_2905.PNG')

"""----------------------------------COLOURS-------------------------------"""
#@TODO: Add some more colours
BLACK = (0 ,0, 0)
WHITE = (255,255,255)
FULL_RED = (255,0,0)
FULL_MAGENTA = (255,0,255)

"""----------------------------------RESOLUTION-------------------------------"""
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
"""----------------------------------RESOURCES-------------------------------"""
def backgroundCollectionInit():
    print ("creating background collection...")
    backgroundCollection = ImageLoader()
    # find all backgrounds and add them to collection
    for background in os.listdir(BACKGROUND_PATH):
        backgroundCollection.__setattr__(background.rpartition(os.path.normcase('.'))[0], os.path.join(BACKGROUND_PATH, background))
        # add name of file (without the .png suffix) and full path to dictionary
    print ("created background collection that includes: ")
    print backgroundCollection.names
    return backgroundCollection

BACKGROUND_COLLECTION = backgroundCollectionInit()

def gameSpritesheetCollectionInit():
    print ("creating spritesheet collection...")
    gameSpritesheetCollection = ImageLoader()
    # find all spritesheets and add them to collection
    for spritesheet in os.listdir(SPRITESHEET_PATH):
        gameSpritesheetCollection.__setattr__(spritesheet.rpartition(os.path.normcase('.'))[0], os.path.join(SPRITESHEET_PATH, spritesheet))
        # add name of file (without the .png suffix) and full path to dictionary
    print ("created spritesheet collection that includes: ")
    print gameSpritesheetCollection.names
    return gameSpritesheetCollection
    
GAME_SPRITESHEET_COLLECTION = gameSpritesheetCollectionInit()

#@TODO: sound and font collections!

"""----------------------------------MISC-------------------------------"""

GAME_FPS = 30

print(" ")

