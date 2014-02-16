'''
The true core of the game. This module will take care of the game itself, as the name suggests.

@author: DannyUfonek
'''
import pygame
import pygame.locals as pl
import core.levelCreator as levelCreator
from core.constants import *

def start(screen, shipSurface, userSave):
    
    #set keys to repeat
    pygame.key.set_repeat(100,100)
    print("starting game, getting level")
    levelCreator.getLevel(0)
    
  
    