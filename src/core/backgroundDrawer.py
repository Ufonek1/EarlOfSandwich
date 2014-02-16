'''

@author: DannyUfonek

this module keeps track of the background overlay over the solid background, and returns a surface for blitting
'''
import pygame
import random
from core.constants import *
from core.spritesheet_functions import SpriteSheet

class backgroundDrawer(object):
    bgSolid = None
    frame = 0
    #how many pixels to move per frame
    increment = 10
    maxFrames = None
    cloudRects = []
    allClouds = []
    
    def setBackground(self, backgroundName, backgroundOverlayName = "cloud", increment = 10):
        """
        createBackground(Surface, Surface) --> None
        loads the surfaces into the backgroundDrawer
        """
        #change increment if requested
        self.increment = increment
        #get image
        self.bgSolid = BACKGROUND_COLLECTION.__getattr__(backgroundName)
        
        if backgroundOverlayName == "cloud":
            #get clouds
            sprite_sheet = SpriteSheet(backgroundOverlayName)
            self.clouds = {}
            #get all four clouds (refer to file for dimensions)
            image = sprite_sheet.getImage(0, 0, 86, 178)
            self.clouds[image.get_size()] = image
            self.clouds[0] = image
            image = sprite_sheet.getImage(86, 0, 120, 110)
            self.clouds[image.get_size()] = image
            self.clouds[1] = image
            image = sprite_sheet.getImage(86, 110, 37, 31)
            self.clouds[image.get_size()] = image
            self.clouds[2] = image
            image = sprite_sheet.getImage(123, 110, 61, 36)
            self.clouds[image.get_size()] = image
            self.clouds[3] = image
            print(self.clouds)
                    
    def updateClouds(self):
        """
        cloud generator
        updateClouds() --> Surface
        """
        #prepare background for blitting the clouds onto
        full_background = self.bgSolid.copy()
        
        # should we generate a new cloud? 0-3 yes, 4-150 no -> balance if there's too many/too little clouds
        cloudNo = random.randint(0,150)
        if cloudNo <= 3 and len(self.cloudRects) < MAX_CLOUDS:
            newCloud = self.clouds[cloudNo]
            newRect = newCloud.get_rect()
            #move the rect for randomness and outside of screen
            newRect.move_ip(random.randint(-50,GAME_SCREEN_WIDTH),-178 - self.increment)
            self.cloudRects.append(newRect)
            print("created new cloud")
            print("number of clouds: {0}".format(len(self.cloudRects)))

        for rect in self.cloudRects:
            rectindex = self.cloudRects.index(rect)
            #move each cloud by increment
            rect.move_ip(0, self.increment)
            #get cloud which fits the rect's size and blit it onto the full_backgound surface
            full_background.blit(self.clouds[rect.size], (rect))
            self.cloudRects[rectindex] = rect
            if not rect.colliderect(full_background.get_rect()) and rect.y > GAME_SCREEN_HEIGHT:
                del self.cloudRects[rectindex]
                print("cloud deleted")
                print("number of clouds: {0}".format(len(self.cloudRects)))
        
        return full_background
'''        
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
'''       