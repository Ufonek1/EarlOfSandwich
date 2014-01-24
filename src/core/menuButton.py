'''

@author: DannyUfonek
'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from core.spritesheet_functions import SpriteSheet

class menuButton (pygame.sprite.DirtySprite):

    pygame.font.init()
    #the array into which we will load the sprite sheet
    button_frame = []
    
    #destination to which button leads
    destination = ""
    
    # font of buttons
    button_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 35)
    '''@TODO figure out a way how to be able to change the button's text from the outside'''   
    def start(self, text, destination):
        pygame.sprite.Sprite.__init__(self)
        #create the spritesheet
        sprite_sheet = SpriteSheet(BUTTON_SPRITESHEET_PATH)
       
        button_frame = []
        #load all appropriate images and write text over them
        image = sprite_sheet.getImage(0, 0, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (49,7))
        button_frame.append(image)
        image = sprite_sheet.getImage(0, 68, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (49,7))
        button_frame.append(image)
        image = sprite_sheet.getImage(0, 136, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (49,7))
        button_frame.append(image)
        image = sprite_sheet.getImage(0, 204, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (56,14))
        button_frame.append(image)
        
        #set starting image
        self.image = button_frame[0]
        
        #reference to image rect
        self.rect = self.image.get_rect()
        
        #set them up as the button's properties (so that they don't stay stucked in the function only)
        self.button_frame = button_frame
        self.destination = destination
        print ("created menuButton with destination " + str(self.destination))

    def update(self, event):
        if self.rect.collidepoint(mouse.get_pos()):
            if event.type == pl.MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                self.image = self.button_frame[3]
                # this will point Main menu somewhere else (depends on the destination, ofc)
                #if self.destination != 0:
                #   print ("returning self.destination")
                #   return self.destination
            else:
                self.image = self.button_frame[1]
                #print ("cursor is on " + str(self))
        else:
            self.image = self.button_frame[0]
            
    def getMouseOver(self):
        #simple method for getting is the mouse is on the button
        if self.rect.collidepoint(mouse.get_pos()):
            return True
        else:
            return False
        

