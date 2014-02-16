'''

@author: DannyUfonek


this module should return sprites or sprite groups that are appropriate to the menu the user is in.
So that we don't have a separate module for every menu there is
'''
import pygame
from core.colourPicker import ColourPicker
from core.menuButton import menuButton
from core.constants import *

def getMenu(menuName):
    
    if menuName == "MAIN":
        """----------------------------------MAIN MENU-------------------------------"""
                
        #buttons tuple
        buttons = pygame.sprite.Group()
           
        #create all the buttons
        button1 = menuButton()
        button1.start("Play", "PLAY")
        button1.rect.x  = (BUTTON_COLUMN_LEFT)
        button1.rect.y = (BUTTON_COLUMN_TOP)
        button1.add(buttons)
        
        button2 = menuButton()
        button2.start("Options", "OPTIONS")
        button2.rect.x  = (BUTTON_COLUMN_LEFT)
        button2.rect.y = (BUTTON_COLUMN_TOP + 100)
        button2.add(buttons)
        
        button3 = menuButton()
        button3.start("Extras", "EXTRAS")
        button3.rect.x  = (BUTTON_COLUMN_LEFT)
        button3.rect.y = (BUTTON_COLUMN_TOP + 200)
        button3.add(buttons)
        
        button4 = menuButton()
        button4.start("Exit", "MAINQUIT")
        button4.rect.x  = (BUTTON_COLUMN_LEFT)
        button4.rect.y = (BUTTON_COLUMN_TOP + 300)
        button4.add(buttons)
        
        #add it to tuple
        tupleOfSprites = ((buttons),None)
        return tupleOfSprites
    
    elif menuName == "PLAY":
        """----------------------------------PREGAME MENU-------------------------------"""

        #buttons tuple
        buttons = pygame.sprite.Group()   
        
        #create all the buttons
        button1 = menuButton()
        button1.start("New Game", "NEW")
        button1.rect.x  = (BUTTON_COLUMN_LEFT)
        button1.rect.y = (BUTTON_COLUMN_TOP)
        button1.add(buttons)
        
        button2 = menuButton()
        button2.start("Load Game", "LOAD")
        button2.rect.x  = (BUTTON_COLUMN_LEFT)
        button2.rect.y = (BUTTON_COLUMN_TOP + 100)
        button2.add(buttons)

        button4 = menuButton()
        button4.start("Back to menu", "MAIN")
        button4.rect.x  = (BUTTON_COLUMN_LEFT)
        button4.rect.y = (BUTTON_COLUMN_TOP + 200)
        button4.add(buttons)
        
        #add it to tuple
        tupleOfSprites = ((buttons),None)
        return tupleOfSprites
    
    elif menuName == "OPTIONS":
        """----------------------------------OPTIONS MENU-------------------------------"""
        
        #buttons tuple
        buttons = pygame.sprite.Group()
        
        button4 = menuButton()
        button4.start("Back to menu", "MAIN")
        button4.rect.x  = (BUTTON_COLUMN_LEFT)
        button4.rect.y = (BUTTON_COLUMN_TOP + 300)
        button4.add(buttons)
        
        #add it to tuple
        tupleOfSprites = ((buttons),None)
        return tupleOfSprites
    
    elif menuName == "EXTRAS":
        """----------------------------------EXTRAS MENU-------------------------------"""
        
        #buttons tuple
        buttons = pygame.sprite.Group()
        
        button4 = menuButton()
        button4.start("Back to menu", "MAIN")
        button4.rect.x  = (BUTTON_COLUMN_LEFT)
        button4.rect.y = (BUTTON_COLUMN_TOP + 300)
        button4.add(buttons)
        
        #add it to tuple
        tupleOfSprites = ((buttons),None)
        return tupleOfSprites
    
    elif menuName == "LOAD":
        """----------------------------------LOAD CAMPAIGN MENU-------------------------------"""
        
        #buttons group
        buttons = pygame.sprite.Group()
        
        button4 = menuButton()
        button4.start("Back to menu", "MAIN")
        button4.rect.x  = (BUTTON_COLUMN_LEFT)
        button4.rect.y = (BUTTON_COLUMN_TOP + 300)
        button4.add(buttons)
        
        #add it to tuple
        tupleOfSprites = ((buttons),None)
        return tupleOfSprites
    
    elif menuName == "NEW":
        """----------------------------------NEW CAMPAIGN MENU-------------------------------"""
                        
        #buttons group
        buttons = pygame.sprite.Group()
        
        button1 = menuButton()
        button1.start("Start game!", "GAME")
        button1.rect.x  = (BUTTON_COLUMN_LEFT)
        button1.rect.y = (BUTTON_COLUMN_TOP + 300)
        button1.add(buttons)
        
        button3 = menuButton()
        button3.start("Save colour", "COLOUR", 0.5)
        button3.rect.x  = (BUTTON_COLUMN_LEFT + 30)
        button3.rect.y = (BUTTON_COLUMN_TOP + 230)
        button3.add(buttons)

        button4 = menuButton()
        button4.start("Back to menu", "MAIN")
        button4.rect.x  = (BUTTON_COLUMN_LEFT)
        button4.rect.y = (BUTTON_COLUMN_TOP + 400)
        button4.add(buttons)
        
        #create a colourpicker instance and draw it on the screen
        ColorPicker = ColourPicker()
        ColorPicker.rect.x = BUTTON_COLUMN_LEFT+300
        ColorPicker.rect.y = BUTTON_COLUMN_TOP
        
        #colour square:
        colourOutput = pygame.sprite.DirtySprite()
        colourOutput.image = pygame.Surface((50,50))
        colourOutput.image.fill(FULL_GREEN)
        colourOutput.rect = colourOutput.image.get_rect()
        colourOutput.rect.topleft = (BUTTON_COLUMN_LEFT+30, BUTTON_COLUMN_TOP+145)
        #colour on ship:
        shipColoured = pygame.sprite.DirtySprite()
        shipColoured.image = GAME_IMAGE_COLLECTION.skyship.copy()
        shipColoured.rect = shipColoured.image.get_rect()
        shipColoured.rect.topleft = (BUTTON_COLUMN_LEFT+100, BUTTON_COLUMN_TOP+100)
        print("the colourkey of shipColoured.image is " + str(shipColoured.image.get_colorkey()))
        #colour picker subtitle
        # load font
        title_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 30)
        #create the title as sprites with text as their source image
        colourPickerTitle = pygame.sprite.DirtySprite() 
        text1 = (title_font.render("Pick your colour:", True, FULL_RED))
        colourPickerTitle.image = text1
        colourPickerTitle.rect = colourPickerTitle.image.get_rect()
        colourPickerTitle._layer = 2
        colourPickerTitle.rect.x = BUTTON_COLUMN_LEFT
        colourPickerTitle.rect.y = BUTTON_COLUMN_TOP
        
        #add it to tuple
        tupleOfSprites = ((buttons), ColorPicker, colourOutput, shipColoured, colourPickerTitle)
        
        return tupleOfSprites 
    
    else:
        print("there is no valid menu for this destination")