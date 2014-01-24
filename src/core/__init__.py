'''

@author: DannyUfonek

'''

import sys
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core import mainMenu
from constants import *

pygame.init()

# start up the window
screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screensize.size) 
pygame.display.set_caption("Yet another pygame window")
print "window fired up"

gameBackground = pygame.sprite.GroupSingle()

#background
background = pygame.sprite.Sprite()
background.image = pygame.image.load(MAIN_MENU_BACKGROUND_PATH).convert_alpha()
background.rect = screensize
background.add(gameBackground)
gameBackground.draw(screen)
# start main menu and wait for response, which gets saved
menuOutput = mainMenu.start(screen)
'''
now check the value and forward elsewhere
button destinations are self-explanatory
btw, they're set in mainMenu.start()
'''
if menuOutput == "QUIT":
    print ("game closed from MAIN MENU")
elif menuOutput == "GAME":
    print ("Start game button was clicked")
elif menuOutput == "OPTIONS":
    print ("Options button was clicked")
elif menuOutput == "EXTRAS":
    print ("Some other button was clicked")
else:
    print ("Somebody didn't specify the button destination or destination handling right")


# when that is done, quit
print(" ")
print("Quitting, nothing left to do")
pygame.quit()
sys.exit()
 
        