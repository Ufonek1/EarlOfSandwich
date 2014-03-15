'''
Created on 17.1.2014

ripped from http://programarcadegames.com/python_examples/sprite_sheets/
'''

import pygame
from core.resourceLoader import ImageLoader
from core.constants import *

class SpriteSheet():
# This points to our sprite sheet image
    sprite_sheet = None
    def __init__(self, image_name_in_collection):
        ''' 
        Load the sprite sheet from the spritesheet collection. As image_name_in_collection is a variable,
        we have to call the resourceLoader's __getattr__ method, rather than just GAME_IMAGE_COLLECTION.image_name_in_collection
        '''
        self.sprite_sheet = GAME_IMAGE_COLLECTION.__getattr__(image_name_in_collection)
        
    def getImage(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
           Pass in the x, y location of the sprite
           and the width and height of the sprite. """
        # Create a new blank, transparent image with per pixel alphas
        image = pygame.Surface((width, height), flags = 1011001)
        image.fill((0,255,0,0))
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height) , special_flags = 0)
        return image
    
