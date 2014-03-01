'''

@author: DannyUfonek

'''

import sys
import datetime
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
import core.menuCreator as menuCreator
import core.selectionTip as selectionTip
import core.colourPicker as colourPicker
import core.levelCreator as levelCreator
from core.playerShip import playerShip
from core.settingsHandler import settingsHandler
from core.backgroundDrawer import backgroundDrawer
from core.constants import *


pygame.init()

# start up the window
screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screensize.size) 
pygame.display.set_caption("Yet another pygame window")
print("window fired up")

#FPS controls
clock = pygame.time.Clock()

"""----------------------------------GLOBAL STUFF-------------------------------"""
#group for drawing sprites
allSprites = pygame.sprite.LayeredUpdates(layer = 0)
#layer 0-2 backgrounds
#layer 3 classic buttons & player ship
#layer 4 any other buttons

titleSprites = pygame.sprite.Group()
#group for holding button to update
buttonToDraw = pygame.sprite.GroupSingle()

#Create bottom tip field
def tipFieldInit():
    x = pygame.Surface(TIP_FIELD_RECT.size)
    x.fill(WHITE)
    return x

"""----------------------------------VARIABLES THAT THE SESSION WILL CHANGE-------------------------------"""
#default save file (0 will create a new one)
userSave = 0
#default ship surface
shipSurface = GAME_IMAGE_COLLECTION.skyship
#load settings
settings = settingsHandler()
settings.loadSettings()
#after loading settings, import them and create a dict for referring to
from core.constants import _SETTINGS
from core.constants import _ALLOWED_KEYS

