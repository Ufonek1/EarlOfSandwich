'''

@author: DannyUfonek
'''
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from constants import *

class ColourPicker (pygame.sprite.DirtySprite):
    
    #load spectrum.png
    spectrum = GAME_IMAGE_COLLECTION.spectrum
    #pixelArray to grab pixels out of
    pixels = pygame.PixelArray(spectrum)
    #normal sprite attributes
    image = spectrum.copy()
    rect = image.get_rect()

    def getMouseOver(self):
        if self.rect.collidepoint(mouse.get_pos()):
            return True
        else:
            return False
        
    def pickColour(self):
        '''
        This: 
        gets the mouse position
        pos is the colourPicker position in relation to the screen,
        so that we can access pixels which are actually there
        finds the pixel that is on that position
        unmaps the pixel into a pygame.Color object
        and returns its colour
        '''
        posx = self.rect.x
        posy = self.rect.y
        x, y = mouse.get_pos()
        print("looking for pixel of index " + str(x-posx) + ", " + str(y - posy))
        colourPicked = self.image.unmap_rgb(self.pixels[x - posx, y - posy])
        print("returning colour " + str(colourPicked))
        return colourPicked
    
    def saveColour(self, entryImage, colourToChange, colourDesired):
        '''
        UNUSED YET
        This is a converter of surface pixels of a given colour to a different colour
        the return value is a surface with its pixels changed to the desired colour
        '''
        someotherpixels = pygame.PixelArray(entryImage)
        someotherpixels.replace(colourToChange, colourDesired)
        outputImage = someotherpixels.make_surface()
        return outputImage
    
    