'''

@author: DannyUfonek

handles controls changing and assigning them to events
'''
import pygame
import pygame.locals as pl
import collections
import os
import core.constants
from core.constants import *

#for translating and reassigning controls

class settingsHandler(object):
    
    settingsFont = pygame.font.Font(MAIN_MENU_FONT_PATH, 25)
    settingDict = collections.OrderedDict()
    _Number2Name = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT', 'PAUSE', 'ATTACK', 'MUSIC_VOLUME', 'SOUND_VOLUME']
    _Name2Text = {'MOVE_UP':'Up', 'MOVE_DOWN':'Down', 'MOVE_LEFT':'Left', 'MOVE_RIGHT':'Right', 'PAUSE':'Pause', 'ATTACK':'Attack', 'MUSIC_VOLUME':'Music Volume', 'SOUND_VOLUME':'Sound Volume'}
    
    def loadSettings(self):
        '''
        load existing settings file
        '''
        #readdict = {}
        with open(SETTINGS_PATH) as source:
            
            for line in source:
                #load the key and value from each line (strip is there to remove \n)
                (key, val) = line.strip().split(";")
                self.settingDict[key] = val
                
            #self.settingDict = collections.OrderedDict(readdict)
        
        print("Loaded settings: \n {}".format(self.settingDict))
        print("Writing up to constants:")
        
        for setting in self.settingDict:
            if self.settingDict[setting].startswith('K_'):
                #assign value from dictionary to constants
                x = pl.__dict__[self.settingDict[setting]]
                core.constants._ALLOWED_KEYS.append(x)
            else:
                #assign other settings from dictionary to constants
                core.constants._SETTINGS[setting] = self.settingDict[setting]
        print("allowed keys: \n {0}".format(core.constants._ALLOWED_KEYS))
        print("settings: \n {0}".format(core.constants._SETTINGS))
            
    def setSetting(self, settingNumber, settingValue = None):
        '''
        replace the key/value in dictionary and in constants
        see constants for reference which number is which control
        '''
        if settingValue == None:
            print("waiting for key input")
            waitingforinput = True
            while waitingforinput:
                event = pygame.event.wait()
                if event.type == pl.KEYDOWN:
                    print(event.key)
                    '''
                    if event.key in core.constants._ALLOWED_KEYS:
                        # if this key is bound already, remove the existing bond
                        _ALLOWED_KEYS[_ALLOWED_KEYS.index(event.key)] = 
                    '''
                    # if a key is pressed, assign it to the control in constants
                    core.constants._ALLOWED_KEYS[settingNumber] = event.key
                    # convert its integer to string form
                    # get the setting we're saving to
                    # then save it to dictionary
                    eventkeyName = pygame.key.name(event.key)
                    if len(eventkeyName) > 1:
                        #raise case of event name (omg pygame really sucks at this place)
                        eventkeyName = eventkeyName.upper()
                    
                    print("setting {} to {}".format(self._Number2Name[settingNumber], "K_{}".format(eventkeyName)))
                    self.settingDict[self._Number2Name[settingNumber]] = "K_{}".format(eventkeyName)
                    
                    waitingforinput = False
                    return self.settingDict[self._Number2Name[settingNumber]]
                else:
                    pass
        else:
            print(settingValue)
            # limit the setting between 0 to 100 and deal with the two extremes, 0 and 100:
            currentSettingVal = int(self.settingDict[self._Number2Name[settingNumber]])
            if currentSettingVal in range(1,100) or (currentSettingVal == 100 and settingValue == -1) or (currentSettingVal == 0 and settingValue == 1):
                # change value of setting in constants -> this is a dict so we have to convert as well
                core.constants._SETTINGS[self._Number2Name[settingNumber]] = str(int(core.constants._SETTINGS[self._Number2Name[settingNumber]]) + settingValue)
                print("setting {0} to {1}".format(self._Number2Name[settingNumber], int(core.constants._SETTINGS[self._Number2Name[settingNumber]]) + settingValue))
                # convert its integer to string form
                # get the setting we're saving to
                # then save it to dictionary
                
                self.settingDict[self._Number2Name[settingNumber]] = str(int(self.settingDict[self._Number2Name[settingNumber]]) + settingValue)
                print("setting {} to {}".format(self._Number2Name[settingNumber], int(self.settingDict[self._Number2Name[settingNumber]]) + settingValue))
            
    def drawSetting(self, settingNumber = "EMPTY", colour = FULL_RED):
        '''
        draw an existing setting into a surface
        drawSetting(setting) --> Surface
        '''
        if settingNumber == "EMPTY":
            print("drawing _")
            image = self.settingsFont.render("_", True, colour)
        else:
            print("drawing new setting: ".format(settingNumber))
            settingName = self._Number2Name[settingNumber]
            text = self.settingDict[settingName]
            if text.startswith("K_"):
                text = text.partition("K_")[2]
            print("drew " + text)
            image = self.settingsFont.render(text, True, colour)
        return image
        
        
    def saveSettings(self):
        '''
        save the existing settingDict to file
        saveSettings() --> None
        '''
        with open(SETTINGS_PATH, 'w') as output:
            for setting in self.settingDict:
                #write out the dictionary
                value = self.settingDict[setting]
                output.write('{0};{1}\n'.format(setting, value))
            print("saved settings to {}".format(SETTINGS_PATH))
    
    