#some vars to control further action
playing = False
startGame = False
menuRunning = True
alive = True
'''
One Loop to rule them all, One Loop to find them,
One Loop to bring them all and in the darkness bind them
'''
while alive:
    
    """----------------------------------MAIN MENU CREATION-------------------------------"""
    """this does nothing if menuRunning is False"""
    if menuRunning == True:
        #background from background collection
        screen.blit(MENU_BACKGROUND, (0,0))
        pygame.display.flip()
        tipField = tipFieldInit()
        screen.blit(tipField, (TIP_FIELD_RECT))
    
        # load font for title
        title_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 100)
        #create the title as sprites with text as their source image
        title1 = pygame.sprite.DirtySprite() 
        text1 = (title_font.render("THE GAME", True, FULL_RED))
        title1.image = text1
        title1.rect = title1.image.get_rect()
        title1._layer = 2
        #coordinates of title
        title1.rect.x = 200
        title1.rect.y = 20
        title1.add(titleSprites)
        print("title created and drawn on layer " + str(title1._layer))
        # draw out titles
        titleSprites.draw(screen)
        
        pygame.display.flip()
        print ("sprites created and drawn on screen")
        
        #create buttons and add them to allSprites
        buttons = menuCreator.getMenu("MAIN")[0]
        allSprites.add(buttons, layer = 3)
        print("top layer of all sprites has the number " + str(allSprites.get_top_layer()))
        print("bottom layer of all sprites has the number " + str(allSprites.get_bottom_layer()))
        
    """----------------------------------MAIN MENU LOOP-------------------------------"""
    while menuRunning:
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("game closed from menu")
                '''
                clean up the screen before leaving (like a good module!)
                '''
                screen.blit(MENU_BACKGROUND, (0,0))
                pygame.display.flip()
                menuRunning = False
                alive = False
            if event.type == pl.KEYDOWN and event.key == pl.K_F2:
                '''
                Screenshot-taking function
                Screenshots are saved under current time
                '''
                #    get current display surface
                screenshot = pygame.display.get_surface()
                # get current time
                now = datetime.datetime.now()
                # replace : with - for it to be a proper filename
                now = str(now).replace(":","-")
                # add .png to be able to save as an image
                now = "{}.png".format(now)
                filepath = os.path.join(SCREENSHOT_PATH, now)
                print("saving screenshot to {}".format(filepath))
                pygame.image.save(screenshot, filepath)
            if event.type == pl.MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                '''
                This is where the button's destination kicks in
                Unfortunately, we have to check each button separately,
                as the pygame.sprite.Group.update() can't return sprites' .update()
                return values.
                What happens here:
                When the user clicks a button: 
                1. all buttons are checked (one by one) to see which one the mouse is on,
                2. the background is drawn over it (and only it)
                3. the button updates
                4. the button gets put into the buttonToDraw one-sprite-only group
                5. buttonToDraw draws it onto the screen
                6. the display updates only on it
                7. then the destination is checked, and except for two special cases, new buttons are
                loaded from menuCreator (that is, all existing buttons removed, and new ones drawn on screen)
                8. then we check the colourpicker. If it isn't there (we aren't in the colour picking menu)
                nothing happens, as it's all contained in the try statement.
                '''
                for button in buttons:
                    if button.getMouseOver():
                        screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                        button.update(event)
                        buttonToDraw.add(button)
                        buttonToDraw.draw(screen)
                        pygame.display.update(button.rect)                   
                        if "QUIT" in button.destination:
                            '''
                            the middle bit is ripped from button.destionation to see from where it was
                            '''
                            print ("game closed from " + button.destination[:button.destination.find("QUIT")] + " MENU")
                            
                            menuRunning = False
                            alive = False
                        elif button.destination == "GAME":
                            print ("Game button was clicked")
                            #erase and kill all existing sprites
                            for sprite in allSprites:
                                screen.blit(MENU_BACKGROUND, (sprite.rect.x, sprite.rect.y), sprite.rect)
                                pygame.display.update((sprite.rect))
                                sprite.kill()
                            #exit loop
                            startGame = True
                            menuRunning = False
                        elif button.destination == "COLOUR":
                            ColorPicker, colourOutput, shipColoured, colourPickerTitle = allSprites.get_sprites_from_layer(layer = 2)
                            #grab the current image of the ship and save it to the variable
                            shipSurface = shipColoured.image
                            #change tip according to button and blit it onto the tipField, then onto the screen, then update
                            tipField.blit((selectionTip.getTip("DEFAULT")), (0,0))
                            tipField.blit(selectionTip.getTip("SAVED"), (10,10))
                            screen.blit(tipField, (TIP_FIELD_RECT))
                            pygame.display.update(TIP_FIELD_RECT)
                        elif button.destination == "OPTIONS":
                            #save button.destination
                            dest = button.destination
                            print ("Options button was clicked")
                            #clear all sprites and
                            #remove them from allSprites
                            for sprite in allSprites:
                                screen.blit(MENU_BACKGROUND, (sprite.rect.x, sprite.rect.y), sprite.rect)
                                pygame.display.update((button.rect))
                                sprite.kill()
                            #get new buttons for appropriate menu
                            print("buttons were removed from group, getting new ones")
                            buttons, optionButtons, optionsTitles, skyshiparrows = (menuCreator.getMenu(dest, settings))
                            allSprites.add(buttons, layer = 3)
                            allSprites.add(optionButtons, layer = 4)
                            allSprites.add(optionsTitles, layer = 2)
                            allSprites.add(skyshiparrows, layer = 2)
                            allSprites.draw(screen)
                            pygame.display.flip()
                        else:
                            #save button.destination
                            dest = button.destination
                            print (dest + " button was clicked")
                            #clear all sprites and
                            #remove them from allSprites
                            for sprite in allSprites:
                                screen.blit(MENU_BACKGROUND, (sprite.rect.x, sprite.rect.y), sprite.rect)
                                pygame.display.update((button.rect))
                                sprite.kill()
                            #get new buttons for appropriate menu
                            print("buttons were removed from group, getting new ones")
                            buttons = (menuCreator.getMenu(dest))[0]
                            allSprites.add(buttons, layer = 3)
                            
                            if dest == "NEW":
                                #load colourPicker
                                allSprites.add(menuCreator.getMenu(dest)[1:], layer = 2)
                                allSprites.draw(screen)
                            else:
                                allSprites.draw(screen)
                            pygame.display.flip()
                            break
                    try:
                        # get sprites for colourpicker - this should equal the colourPicker sprites found there
                        ColorPicker, colourOutput, shipColoured, colourPickerTitle = allSprites.get_sprites_from_layer(layer = 2)
                        colourPickShow = pygame.sprite.Group(colourOutput, shipColoured) 
                        if ColorPicker.getMouseOver():
                            '''
                            the underlying surface of the colourOutput gets filled with the colour that is under the mouse cursor
                            then we redraw it
                            '''
                            pickedColour = ColorPicker.pickColour()
                            colourOutput.image.fill(pickedColour)
                            '''
                            1. Create a new surface by replacing the FULL_GREEN area of the displayed ship's image with the picked colour
                            2. Blit the surface in place of the existing shipColoured.image
                            '''
                            shipSurface = colourPicker.setColour(pickedColour)
                            shipColoured.image.blit(shipSurface, (0,0))
                            #draw background over both
                            screen.blit(MENU_BACKGROUND, colourOutput.rect.topleft, colourOutput.rect)
                            screen.blit(MENU_BACKGROUND, shipColoured.rect.topleft, shipColoured.rect)
                            #redraw both and update display
                            colourPickShow.draw(screen)
                            rectlist = [colourOutput.rect, shipColoured.rect]
                            pygame.display.update(rectlist)
                    except:
                        pass
                    
                    try:
                        #get sprites for options - changing settings
                        optionsButtons = allSprites.get_sprites_from_layer(layer = 4)
                        for button in optionsButtons:
                            if button.getMouseOver():
                                #if button is a key button:
                                if button.setting < 6:
                                    #replace with _
                                    screen.blit(MENU_BACKGROUND, (button.rect), button.rect)
                                    button.image = settings.drawSetting()
                                    buttonToDraw.add(button)
                                    buttonToDraw.draw(screen)
                                    pygame.display.update((button.rect))
                                    #grab the next key pressed down and change setting
                                    settingNumber = button.setting
                                    settingName = settings._Number2Name[settingNumber]
                                    settings.setSetting(settingNumber)
                                    #----redraw button image and change rect----
                                    screen.blit(MENU_BACKGROUND, (button.rect), button.rect)
                                    oldrect = button.rect
                                    button.image = settings.drawSetting(settingNumber)
                                    #get new rect (100 is wider than 1)
                                    button.rect = button.image.get_rect()
                                    #move the rect to the old position
                                    button.rect.topleft = oldrect.topleft
                                    buttonToDraw.add(button)
                                    buttonToDraw.draw(screen)
                                    pygame.display.update([oldrect, button.rect])
                                    #get tip
                                    tipField.blit((selectionTip.getTip("DEFAULT")), (0,0))
                                    tipField.blit(selectionTip.getTip("SETTING", settingName, settings.settingDict[settings._Number2Name[settingNumber]]), (10,10))
                                    screen.blit(tipField, (TIP_FIELD_RECT))
                                    pygame.display.update(TIP_FIELD_RECT)
                                    
                                #if button is the other stuff, do nothing
                                else:
                                    #get tip
                                    tipField.blit((selectionTip.getTip("DEFAULT")), (0,0))
                                    tipField.blit(selectionTip.getTip("WHEEL"), (10,10))
                                    screen.blit(tipField, (TIP_FIELD_RECT))
                                    pygame.display.update(TIP_FIELD_RECT)
                    except:
                        pass
            if event.type == pl.MOUSEBUTTONDOWN and event.button in [4,5]:
                try:
                    #get sprites for options - changing settings
                    optionsButtons = allSprites.get_sprites_from_layer(layer = 4)
                    #get only those changeable by mouse scrolling
                    for button in optionsButtons:
                        if button.setting >= 6:
                            if button.getMouseOver():
                                print("you rolled the wheel on a button")
                                #convert turning of mouse wheel to reduction/increase
                                if event.button == 4:
                                    valueChange = 1
                                elif event.button == 5:
                                    valueChange = -1
                                #grab the next key pressed down and change setting
                                settingNumber = button.setting
                                settingName = settings._Number2Name[settingNumber]
                                settings.setSetting(settingNumber, valueChange)
                                #----redraw button image and change rect----
                                screen.blit(MENU_BACKGROUND, (button.rect), button.rect)
                                oldrect = button.rect
                                button.image = settings.drawSetting(settingNumber)
                                #get new rect (100 is wider than 1)
                                button.rect = button.image.get_rect()
                                #move the rect to the old position
                                button.rect.topleft = oldrect.topleft
                                buttonToDraw.add(button)
                                buttonToDraw.draw(screen)
                                pygame.display.update([oldrect, button.rect])
                except:
                    pass
            if event.type == pl.MOUSEMOTION:
                '''
                here we update buttons if they get mouseovered
                '''
                for button in buttons:
                    if button.getMouseOver():
                        screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                        button.update(event)
                        buttonToDraw.add(button)
                        buttonToDraw.draw(screen)
                        pygame.display.update((button.rect))
                        #change tip according to button and blit it onto the tipField, then onto the screen, then update
                        tipField.blit((selectionTip.getTip("DEFAULT")), (0,0))
                        try:
                            tipField.blit(selectionTip.getTip(button.destination), (10,10))
                        except:
                            # if it's not a menuButton, then no tip should be shownd
                            pass
                        screen.blit(tipField, (TIP_FIELD_RECT))
                        pygame.display.update(TIP_FIELD_RECT)                    
                        
            clock.tick(GAME_FPS)
            #we update twice, so that the button doesn't freeze after mouseover/pressing
            '''
            This updates the buttons (so that they spring back after being clicked)
            as well as the tip Field - if no button has the mouse on it, the tip field is cleared
            '''
            buttonsCursorStatus = {}
                        
            for button in buttons:
                screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                button.update(event)
                buttonToDraw.add(button)
                buttonToDraw.draw(screen)
                pygame.display.update((button.rect))
                buttonsCursorStatus[button] = button.getMouseOver()
                
            for button in allSprites.get_sprites_from_layer(layer = 4):
                buttonsCursorStatus[button] = button.getMouseOver()
            
            if not True in buttonsCursorStatus.values():
                #basically, if no button has the cursor on it, the tipField is cleared.
                screen.blit(MENU_BACKGROUND, (TIP_FIELD_RECT), TIP_FIELD_RECT)
                tipField.blit((selectionTip.getTip("DEFAULT")), (0,0))
                screen.blit(tipField, TIP_FIELD_RECT)
                pygame.display.update(TIP_FIELD_RECT)
                buttonsCursorStatus.clear()

    """----------------------------------GAME STUFF-------------------------------"""
    '''this does nothing if startGame is False'''
    if startGame == True:
        # wipe screen first (sprites should be killed already if we're going to play), just to be sure
        screen.fill(BLACK)
        pygame.display.flip()
        print("starting game")
        
        #KEYBOARD
        pygame.key.set_repeat(KEY_REPEAT_TIME, KEY_REPEAT_TIME)
        
        
        
        #load level
        enemies, levelbackground, backgroundOverlay = levelCreator.getLevel(0)
        
        #load background
        bgDraw = backgroundDrawer()
        bgDraw.setBackground(levelbackground, increment = 1)
        #draw background
        screen.blit(levelbackground, (GAME_SCREEN_RECT))
        #save empty background
        emptylevelbackground = levelbackground.copy()
        
        #the player's ship
        skyship = playerShip()
        skyship.load(shipSurface)
        skyship.rect.centerx = GAME_SCREEN_RECT.centerx
        #draw to bottom of game screen
        skyship.rect.y = GAME_SCREEN_RECT.height - skyship.rect.height
        allSprites.add(skyship, layer = 3)
        allSprites.draw(screen)
        
        #single group for drawing spritesd
        spriteToDraw = pygame.sprite.GroupSingle()
        
        #simple counter for stuff that doesn't update every frame
        frame = 0
        
        #update display
        pygame.display.flip()
        
        playing = True
    """----------------------------------GAME LOOP-------------------------------"""
    while playing:
        # if menu loop was left by "PLAY" button, we go to play game:
        rectlist = []
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("game closed from game")
                '''
                clean up the screen before leaving (like a good module!)
                '''
                screen.fill(BLACK)
                pygame.display.flip()
                playing = False
                alive = False
            if event.type == pl.KEYDOWN and event.key == pl.K_F2:
                '''
                Screenshot-taking function
                Screenshots are saved under current time
                '''
                #    get current display surface
                screenshot = pygame.display.get_surface()
                # get current time
                now = datetime.datetime.now()
                # replace : with - for it to be a proper filename
                now = str(now).replace(":","-")
                # add .png to be able to save as an image
                now = "{}.png".format(now)
                filepath = os.path.join(SCREENSHOT_PATH, now)
                print("saving screenshot to {}".format(filepath))
                pygame.image.save(screenshot, filepath)
        keyStates = []
        # get the current state of all allowed buttons,
        # = filter out the unbinded ones
        for key in _ALLOWED_KEYS:
            keyStates.append(pygame.key.get_pressed()[key])
        '''
        ship behaviour goes here
        '''
        if True in keyStates[:4]:
            # if any of the direction keys are pressed, move the ship:
            
            # draw background with clouds over ship but move it according to where the game screen is - reduce the game screen offset
            screen.blit(levelbackground, skyship.rect, (skyship.rect.move(-GAME_SCREEN_LEFT, -GAME_SCREEN_TOP)))
            print(skyship.rect)
            pygame.display.update(skyship.rect)
            # move the ship itself
            skyship.move(keyStates[:4])
            # redraw it on screen & update display
            spriteToDraw.add(skyship)
            spriteToDraw.draw(screen)
            pygame.display.update(skyship.rect)
    
        clock.tick(GAME_FPS)
        
        # animate ship every third frame
        if frame % 3 == 0 or frame == 0:
            #animate the ship
            skyship.update()
            spriteToDraw.add(skyship)
            spriteToDraw.draw(screen)
            pygame.display.update(skyship.rect)
        
        #update background only every fourth frame
        if frame % 4 == 0 or frame == 0:
            # create new bg
            new_background = levelbackground.copy()
            #clean level background
            new_background.blit(emptylevelbackground, (0,0))
            # update only places that held clouds
            
            # get new surface of clouds and their rects
            clouds, rectlist = bgDraw.updateClouds()
            # blit new clouds onto level background
            new_background.blit(clouds, (0,0))
            levelbackground.blit(new_background, (0,0))
            screen.blit(new_background, GAME_SCREEN_RECT)
            # sprites are redrawn as well, so that clouds never end up on top of them
            allSprites.draw(screen)
            # however, we still update only cloud places
            pygame.display.update(rectlist)
 
        if frame == 11:
            frame = 0
        else:
            frame += 1
    waitingforinput = True
    print(_ALLOWED_KEYS)
    print(_SETTINGS)
    print(settings.settingDict)

    settings.saveSettings()
    
    #clear screen for whatever comes next
    screen.fill(BLACK) 
    pygame.display.flip()

# wipe screen 
screen.fill(BLACK)
pygame.display.flip()

# when that is done, quit
print(" ")
print("Quitting, nothing left to do")
pygame.quit()
sys.exit()
        