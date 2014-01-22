
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
    # text of button and its font
    button_id = 0
    
    button_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 35)
    text = "placeholder"
    '''@TODO figure out a way how to be able to change the button's text from the outside'''   
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #create the spritesheet
        sprite_sheet = SpriteSheet(BUTTON_SPRITESHEET_PATH)
       
        #load all appropriate images and write text over them
        image = sprite_sheet.getImage(0, 0, 450, 68)
        image.blit(self.button_font.render(self.text, True, FULL_RED), (49,7))
        self.button_frame.append(image)
        image = sprite_sheet.getImage(0, 68, 450, 68)
        image.blit(self.button_font.render(self.text, True, FULL_RED), (49,7))
        self.button_frame.append(image)
        image = sprite_sheet.getImage(0, 136, 450, 68)
        image.blit(self.button_font.render(self.text, True, FULL_RED), (49,7))
        self.button_frame.append(image)
        image = sprite_sheet.getImage(0, 204, 450, 68)
        image.blit(self.button_font.render(self.text, True, FULL_RED), (56,14))
        self.button_frame.append(image)
        
        #set starting image
        self.image = self.button_frame[0]
        
        #reference to image rect
        self.rect = self.image.get_rect()
        

    def update(self, event):
        if self.rect.collidepoint(mouse.get_pos()):
            if event.type == pl.MOUSEBUTTONDOWN:
                self.image = self.button_frame[3]
                print (str(self) + " was clicked")
                return
            else:
                self.image = self.button_frame[1]
                #print ("cursor is on " + str(self))
                return
        else:
            self.image = self.button_frame[0]
            return 