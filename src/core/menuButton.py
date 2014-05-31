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

    def __init__(self, text, destination, relativescale = 1):
        #create the spritesheet
        sprite_sheet = SpriteSheet(BUTTON_SPRITESHEET_NAME)
       
        button_frame = []
        '''
        load all appropriate images and write text over them
        
        basic recipe:
        1. find and load the desired area of the spritesheet and make any pixels of the colorkey transparent
        2. render text over that
        3. apply any scaling, if there is any (multiply by that scaling, round the result, and make it into an int)
        4. append to main frame array
        '''
        image = sprite_sheet.getImage(0, 0, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (49,7))
        image = pygame.transform.scale(image, (int(round(450*relativescale)), int(round(68*relativescale))))
        button_frame.append(image)
        
        image = sprite_sheet.getImage(0, 68, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (49,7))
        image = pygame.transform.scale(image, (int(round(450*relativescale)), int(round(68*relativescale))))
        button_frame.append(image)
        
        image = sprite_sheet.getImage(0, 136, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (49,7))
        image = pygame.transform.scale(image, (int(round(450*relativescale)), int(round(68*relativescale))))
        button_frame.append(image)
        
        image = sprite_sheet.getImage(0, 204, 450, 68)
        image.blit(self.button_font.render(text, True, FULL_RED), (56,14))
        image = pygame.transform.scale(image, (int(round(450*relativescale)), int(round(68*relativescale))))
        button_frame.append(image)
        
        #set starting image
        self.image = button_frame[0]
        
        #reference to image rect
        self.rect = self.image.get_rect()
        
        #set them up as the button's properties (so that they don't stay stucked in the function only)
        self.button_frame = button_frame
        self.destination = destination
        
        pygame.sprite.DirtySprite.__init__(self)
        print ("created menuButton with destination " + str(self.destination))
        

    def update(self, event):
        MouseOver = self.getMouseOver()
        if MouseOver == True:
            if event.type == pl.MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                self.image = self.button_frame[3]
            else:
                self.image = self.button_frame[1]
        else:
            self.image = self.button_frame[0]
        
        return MouseOver
            
    def getMouseOver(self):
        #simple method for getting if the mouse is on the button (for outside/public use)
        if self.rect.collidepoint(mouse.get_pos()):
            return True
        else:
            return False
        

class optionsButton (pygame.sprite.DirtySprite):
    
    #this is for the tipField
    destination = -1
    setting = None
    
    def assignSetting(self, settingbind):
        self.setting = settingbind
    
    #duplicate method to allow other buttons to update
    def update(self, event):
        MouseOver = self.getMouseOver()       
        return MouseOver
    
    def getMouseOver(self):
        #simple method for getting if the mouse is on the button (for outside/public use)
        if self.rect.collidepoint(mouse.get_pos()):
            return True
        else:
            return False
    