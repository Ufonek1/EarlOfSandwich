'''
Created on 20.1.2014

'''
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from core.spritesheet_functions import SpriteSheet

class playerShip(pygame.sprite.DirtySprite):
       
    speed = 10
    
    frame = 0
    
    propellersFrame = []
    
    def load(self, Image):
        
        propellers_sprite_sheet = SpriteSheet('propellers')
        # load propellers spritesheet
        picture = propellers_sprite_sheet.getImage(0, 0, 100, 100)
        self.propellersFrame.append(picture)
        picture = propellers_sprite_sheet.getImage(100, 0, 100, 100)
        self.propellersFrame.append(picture)
        
        #set the starting frame
        self.frame = 0
        # blit that frame onto self.image
        Image.blit(self.propellersFrame[0], (0,0))
        self.image = Image
        #return rects and stuff
        self.rect = self.image.get_rect()
        
    def move(self, directions):
        '''
        move([bool,bool,bool,bool], Surface) --> bool, Rect
        
        if True -> rect.move():
        up,        ( 0,-1)     
        down,      ( 0, 1)
        left,      (-1, 0)
        right      ( 1, 0)
        '''
        #save old rect for display updating
        oldrect = self.rect.copy()
        
        up,down,left,right = directions
        # If opposing directions are pressed, the ship doesn't move on that axis,
        # however, perpendicular directions are ok, the ship will move diagonally
        # calculate directions
        x = (right - left)*self.speed
        y = (down - up)*self.speed
        # exit to save resources if we don't move
        if x == 0 and y == 0:
            return False, oldrect, self.rect
        else:
            self.rect.move_ip(x,y)
            self.rect = self.rect.clamp(PLAYABLE_RECT)
            newrect = self.rect.copy()
            #inflate, but clamp
            newrect.inflate_ip(self.speed*2, self.speed*2)
            newrect.clamp_ip(PLAYABLE_RECT)
            return True, oldrect, newrect

    def update(self):
        
        # update animation frame
        if self.frame == 0:
            self.frame = 1
        elif self.frame == 1:
            self.frame = 0    
        
        # the propellers are in the same space, so they can be blitted over themselves without clearing    
        self.image.blit(self.propellersFrame[self.frame], (0,0))
        