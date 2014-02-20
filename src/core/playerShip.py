'''
Created on 20.1.2014

'''
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from core.spritesheet_functions import SpriteSheet

class playerShip(pygame.sprite.DirtySprite):
       
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
        
    def move(self, directions):
        '''
        move([bool,bool,bool,bool]) --> None
        
        if True -> rect.move():
        up,        ( 0,-1)     
        down,      ( 0, 1)
        left,      (-1, 0)
        right      ( 1, 0)
        '''
        up,down,left,right = directions
        print("direction of movement: {}".format(directions))
        # multiply by speed
        # If opposing directions are pressed, the ship doesn't move on that axis,
        # however, perpendicular directions are ok, the ship will move diagonally
        y = down*self.speed - up*self.speed
        x = right*self.speed - left*self.speed
        self.rect.move_ip(x,y)
    
    def update(self):
        
        # update animation frame
        if self.frame == 0:
            self.frame = 1
        elif self.frame == 1:
            self.frame = 0    
        
        # the propellers are in the same space, so they can be blitted over themselves without clearing    
        self.image.blit(self.propellersFrame[self.frame], (0,0))
        