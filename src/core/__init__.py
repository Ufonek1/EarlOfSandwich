'''

@author: DannyUfonek

'''

import sys
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core import pregameMenu
from core import mainMenu
from core.constants import *

pygame.init()

# start up the window
screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screensize.size) 
pygame.display.set_caption("Yet another pygame window")
print("window fired up")

#background from background collection
screen.blit(MENU_BACKGROUND, (0,0))
pygame.display.flip()

#Create bottom tip field
def tipFieldInit():
    x = pygame.Surface(TIP_FIELD_RECT.size)
    x.fill(WHITE)
    return x
tipField = tipFieldInit()
screen.blit(tipField, (TIP_FIELD_RECT))

alive = True
# start main menu and wait for response, which gets saved

menuOutput = mainMenu.start(screen, tipField)
pygame.display.flip()
'''
now check the value and forward elsewhere
button destinations are self-explanatory
btw, they're set in mainMenu.start()

anyway, this has to be a loop, otherwise the player won't be able to go back and forth between menus

redrawing of the background shouldn't be here, as each module cleans up after itself,
because that's what their parents taught them! 
(well, mostly)
'''
while alive:
    if "QUIT" in menuOutput:
        '''
        the middle bit is ripped from menuOutput to see from where it was
        menuOutput is always in the form of "<something>QUIT"
        yay! now i can use all that string indexing!
        '''
        print ("game closed from " + menuOutput[:menuOutput.find("QUIT")] + " MENU")
        alive = False
    elif menuOutput == "GAME":
        print ("Start game button was clicked")
        menuOutput = pregameMenu.start(screen, tipField)
    elif menuOutput == "OPTIONS":
        print ("Options button was clicked")
        break
    elif menuOutput == "EXTRAS":
        print ("Some other button was clicked")
        break
    elif menuOutput == "BACKTOMAIN":
        print ("The back to main menu button was clicked")
        print ("Returning to main menu")
        menuOutput = mainMenu.start(screen, tipField)
    else:
        print ("Button destination or its recognition unspecified")
        break


# when that is done, quit
print(" ")
print("Quitting, nothing left to do")
pygame.quit()
sys.exit()
 
        