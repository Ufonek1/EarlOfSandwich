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
    
    def setBackground(self, background, backgroundOverlayName = "cloud", increment = 10):
        """
        createBackground(Surface, Surface) --> None
        loads the surfaces into the backgroundDrawer
        """
        #change increment if requested
        self.increment = increment
        #get image
        self.bgSolid = background
        
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
            image = sprite_sheet.getImage(184, 110, 15, 35)
            self.clouds[image.get_size()] = image
            self.clouds[4] = image
            print("everything loadeed")
                    
    def updateClouds(self):
        """
        cloud generator
        updateClouds() --> Surface
        """
        #prepare background for blitting the clouds onto
        cloud_background = pygame.Surface((GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT), flags = 1011001)
        cloud_background.fill((0,255,0,0))
        #prepare rectlist for display updating
        rectlist = []
        # should we generate a new cloud? 0-9 yes, 11 - 250 no -> balance if there's too many/too little clouds
        cloudNo = random.randint(0,250)
        if cloudNo <= 9 and len(self.cloudRects) < MAX_CLOUDS:
            #by this we increase probability of small clouds: 0,1 = big clouds; 2,5,8 = small cloud 1 ; 3,6,9 = small cloud 2; 4,7 = tiny cloud 
            while cloudNo > 4:
                cloudNo = cloudNo - 3
            #get appropriate rect
            newCloud = self.clouds[cloudNo]
            newRect = newCloud.get_rect()
            #move the rect for randomness and outside of screen
            newRect.move_ip(random.randint(GAME_SCREEN_LEFT-50,GAME_SCREEN_LEFT+GAME_SCREEN_WIDTH),GAME_SCREEN_TOP-178 - self.increment)
            print(newRect)
            self.cloudRects.append(newRect)
            print("created new cloud")
            print("number of clouds: {0}".format(len(self.cloudRects)))

        for rect in self.cloudRects:
            rectindex = self.cloudRects.index(rect)
            #move each cloud rect by increment
            rect.move_ip(0, self.increment)
            #get cloud which fits the rect's size and blit it onto the full_backgound surface, but reduce it first
            zeroedrect = rect.move(-GAME_SCREEN_LEFT,-GAME_SCREEN_TOP)
            cloud_background.blit(self.clouds[rect.size], (zeroedrect))
            self.cloudRects[rectindex] = rect
            if not rect.colliderect(cloud_background.get_rect().move(GAME_SCREEN_RECT.topleft)) and rect.y > GAME_SCREEN_TOP + GAME_SCREEN_HEIGHT:
                del self.cloudRects[rectindex]
                print("cloud deleted")
                print("number of clouds: {0}".format(len(self.cloudRects)))
            rectlist.append(rect.inflate(0,2))
        
        return cloud_background, rectlist
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