'''

@author: DannyUfonek


this module should return sprites or sprite groups that are appropriate to the menu the user is in.
So that we don't have a separate module for every menu there is
'''
import pygame
from core.colourPicker import ColourPicker
from core.menuButton import menuButton, optionsButton
from core.constants import *

def getMenu(menuName, settings = None, shipSurface = None):
    
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
        """simply:
        create rows -> descr
        import current settings
        """
        #title group
        optionsTitles = pygame.sprite.Group()
        
        setting_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 25)
        title_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 30)
        big_title_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 50)
        #create the title as sprite with text as the source image
        smallTitle1 = pygame.sprite.DirtySprite() 
        text1 = (title_font.render("Movement:", True, FULL_RED))
        smallTitle1.image = text1
        smallTitle1.rect = smallTitle1.image.get_rect()
        smallTitle1._layer = 2
        smallTitle1.rect.x = BUTTON_COLUMN_LEFT
        smallTitle1.rect.y = BUTTON_COLUMN_TOP
        smallTitle1.add(optionsTitles)
        #create the title as sprite with text as the source image
        smallTitle2 = pygame.sprite.DirtySprite() 
        text2 = (title_font.render("Other:", True, FULL_RED))
        smallTitle2.image = text2
        smallTitle2.rect = smallTitle2.image.get_rect()
        smallTitle2._layer = 2
        smallTitle2.rect.x = BUTTON_COLUMN_LEFT + 300
        smallTitle2.rect.y = BUTTON_COLUMN_TOP
        smallTitle2.add(optionsTitles)
        #create the title as sprite with text as the source image
        bigTitle = pygame.sprite.DirtySprite() 
        text2 = (big_title_font.render("Options", True, FULL_RED))
        bigTitle.image = text2
        bigTitle.rect = bigTitle.image.get_rect()
        bigTitle._layer = 2
        bigTitle.rect.x = BUTTON_COLUMN_LEFT
        bigTitle.rect.y = BUTTON_COLUMN_TOP - 70
        bigTitle.add(optionsTitles)
        
        #buttons groups
        buttons = pygame.sprite.Group()
        optionButtons = pygame.sprite.Group()
        
        #shiparrows sprite for reference by setting buttons
        skyshiparrows = pygame.sprite.DirtySprite()
        skyshiparrows.image = GAME_IMAGE_COLLECTION.skyshipdirections
        skyshiparrows.rect = skyshiparrows.image.get_rect()
        skyshiparrows.rect.x = BUTTON_COLUMN_LEFT + 50
        skyshiparrows.rect.y = BUTTON_COLUMN_TOP + 80
        
        #setting buttons
        """Of course, these aren't exactly buttons, they're just text that behaves like a button"""
        '''DIRECTION BUTTONS'''
        '''UP'''
        control0 = optionsButton()
        control0.assignSetting(0)
        control0.image = settings.drawSetting(0)
        control0.rect = control0.image.get_rect()
        control0.rect.centerx = skyshiparrows.rect.centerx
        control0.rect.bottom = skyshiparrows.rect.top - 10
        control0.add(optionButtons)
        '''DOWN'''
        control1 = optionsButton()
        control1.assignSetting(1)
        control1.image = settings.drawSetting(1)
        control1.rect = control1.image.get_rect()
        control1.rect.centerx = skyshiparrows.rect.centerx
        control1.rect.top = skyshiparrows.rect.bottom + 10
        control1.add(optionButtons)
        '''LEFT'''
        control2 = optionsButton()
        control2.assignSetting(2)
        control2.image = settings.drawSetting(2)
        control2.rect = control2.image.get_rect()
        control2.rect.right = skyshiparrows.rect.left - 10
        control2.rect.centery = skyshiparrows.rect.centery
        control2.add(optionButtons)
        '''RIGHT'''
        control3 = optionsButton()
        control3.assignSetting(3)
        control3.image = settings.drawSetting(3)
        control3.rect = control3.image.get_rect()
        control3.rect.left = skyshiparrows.rect.right + 10
        control3.rect.centery = skyshiparrows.rect.centery
        control3.add(optionButtons)
        
        
        '''NON-DIRECTION TITLES'''
        titles = pygame.Surface((200,120), flags = 1011001)
        #fill with empty alpha
        titles.fill((0,255,0,0))
        #write options names onto the surface
        titles.blit(setting_font.render("Pause", True, FULL_RED), (0,0))
        titles.blit(setting_font.render("Attack", True, FULL_RED), (0,30))
        titles.blit(setting_font.render("Sound Volume", True, FULL_RED), (0,60))
        titles.blit(setting_font.render("Music Volume", True, FULL_RED), (0,90))
        settingTitles = pygame.sprite.DirtySprite()
        settingTitles.image = titles
        settingTitles.rect = settingTitles.image.get_rect()
        settingTitles.rect.x = BUTTON_COLUMN_LEFT + 270
        settingTitles.rect.y = BUTTON_COLUMN_TOP + 50
        settingTitles.add(optionsTitles)
        
        '''NON-DIRECTION BUTTONS'''
        '''PAUSE'''
        control4 = optionsButton()
        control4.assignSetting(4)
        control4.image = settings.drawSetting(4)
        control4.rect = control4.image.get_rect()
        control4.rect.left = settingTitles.rect.right + 10
        control4.rect.y = BUTTON_COLUMN_TOP + 50
        control4.add(optionButtons)
        '''ATTACK'''
        control5 = optionsButton()
        control5.assignSetting(5)
        control5.image = settings.drawSetting(5)
        control5.rect = control5.image.get_rect()
        control5.rect.left = settingTitles.rect.right + 10
        control5.rect.y = BUTTON_COLUMN_TOP + 80
        control5.add(optionButtons)
        '''MUSIC VOLUME'''
        control6 = optionsButton()
        control6.assignSetting(6)
        control6.image = settings.drawSetting(6)
        control6.rect = control6.image.get_rect()
        control6.rect.left = settingTitles.rect.right + 10
        control6.rect.y = BUTTON_COLUMN_TOP + 110
        control6.add(optionButtons)
        '''SOUND VOLUME'''
        control7 = optionsButton()
        control7.assignSetting(7)
        control7.image = settings.drawSetting(7)
        control7.rect = control7.image.get_rect()
        control7.rect.left = settingTitles.rect.right + 10
        control7.rect.y = BUTTON_COLUMN_TOP + 140
        control7.add(optionButtons)
        
        #classic button
        button4 = menuButton()
        button4.start("Back to menu", "MAIN")
        button4.rect.x = (BUTTON_COLUMN_LEFT)
        button4.rect.y = (BUTTON_COLUMN_TOP + 300)
        button4.add(buttons)
        

        
        #add it all to a tuple
        tupleOfSprites = ((buttons),(optionButtons),(optionsTitles),skyshiparrows)
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