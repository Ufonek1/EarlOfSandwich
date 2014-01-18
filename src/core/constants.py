'''
Created on 17.1.2014

@author: Hynek
'''

import pygame
import os

""" This class is to make the code more readable by replacing values with names in CAPITALS
and with _
"""

"""----------------------------------PATHS-------------------------------"""
'''This is a bit problematic, as the paths have to be found first'''

# general paths
RESOURCES_PATH = os.getcwd().rpartition(os.path.normcase('/src'))[0] #this splits the current directory and outputs first part of the 3-tuple
print ("located game directory at " + RESOURCES_PATH)

SPRITESHEET_PATH = os.path.join(RESOURCES_PATH, os.path.normcase('resources/spritesheets'))

# specific paths
BUTTON_SPRITESHEET_PATH = os.path.join(SPRITESHEET_PATH, 'buttonsprite.png')

"""----------------------------------COLOURS-------------------------------"""
BLACK = (0 ,0, 0)
WHITE = (255,255,255)
FULL_RED = (255,0,0)

"""----------------------------------RESOLUTION-------------------------------"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

