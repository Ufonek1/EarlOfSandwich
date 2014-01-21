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

background = pygame.Surface(screensize.size)
background.fill(BLACK)
screen.blit(background, (0,0))

# start main menu
mainMenu.start(screen)

# when that is done, quit
print("Quitting")
pygame.quit()
sys.exit()
 
        