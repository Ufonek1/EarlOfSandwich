'''
Created on 17.1.2014

@author: Hynek
'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from constants import *
from menuButton import menuButton

pygame.init()

#initialize window
screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screensize.size) 
pygame.display.set_caption("Yet another pygame window")

#with background
background = pygame.Surface(screensize.size)
background.fill(BLACK)
screen.blit(background, (0,0))


clock = pygame.time.Clock()

#button class


# now let's define the button states -> the change in frames

running = True
buttons = pygame.sprite.Group()

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
# Draw all the spites
# Go ahead and update the screen with what we've drawn.
pygame.display.flip()
# --- Limit to 20 frames per second


#screen.blit(background, (0,0))
while running:
    for event in pygame.event.get():
        if event.type == pl.QUIT:
            running = False
        if event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE:
            running = False
        if event.type == pl.MOUSEBUTTONDOWN or event.type == pl.MOUSEMOTION:
            #screen.blit(background2, (0,0))
            buttons.update(event)
            buttons.draw(screen)
            pygame.display.flip()
    clock.tick(30)
    """ we update twice, so that the button doesn't freeze after pressing """
    buttons.update(event)
    buttons.draw(screen)
    pygame.display.flip()
    
pygame.display.quit()

    
    
        