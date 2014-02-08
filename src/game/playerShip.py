'''
Created on 20.1.2014

'''
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from core.spritesheet_functions import SpriteSheet

class playerShip(pygame.sprite.Sprite):
    
    #ship spritesheet array  
    ship_frame = []
    
    def init(self):
        pygame.sprite.Sprite.__init__(self)
        #create the spritesheet
        sprite_sheet = SpriteSheet(BUTTON_SPRITESHEET_PATH)
       
        """TODO - draw the ship spritesheet and image loads"""
        '''
        #load all appropriate images
        image = sprite_sheet.getImage(0, 0, 450, 68)
        self.button_frame.append(image)
        image = sprite_sheet.getImage(0, 68, 450, 68)
        self.button_frame.append(image)
        image = sprite_sheet.getImage(0, 136, 450, 68)
        self.button_frame.append(image)
        image = sprite_sheet.getImage(0, 204, 450, 68)
        self.button_frame.append(image)
        '''
        #set starting image
        self.image = self.button_frame[0]
        
        #reference to image rect
        self.rect = self.image.get_rect()
        
    def update(self):
        """TODO"""