'''

@author: DannyUfonek

'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
import core.mainMenu as mainMenu
from constants import *

pygame.init()

screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screensize.size) 
pygame.display.set_caption("Yet another pygame window")

background = pygame.Surface(screensize.size)
background.fill(BLACK)
screen.blit(background, (0,0))

clock = pygame.time.Clock()

mainMenu.start()
mainMenu.buttons.draw(screen)
pygame.display.flip()
print ("written on screen")

alive = True

while alive:
    for event in pygame.event.get():
        if event.type == pl.QUIT:
            print("quitting")
            alive = False
        if event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE:
            print("quitting")
            alive = False
        if event.type == pl.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            mainMenu.updateButtons(event, screen)
            pygame.display.flip()
        if event.type == pl.MOUSEMOTION:
            mainMenu.updateButtons(event, screen)
            pygame.display.flip()
    clock.tick(30)
    """Update the buttons anyway, so that they don't freeze after clicking"""
    mainMenu.updateButtons(event, screen)
    pygame.display.flip()
#mainMenu.closeMenu()
print("Quitting")
pygame.quit()

    
        