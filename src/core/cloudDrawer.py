'''

@author: DannyUfonek
'''

import pygame
import random
from core.constants import *
from core.spritesheet_functions import SpriteSheet

print("loading cloud drawer")

class cloudDrawer(object):

    #how many pixels to move per frame
    increment = 1
    cloudsImages = []
    allClouds = []
    
    def load(self, backgroundOverlayName = "cloud", increment = 1):
        """
        createBackground(Surface, Surface) --> None
        loads the surfaces into the backgroundDrawer
        """
        #create fresh list
        self.allClouds = []
        #change increment if requested
        self.increment = increment
        #set backgroundoverlay
        self.backgroundOverlayName = backgroundOverlayName
        
        if backgroundOverlayName == "cloud":
            #get clouds from file
            sprite_sheet = SpriteSheet(backgroundOverlayName)
            cloudsImages = []

            image = sprite_sheet.getImage(0, 0, 86, 178)
            cloudsImages.append(image)
            
            image = sprite_sheet.getImage(86, 0, 120, 110)
            cloudsImages.append(image)
            
            image = sprite_sheet.getImage(86, 110, 37, 31)
            cloudsImages.append(image)
            
            image = sprite_sheet.getImage(123, 110, 61, 36)
            cloudsImages.append(image)
            
            image = sprite_sheet.getImage(184, 110, 15, 35)
            cloudsImages.append(image)
            print("clouds spritesheet loaded successfully")
            
            self.cloudsImages = cloudsImages

    def update(self, allSprites):
        """
        cloud updater
        updateClouds() --> [DirtySprite, DirtySprite, ...], [Rect, Rect, ...]
        """

        # should we generate a new cloud? 0-9 yes, 11 - 250 no -> balance if there's too many/too little clouds
        cloudNumber = random.randint(0,250)
        if cloudNumber <= 9 and len(self.allClouds) < MAX_CLOUDS:
            #by this we increase probability of small clouds: 0,1 = big clouds; 2,5,8 = small cloud 1 ; 3,6,9 = small cloud 2; 4,7 = tiny cloud 
            while cloudNumber > 4:
                cloudNumber = cloudNumber - 3
            #create new cloud
            self.allClouds.append(Cloud(cloudNumber, self.cloudsImages[cloudNumber]))
            # move to random place above game screen
            self.allClouds[-1].rect.move_ip(random.randint(GAME_SCREEN_RECT.left-50,GAME_SCREEN_RECT.left+GAME_SCREEN_RECT.width),GAME_SCREEN_RECT.top - self.allClouds[-1].rect.height - self.increment)
            #add to cloud list
            allSprites.add(self.allClouds[-1], layer = 1)

            print("created new cloud")
            print("number of clouds: {0}".format(len(self.allClouds)))
        
        #prepare returning stuff
        oldrectlist = []
        newrectlist = []
        
        for cloud in self.allClouds:
            #chop off places that are outside the game screen
            oldrect = cloud.rect.clip(GAME_SCREEN_RECT)
            #save old rect for later display updating
            oldrectlist.append(oldrect)
            
            #move cloud rect by increment
            cloud.move(self.increment)
            
            #chop off places that are outside the game screen
            newrect = cloud.rect.clip(GAME_SCREEN_RECT)
            #save old rect for later display updating
            newrectlist.append(newrect)
            
            #is the cloud outside the game screen? If so, delete it
            if not cloud.rect.colliderect(GAME_SCREEN_RECT) and cloud.rect.y > GAME_SCREEN_RECT.top + GAME_SCREEN_RECT.height:
                cloud.kill()
                del self.allClouds[self.allClouds.index(cloud)]
                print("cloud deleted")
                print("number of clouds: {0}".format(len(self.allClouds)))

        return self.allClouds, oldrectlist, newrectlist
            
class Cloud(pygame.sprite.DirtySprite):
    # which size is the cloud? (see sprite sheet
    type = 0
    
    def __init__(self, typeNumber, image, *groups):
        #assign cloud properties
        self.type = typeNumber
        self.image = image
        self.rect = self.image.get_rect()
        pygame.sprite.DirtySprite.__init__(self, *groups)

    def move(self,increment):
        x = 0
        y = 1
        x = x * increment
        y = y * increment
        self.rect.move_ip(x,y)
    