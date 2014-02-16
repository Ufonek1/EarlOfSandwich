'''

@author: DannyUfonek

this module keeps track of the background overlay over the solid background, and returns a surface for blitting
'''
import pygame
from core.constants import *

class backgroundDrawer(object):
    bgSolid = None
    bgOverlay = None
    frame = 0
    #how many pixels to move per frame
    increment = 10
    maxFrames = None
    
    def setBackground(self, background, backgroundOverlay, increment = 10):
        """
        createBackground(Surface, Surface) --> None
        loads the surfaces into the backgroundDrawer
        """
        self.bgSolid = background
        self.bgOverlay = backgroundOverlay
        #reset frame
        self.frame = 0
        self.increment = increment
        self.maxFrames = self.bgOverlay.get_height() // self.increment + GAME_SCREEN_HEIGHT // self.increment
    
    def updateBackground(self):
        """
        updateBackground() --> Surface
        """
        full_background = self.bgSolid.copy()
        #try:
        sourceX = 100
        # get the rectangle that is increment*frame + GAME_SCREEN_HEIGHT pixels from the bottom
        # so that the overlay moves upwards
        sourceY = self.bgOverlay.get_height() - self.frame*self.increment
        full_background.blit(self.bgOverlay,(0,0),(sourceX,sourceY,GAME_SCREEN_WIDTH,GAME_SCREEN_HEIGHT))
        # add frame
        if self.frame < self.maxFrames:
            self.frame += 1
        else:
            self.frame = 0
        return full_background
        #except:
        #    print("something's wrong with the background, returning blank background")
        #    return full_background
        