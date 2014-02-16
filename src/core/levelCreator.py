'''

@author: DannyUfonek

This module works similar to menuCreator - it returns sprites according to what you ask of it,
however, levels are read from external files and translated for the game's use.
Think of this as a dictionary with which the game.__init__ module interprets levels saved
in external files.
'''

import pygame
import os
from core.constants import *

def getLevel(levelNumber):
    """
    getLevel(int) --> [pygame.sprite.Group, ...], pygame.sprite.Surface, pygame.sprite.Surface
    getLevel(levelNumber) --> enemies, background, backgroundOverlay
    """
    print("getting level " + str(levelNumber))
    
    #locate level file
    levelPath = os.path.join(LEVELS_PATH, ('level' + str(levelNumber)))
    enemies = []
    # enemies = [wave[enemy, enemy, enemy, ...], wave[enemy, enemy, enemy, ...], wave[enemy, enemy, enemy, ...], ...]
    with open(levelPath, newline=None) as source:
        #transform file into list
        lines = []
        for line in source:
            line = line.partition('\n')[0]
            lines.append(line)
        print(lines)
        #find start and end of enemy block - read the lines within
        for line in lines[lines.index("*enemy")+1:lines.index("*", lines.index("*enemy"))]:
            #load enemies into full array
            thiswave = line.strip().split(",")
            enemies.append(thiswave)
        #get background stuff
        background = lines[lines.index("*background")+1]
        backgroundOverlay = lines[lines.index("*background")+2]
        print("loaded level {0} from file, which is the following:".format(levelNumber))
        print(enemies, background, backgroundOverlay)
    #now get the appropriate background images
    background = BACKGROUND_COLLECTION.__getattr__(background)
    #backgroundOverlay = BACKGROUND_COLLECTION.__getattr__(backgroundOverlay)
    
    return enemies, background, backgroundOverlay
                