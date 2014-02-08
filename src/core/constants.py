'''

@author: DannyUfonek
'''

import pygame
import os
from core.resourceLoader import ImageLoader

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

SPRITES_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/sprites'))
FONT_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/fonts'))
BACKGROUND_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/backgrounds'))
TEXTS_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/texts'))
# specific paths (deprecated, to be removed in next version)
#@TODO: remove and replace with appropriate resourceLoaders
BUTTON_SPRITESHEET_PATH = os.path.join(SPRITES_PATH, 'buttonsprite.png')
MAIN_MENU_FONT_PATH = os.path.join(FONT_PATH, 'Polentical Neon Regular.ttf')
MAIN_MENU_BACKGROUND_PATH = os.path.join(BACKGROUND_PATH, 'IMG_2905.PNG')
TIPDICT_PATH = os.path.join(TEXTS_PATH, 'tipDict')

"""----------------------------------COLOURS-------------------------------"""
#@TODO: Add some more colours
BLACK = pygame.Color(0 ,0, 0)
WHITE = pygame.Color(255,255,255)
FULL_RED = pygame.Color(255,0,0)
FULL_MAGENTA = pygame.Color(255,0,255)
FULL_GREEN = pygame.Color(0,255,0)

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
    print("created background collection that includes: ")
    print(backgroundCollection.names)
    return backgroundCollection

BACKGROUND_COLLECTION = backgroundCollectionInit()

def gameSpritesCollectionInit():
    print ("creating spritesheet collection...")
    gameSpritesCollection = ImageLoader()
    # find all spritesheets and add them to collection
    for spritesheet in os.listdir(SPRITES_PATH):
        gameSpritesCollection.__setattr__(spritesheet.rpartition(os.path.normcase('.'))[0], os.path.join(SPRITES_PATH, spritesheet))
        # add name of file (without the .png suffix) and full path to dictionary
    print("created spritesheet collection that includes: ")
    print(gameSpritesCollection.names)
    return gameSpritesCollection
    
GAME_IMAGE_COLLECTION = gameSpritesCollectionInit()

#@TODO: sound and font collections!

"""----------------------------------MISC-------------------------------"""
#resized menu background
MENU_BACKGROUND = pygame.transform.scale(BACKGROUND_COLLECTION.menubackground, (SCREEN_WIDTH, SCREEN_HEIGHT))
TIP_FIELD_RECT = pygame.Rect(0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50)
GAME_FPS = 60

print(" ")

