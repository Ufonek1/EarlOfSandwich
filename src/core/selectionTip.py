'''

@author: DannyUfonek

this module stores all the different tooltips, and when asked for tips on buttons, it returns a surface 
to be drawn on screen.
'''
import pygame
import core
from core.constants import *

'''
load the description dictionary
'''
tipDict = {}
with open(TIPDICT_PATH) as source:
    for line in source:
        #load the key and value from each line (strip is there to just take the text)
        (key, val) = line.strip().split(";")
        tipDict[key] = val
tipFont = pygame.font.Font(MAIN_MENU_FONT_PATH, 30)

class tipField(pygame.sprite.DirtySprite):
    
    def __init__(self):
        self.image = pygame.Surface(TIP_FIELD_RECT.size)
        self.image.fill(WHITE)
        self.rect = TIP_FIELD_RECT
        pygame.sprite.DirtySprite.__init__(self)
    
    def getTip(self, buttonName, SettingName = None, SettingValue = None):
        '''
        this should get tips from the game's tip dictionary, and change the tip field's image according to that
        getTip(String) -> None
        '''
        #this is for options buttons or other buttons that don't have a tip and don't need updating of the tip field
        if buttonName == -1:
            return None
        #get current image
        newTip = self.image.copy()
        #clear the current image
        newTip.fill(WHITE)
        # convert all the QUIT destinations into one
        if "QUIT" in buttonName:
            buttonName = "QUIT"
        # look for it in the tipDict
        if buttonName in tipDict.keys():
            text = tipDict[buttonName]
            # draw out the new tip
            newTip.blit(tipFont.render(text, True, FULL_RED), (10,10))
        elif buttonName == "DEFAULT":
            # do nothing, the image is already cleared
            pass
        elif buttonName == "SETTING":
            text = "Setting for {} changed to {}".format(SettingName, SettingValue)
            newTip.blit(tipFont.render(text, True, FULL_RED), (10,10))
        else:
            raise TipException("Tip for this button not found in tipDict")
        #set new image
        self.image = newTip