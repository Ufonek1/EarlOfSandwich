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

def getTip(buttonName, SettingName = None, SettingValue = None):
    '''
    this should get tips from the game's tip dictionary, and write them out into a surface
    getTip(String) -> Surface
    if there's nothing, return empty tip field
    '''
    # convert all the QUIT destinations into one
    if "QUIT" in buttonName:
        buttonName = "QUIT"
    # look for it in the tipDict
    if buttonName in tipDict.keys():
        print("looking for tip on " + buttonName)
        text = tipDict[buttonName]
        tipWritten = tipFont.render(text, True, FULL_RED)
        return tipWritten
    # if it isn't there, return the default surface
    elif buttonName == "DEFAULT":
        return core.tipFieldInit()
    elif buttonName == "SETTING":
        print("looking for tip on " + buttonName)
        text = "Setting for {} changed to {}".format(SettingName, SettingValue)
        tipWritten = tipFont.render(text, True, FULL_RED)
        return tipWritten
    else:
        print("this button doesn't have a tooltip in tipDict")
        return core.tipFieldInit()