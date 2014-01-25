'''

@author: DannyUfonek

'''

import sys
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
import pregameMenu
from core import mainMenu
from constants import *

pygame.init()

# start up the window
screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screensize.size) 
pygame.display.set_caption("Yet another pygame window")
print "window fired up"

#background
screen.blit(MENU_BACKGROUND, (0,0))
pygame.display.flip()

alive = True
# start main menu and wait for response, which gets saved

menuOutput = mainMenu.start(screen)
pygame.display.flip()
'''
now check the value and forward elsewhere
button destinations are self-explanatory
btw, they're set in mainMenu.start()

anyway, this has to be a loop, otherwise the player won't be able to go back and forth between menus
'''
while alive:
    if menuOutput == "QUIT":
        print ("game closed from MAIN MENU")
        alive = False
    elif menuOutput == "GAME":
        print ("Start game button was clicked")
        screen.blit(MENU_BACKGROUND, (0,0))
        pygame.display.flip()
        menuOutput = pregameMenu.start(screen)
    elif menuOutput == "OPTIONS":
        print ("Options button was clicked")
        break
    elif menuOutput == "EXTRAS":
        print ("Some other button was clicked")
        break
    elif menuOutput == "BACKTOMAIN":
        print ("The back to main menu button was clicked")
        print ("Returning to main menu")
        screen.blit(MENU_BACKGROUND, (0,0))
        pygame.display.flip()
        menuOutput = mainMenu.start(screen)
    else:
        print ("Somebody didn't specify the button destination or destination handling right")
        break


# when that is done, quit
print(" ")
print("Quitting, nothing left to do")
pygame.quit()
sys.exit()
 
        