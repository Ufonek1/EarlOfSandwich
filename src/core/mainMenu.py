'''

@author: DannyUfonek

this package should deal with the main menu -> load, create, and do anything that is required
'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from menuButton import menuButton

buttons = pygame.sprite.Group()
buttonLabels = pygame.sprite.Group()
allSprites = pygame.sprite.LayeredUpdates(layer = 5)

def start(screen):
    
    pygame.init()
    
    #for fps control
    clock = GAME_CLOCK
       
    #create all the buttons
    button1 = menuButton()
    button1.button_id = 1
    button1.text = "I like peanuts"
    button1.__init__()
    button1.rect.x  = (100)
    button1.rect.y = (300)
    button1.add(buttons)
    button1.add(allSprites)
    #allSprites.add(button1, 0)
    
    button2 = menuButton()
    button2.button_id = 2
    button2.text = "I like blackberries"
    button2.__init__()
    button2.rect.x  = (100)
    button2.rect.y = (200)
    button2.add(buttons)
    button2.add(allSprites)
    #allSprites.add(button2, 0)
    
    button3 = menuButton()
    button3.button_id = 3
    button3.text = "I like tea"
    button3.__init__()
    button3.rect.x  = (100)
    button3.rect.y = (100)
    button3.add(buttons)
    button3.add(allSprites)
    
    #add buttons to bottom layer
    allSprites.add(buttons, layer = 0)

    # draw them on screen and update
    #buttons.draw(screen)
    
    # load font for labels
    button_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 72)
    
    #create the labels as sprites with text as their source image
    label1 = pygame.sprite.DirtySprite() 
    text1 = (button_font.render("Goodbye", True, FULL_RED))
    label1.image = text1
    label1.rect = label1.image.get_rect()
    label1.rect.x = 100
    label1.rect.y = 10
    #label1.add(buttonLabels)
    label1.add(allSprites)
    
    #draw sprites
    allSprites.change_layer(label1, 1)
    allSprites.move_to_front(label1)
    print allSprites.get_top_layer()
    print allSprites.get_bottom_layer()
    allSprites.draw(screen)
    #buttonLabels.draw(screen)    
    #screen.blit(button_font.render("Is this ok?", True, FULL_RED), (100,190))
    pygame.display.flip()
    
    print ("sprites created and drawn on screen")
    
    
    # Main Menu event loop
    menuRunning = True
    
    while menuRunning:
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("quitting")
                menuRunning = False
            if event.type == pl.MOUSEBUTTONDOWN:
                buttons.update(event)
                allSprites.draw(screen)
                pygame.display.flip()
            if event.type == pl.MOUSEMOTION:
                buttons.update(event)
                allSprites.draw(screen)
                pygame.display.flip()
        clock.tick(30)
        #we update twice, so that the button doesn't freeze after pressing           
        buttons.update(event)
        allSprites.draw(screen)
        pygame.display.flip()
    
''' 
def updateButtons(event, screen):
    """Method for updating buttons externally"""
    buttons.update(event)
    buttons.draw(screen)
#    pygame.display.flip()
'''        

