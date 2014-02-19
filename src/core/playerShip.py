'''
Created on 20.1.2014

'''
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from core.spritesheet_functions import SpriteSheet

class playerShip(pygame.sprite.DirtySprite):
    
    #translating control names to directions
    directionsDict = {'MOVE_UP':(0,-1), 'MOVE_DOWN':(0,1), 'MOVE_LEFT':(-1,0), 'MOVE_RIGHT':(1,0)}
    
    speed = 15
    
    frame = 0
    
    propellersFrame = []
    
    def load(self, Image):
        
        propellers_sprite_sheet = SpriteSheet('propellers')
        
        picture = propellers_sprite_sheet.getImage(0, 0, 100, 100)
        self.propellersFrame.append(picture)
        picture = propellers_sprite_sheet.getImage(100, 0, 100, 100)
        self.propellersFrame.append(picture)
        
        self.frame = 0
        Image.blit(self.propellersFrame[0], (0,0))
        self.image = Image
        self.rect = self.image.get_rect()
        
    def move(self, direction):
        
        x,y = self.directionsDict[direction]
        # one of them equals 0, but that should be no problem
        x = x*self.speed
        y = y*self.speed
        
        self.rect.move_ip(x,y)
    
    def update(self):
        
        # update animation frame
        if self.frame == 0:
            self.frame = 1
        elif self.frame == 1:
            self.frame = 0    
        
        # the propellers are in the same space, so they can be blitted over themselves without clearing    
        self.image.blit(self.propellersFrame[self.frame], (0,0))
        