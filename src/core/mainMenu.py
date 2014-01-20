'''

@author: DannyUfonek

this package should deal with the main menu -> load, create, and do anything that is required
'''
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from menuButton import menuButton

    
def start():
    
    buttons = pygame.sprite.Group()
    pygame.init()
    
    screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screensize.size) 
    pygame.display.set_caption("Yet another pygame window")

    
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill(BLACK)
    screen.blit(background, (0,0))

    clock = pygame.time.Clock()

    #create all the buttons
    button1 = menuButton()
    button1.__init__
    button1.rect.x  = (100)
    button1.rect.y = (300)
    button1.add(buttons)
    
    button2 = menuButton()
    button2.__init__
    button2.rect.x  = (100)
    button2.rect.y = (200)
    button2.add(buttons)
    
    button3 = menuButton()
    button3.__init__
    button3.rect.x  = (150)
    button3.rect.y = (100)
    button3.add(buttons)
    
    buttons.draw(screen)
    pygame.display.flip()
    
    print ("buttons created and drawn on screen")
    

    # Draw all the spites
    # Go ahead and update the screen with what we've drawn.
   # pygame.display.flip()

        
    #screen.blit(background, (0,0))
    menuRunning = True
    
    while menuRunning:
        for event in pygame.event.get():
            print ("something happened")
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("quitting")
                menuRunning = False
            if event.type == pl.MOUSEBUTTONDOWN:
                buttons.update(event)
                buttons.draw(screen)
                pygame.display.flip()
            if event.type == pl.MOUSEMOTION:
                #screen.blit(background2, (0,0))
                buttons.update(event)
                buttons.draw(screen)
                pygame.display.flip()
        clock.tick(30)
        #we update twice, so that the button doesn't freeze after pressing           
        buttons.update(event)
        buttons.draw(screen)
        pygame.display.flip()
'''      
def updateButtons(event, screen):
    """Method for updating buttons externally"""
    buttons.update(event)
    buttons.draw(screen)
#    pygame.display.flip()
        
def closeMenu():
    """This method is to clear memory"""
    buttons.clear(MENU_BACKGROUND, MENU_BACKGROUND)
    buttons.empty()
    print("main menu closed")
    pygame.display.flip()
    return
'''
