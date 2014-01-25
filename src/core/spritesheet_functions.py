'''
Created on 17.1.2014

ripped from http://programarcadegames.com/python_examples/sprite_sheets/
'''

import pygame
from constants import *

class SpriteSheet():
# This points to our sprite sheet image
    sprite_sheet = None
    def __init__(self, file_name):
    # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
        
    def getImage(self, x, y, width, height, colorkey):
        """ Grab a single image out of a larger spritesheet
           Pass in the x, y location of the sprite
           and the width and height of the sprite. """
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height) )
        # setting the transparent colour
        image.set_colorkey(colorkey)
        # Return the image
        return image
    
