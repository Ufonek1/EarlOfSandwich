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
    #for now, only an empty sprite, but weapon cooldowns and hp and so on should go here probably
    
    def load(self, Image):
        self.image = Image
        self.rect = self.image.get_rect()
        
    def move(self, direction):
        
        x,y = self.directionsDict[direction]
        # one of them equals 0, but that should be no problem
        x = x*self.speed
        y = y*self.speed
        
        self.rect.move_ip(x,y)