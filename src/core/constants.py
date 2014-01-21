'''

@author: DannyUfonek
'''

import pygame
import os

""" This class is to make the code more readable by replacing values with names in CAPITALS
and with _
"""

"""----------------------------------PATHS-------------------------------"""
'''This is a bit problematic, as the paths have to be found first'''

# general paths
PROJECT_PATH = os.getcwd().rpartition(os.path.normcase('/src'))[0] #this splits the current directory and outputs first part of the 3-tuple

SPRITESHEET_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/spritesheets'))
FONT_PATH = os.path.join(PROJECT_PATH, os.path.normcase('resources/fonts'))

# specific paths
BUTTON_SPRITESHEET_PATH = os.path.join(SPRITESHEET_PATH, 'buttonsprite.png')
MAIN_MENU_FONT_PATH = os.path.join(FONT_PATH, 'cranberry gin.ttf')

"""----------------------------------COLOURS-------------------------------"""
BLACK = (0 ,0, 0)
WHITE = (255,255,255)
FULL_RED = (255,0,0)

"""----------------------------------RESOLUTION-------------------------------"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""----------------------------------MISC-------------------------------"""
MENU_BACKGROUND = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
MENU_BACKGROUND.fill(BLACK)

GAME_CLOCK = pygame.time.Clock()


