
#import os
#os.putenv('PYGAME_FREETYPE', "1")
import pygame
#import pygame.freetype
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from core.spritesheet_functions import SpriteSheet

class menuButton (pygame.sprite.DirtySprite):

    pygame.font.init()
    #the array into which we will load the sprite sheet
    button_frame = []
    
    #destination to which button leads
    destination = 0
    
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
        
        #set them up as the object's properties
        self.button_frame = button_frame
        self.destination = destination

    def update(self, event):
        if self.rect.collidepoint(mouse.get_pos()):
            if event.type == pl.MOUSEBUTTONDOWN:
                self.image = self.button_frame[3]
                print (str(self) + " was clicked")
                # this will point Main menu somewhere else (depends on the destination, ofc)
                if self.destination != 0:
                    return self.destination
            else:
                self.image = self.button_frame[1]
                #print ("cursor is on " + str(self))
                return
        else:
            self.image = self.button_frame[0]
            return 