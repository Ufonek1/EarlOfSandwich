'''

@author: DannyUfonek
'''
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *

class ColourPicker(pygame.sprite.DirtySprite):
    
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
    
def setColour(colourDesired = FULL_GREEN, colourToChange = FULL_GREEN, entryImage = GAME_IMAGE_COLLECTION.skyshipns.copy()):
    '''setColour(pygame.Color, pygame.Color, Surface) -> Surface 
    defaults to green
    1. make entry image into PixelArray (with converting it first)
    2. replace the pixels of colour colourToChange to the colour colourDesired
    3. make the PixelArray into a Surface
    4. blit shadows onto this surface
    5. return the surface
    '''
    sourceShipPixels = pygame.PixelArray(entryImage.convert_alpha())
    sourceShipPixels.replace(colourToChange, colourDesired)
    print("The colour " + str(colourToChange) + " was replaced with " + str(colourDesired))
    outImage = sourceShipPixels.make_surface()
    outImage.blit(GAME_IMAGE_COLLECTION.skyshipshadows, (0,0))
    #outImage.set_colorkey(FULL_MAGENTA)
    return outImage
    
