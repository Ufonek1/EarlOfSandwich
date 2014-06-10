'''

@author: DannyUfonek

'''

import sys
import datetime
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
import core.menuCreator as menuCreator
import core.colourPicker as colourPicker
import core.levelCreator as levelCreator
from core.playerShip import playerShip
from core.settingsHandler import settingsHandler
from core.cloudDrawer import cloudDrawer
from core.selectionTip import tipField
from core.constants import *


pygame.init()

#FPS controls
clock = pygame.time.Clock()


"""----------------------------------GLOBAL, CONSTANT STUFF-------------------------------"""
# load fonts
title_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 100)
small_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 40)
tiny_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 25)
main_title_font = pygame.font.Font(MAIN_TITLE_FONT_PATH, 100)

# sprite groups
allSprites = pygame.sprite.LayeredUpdates(layer = 0)
#layers (see constants)w
#layer 0-1 background
#layer 2 tip field
#layer 3 classic buttons & player ship
#layer 4 any other buttons
#layer 5 debugging
debugSprites = pygame.sprite.Group()
titleSprites = pygame.sprite.Group()



"""----------------------------------GLOBAL DEBUGGING-------------------------------"""
fpsdisplay = pygame.sprite.DirtySprite()
text = "FPS: 60"
image = tiny_font.render(text, True, FULL_RED)
fpsdisplay.image = image
fpsdisplay.rect = fpsdisplay.image.get_rect().move(10,10)

debugSprites.add(fpsdisplay)

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
ResNotPicked = True
Playing = False
StartGame = False
Paused = False
MenuRunning = True
Alive = True
DEBUG_MODE = False
CLEAR_DEBUG = False

"""----------------------------------RESOLUTION PICKING WINDOW-------------------------------"""
# start up the window

screen = pygame.display.set_mode((RES_MENU_WIDTH,RES_MENU_HEIGHT)) 
pygame.display.set_caption("Yet another pygame window")
print("resolution window fired up")

resbuttons, resTitles = menuCreator.getMenu("RESOLUTION")
allSprites.add(resbuttons, layer = 2)
allSprites.add(resTitles, layer = 3)
allSprites.draw(screen)
pygame.display.flip()



# wait for user to pick resolution
while ResNotPicked:
    RectsToUpdate = []
    for event in pygame.event.get():
        if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
            print("game closed from res menu")
            '''
            clean up the screen before leaving (like a good module!)
            '''
            ResNotPicked = False
            Alive = False
            # exit game - it's ok here, nothing has happened yet
            sys.exit()
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
        if event.type == pl.KEYDOWN and event.key == pl.K_F3:
            '''
            debugging function
            '''
            if DEBUG_MODE:
                DEBUG_MODE = False
                CLEAR_DEBUG = True
                allSprites.remove(fpsdisplay)
                print("debug mode off")
            else:
                DEBUG_MODE = True
                allSprites.add(fpsdisplay, layer = DEBUG_LAYER)
                print("debug mode on")                               
        if event.type == pl.MOUSEBUTTONUP:
            # if mouse is clicked, see which button was clicked on
            for button in resbuttons:
                if button.getMouseOver() == True:
                    button.update(event)
                    pygame.display.update(button.rect)
                    ResNotPicked = False
                    #set resolution (see menuCreator and constants for explanation)
                    DisplayRect, fullscreen = button.destination
                    # int, bool <-- (int, bool)
    for button in resbuttons:
        button.update(event)
        RectsToUpdate.append(button.rect)      
    
    #classic procedure
    screen.fill(BLACK)
    pygame.display.update(allSprites.draw(screen))
    clock.tick(GAME_FPS)


#start up normal window
if fullscreen == True:
    screen = pygame.display.set_mode(DisplayRect.size, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(DisplayRect.size, 0)
pygame.display.set_caption("Yet another pygame window")
print("main window fired up")

# delete resolution stuff
del resbuttons, resTitles

# SET UP SCREEN
#get size of display
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

#resized menu background
MENU_BACKGROUND = pygame.transform.scale(BACKGROUND_COLLECTION.menubackground, (SCREEN_WIDTH, SCREEN_HEIGHT))


# wipe allSprites
allSprites = pygame.sprite.LayeredUpdates()

'''
One Loop to rule them all, One Loop to find them,
One Loop to bring them all and in the darkness bind them
'''
while Alive:
    
    """----------------------------------MAIN MENU CREATION-------------------------------"""
    """this does nothing if MenuRunning is False"""
    if MenuRunning == True:
        #background from background collection
        screen.blit(MENU_BACKGROUND, (0,0))
        pygame.display.flip()
        
        #create tip field
        TipField = tipField()
        allSprites.add(TipField, layer = 0)
        
        #create dict for storing button mouseovers
        buttonsCursorStatus = {}
        
        #create the title as sprites with text as their source image
        title1 = pygame.sprite.DirtySprite() 
        text1 = (main_title_font.render("The Game", True, FULL_RED))
        title1.image = text1
        title1.rect = title1.image.get_rect()
        title1._layer = 2
        #coordinates of title
        title1.rect.x = 20
        title1.rect.y = 20
        title1.add(titleSprites)
        print("title created and drawn on layer " + str(title1._layer))        

        print ("sprites created and drawn on screen")
        
        #create buttons and add them to allSprites
        buttons = menuCreator.getMenu("MAIN")[0]
        allSprites.add(buttons, layer = 3)
        print("top layer of all sprites has the number " + str(allSprites.get_top_layer()))
        print("bottom layer of all sprites has the number " + str(allSprites.get_bottom_layer()))
        # draw out titles and other sprites
        titleSprites.draw(screen)
        allSprites.draw(screen)
        pygame.display.flip()
        
    """----------------------------------MAIN MENU LOOP-------------------------------"""
    while MenuRunning:
        # refresh stuff
        RectsToUpdate = []
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("game closed from menu")
                '''
                clean up the screen before leaving (like a good module!)
                '''
                MenuRunning = False
                Alive = False
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
            if event.type == pl.KEYDOWN and event.key == pl.K_F3:
                '''
                debugging function
                '''
                if DEBUG_MODE:
                    DEBUG_MODE = False
                    CLEAR_DEBUG = True
                    allSprites.remove(fpsdisplay)
                    print("debug mode off")
                else:
                    DEBUG_MODE = True
                    allSprites.add(fpsdisplay, layer = DEBUG_LAYER)
                    print("debug mode on")
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
                        SFX_CLICK.play()
                        # redraw button to on-clicked image
                        screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                        button.update(event)
                        pygame.display.update(button.rect)                   
                        if "QUIT" in button.destination:
                            '''
                            the middle bit is ripped from button.destionation to see from where it was
                            '''
                            print ("game closed from " + button.destination[:button.destination.find("QUIT")] + " MENU")
                            
                            MenuRunning = False
                            Alive = False
                        elif button.destination == "GAME":
                            print ("Game button was clicked")
                            #remove debug sprites and tipfield
                            Debug = allSprites.remove_sprites_of_layer(DEBUG_LAYER)
                            #erase and kill all existing sprites
                            for sprite in allSprites:
                                RectsToUpdate.append(sprite.rect.copy())
                                sprite.kill()
                            #add debugger back
                            allSprites.add(Debug, layer = DEBUG_LAYER)
                            #exit loop
                            StartGame = True
                            MenuRunning = False
                        elif button.destination == "COLOUR":
                            ColorPicker, colourOutput, shipColoured, colourPickerTitle = allSprites.get_sprites_from_layer(layer = 2)
                            #grab the current image of the ship and save it to the variable
                            shipSurface = shipColoured.image
                            """
                            TODO - figure this out once we get to campaign saving
                            """
                            #change tip according to button and blit it onto the TipField, then onto the screen
                            TipField.getTip("SAVED")
                            #add rect to update
                            RectsToUpdate.append(TIP_FIELD_RECT)
                        elif button.destination == "OPTIONS":
                            #save button.destination
                            dest = button.destination
                            print ("Options button was clicked")
                            #remove debug sprites and tipfield
                            Debug = allSprites.remove_sprites_of_layer(DEBUG_LAYER)
                            TF = allSprites.remove_sprites_of_layer(0)
                            #remove them from allSprites
                            for sprite in allSprites:
                                RectsToUpdate.append(sprite.rect.copy())
                                sprite.kill()
                            #get new buttons for appropriate menu
                            print("buttons were removed from group, getting new ones")
                            buttons, optionButtons, optionsTitles, skyshiparrows = (menuCreator.getMenu(dest, settings))
                            allSprites.add(buttons, layer = 3)
                            allSprites.add(optionButtons, layer = 4)
                            allSprites.add(optionsTitles, layer = 2)
                            allSprites.add(skyshiparrows, layer = 2)
                            #add debugger and TipField back
                            allSprites.add(Debug, layer = DEBUG_LAYER)
                            allSprites.add(TF, layer = 0)
                            #update whole screen, it's a lot of stuff
                        else:
                            #save button.destination
                            dest = button.destination
                            print (dest + " button was clicked")
                            #clear all sprites and
                            Debug = allSprites.remove_sprites_of_layer(DEBUG_LAYER)
                            TipF = allSprites.remove_sprites_of_layer(0)
                            #remove them from allSprites
                            for sprite in allSprites:
                                screen.blit(MENU_BACKGROUND, (sprite.rect.x, sprite.rect.y), sprite.rect)
                                RectsToUpdate.append(sprite.rect.copy())
                                sprite.kill()
                            #get new buttons for appropriate menu
                            print("buttons were removed from group, getting new ones")
                            buttons = (menuCreator.getMenu(dest))[0]
                            allSprites.add(buttons, layer = 3)
                            #add debugger and TipField back
                            allSprites.add(Debug, layer = DEBUG_LAYER)
                            allSprites.add(TipF, layer = 0)
                            
                            if dest == "NEW":
                                #load colourPicker and related stuff
                                allSprites.add(menuCreator.getMenu(dest)[1:], layer = 2)
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
                            #add for redrawing and updating
                            allSprites.add(colourPickShow)
                            RectsToUpdate = RectsToUpdate + [colourOutput.rect, shipColoured.rect]
                    except:
                        pass
                    
                    try:
                        #get sprites for options - changing settings
                        optionsButtons = allSprites.get_sprites_from_layer(layer = 4)
                        # single group for redrawing the one options button
                        buttonToDraw = pygame.sprite.GroupSingle()
                        for button in optionsButtons:
                            if button.getMouseOver():
                                #if button is a key button:
                                if button.setting < 6:
                                    """
                                    Here it's okay to be messy, as the game is Paused when we're waiting for input
                                    It's also gonna look cool when the background animation stops while you're setting your keys :3
                                    """
                                    #replace with _
                                    screen.blit(MENU_BACKGROUND, (button.rect), button.rect)
                                    button.image = settings.drawSetting()
                                    buttonToDraw.add(button)
                                    buttonToDraw.draw(screen)
                                    pygame.display.update((button.rect))
                                    #grab the next key pressed down and change setting
                                    settingNumber = button.setting
                                    settingName = settings._Number2Name[settingNumber]
                                    settingValue = settings.setSetting(settingNumber)
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
                                    TipField.getTip("SETTING", settingName, settingValue)
                                    RectsToUpdate.append(TIP_FIELD_RECT)
                                    
                                #if button is the other stuff, do nothing
                                else:
                                    #get tip
                                    TipField.getTip("WHEEL")
                                    RectsToUpdate.append(TIP_FIELD_RECT)
                    except:
                        pass
            if event.type == pl.MOUSEBUTTONDOWN and event.button in [4,5]:
                #if the mouse wheel is scrolled:
                try:
                    #get sprites for options - changing settings
                    optionsButtons = allSprites.get_sprites_from_layer(layer = 4)
                    #get only those changeable by mouse scrolling
                    for button in optionsButtons:
                        if button.setting >= 6:
                            if button.getMouseOver():
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
                                if button.setting < 6:
                                    oldrect = button.rect
                                    button.image = settings.drawSetting(settingNumber)
                                    #get new rect (100 is wider than 1)
                                    button.rect = button.image.get_rect()
                                    #move the rect to the old position
                                    button.rect.topleft = oldrect.topleft
                                else:
                                    button.image = settings.drawSetting(settingNumber)
                                buttonToDraw.add(button)
                                buttonToDraw.draw(screen)
                                pygame.display.update([oldrect, button.rect])
                except:
                    pass
        '''
        here we update buttons and check if they are mouseovered
        '''
        #get regular buttons and options buttons
        for button in allSprites.get_sprites_from_layer(layer = 3) + allSprites.get_sprites_from_layer(layer = 4):
            # update (change frame) and save mouseover
            MouseOver = button.update(event)
            buttonsCursorStatus[button] = MouseOver
            if MouseOver:
                RectsToUpdate.append(button.rect.copy())
                #change tip according to button and blit it onto the TipField
                TipField.getTip(button.destination)
                RectsToUpdate.append(TIP_FIELD_RECT)                
                     
        '''
        this updates the tip Field - if no button has the mouse on it, the tip field is cleared
        '''           
        if not True in buttonsCursorStatus.values():
            #basically, if no button has the cursor on it, the TipField is cleared:
            # get default blank surface
            TipField.getTip("DEFAULT")
            #add rect for updating
            RectsToUpdate.append(TIP_FIELD_RECT)
            buttonsCursorStatus.clear()
        
        #clear buttons states
        buttonsCursorStatus.clear()
        
        """----------------------------------DEBUGGING-------------------------------"""
        fpsdisplayoldrect = None
        if DEBUG_MODE == True:
            # update debugger
            fpsdisplayoldrect = fpsdisplay.rect.copy()
            text = "FPS: {}".format(int(round(clock.get_fps())))
            image = tiny_font.render(text, True, FULL_RED)
            fpsdisplay.image = image
            fpsdisplay.rect = fpsdisplay.image.get_rect().move(10,10)
            RectsToUpdate = RectsToUpdate + [fpsdisplayoldrect, fpsdisplay.rect]
        if CLEAR_DEBUG == True:
            # clear off debugging sprites (but only once)
            debugSprites.clear(screen, MENU_BACKGROUND)
            RectsToUpdate = RectsToUpdate + [fpsdisplayoldrect, fpsdisplay.rect]
            CLEAR_DEBUG = False
        
        """
        this is okay, we can afford lower fps in menu
        """
        screen.blit(MENU_BACKGROUND, (0,0))
        RectsToUpdate = RectsToUpdate + allSprites.draw(screen)
        pygame.display.update(RectsToUpdate)
        
        clock.tick(GAME_FPS)

    """----------------------------------GAME STUFF-------------------------------"""
    '''this does nothing if StartGame is False -> StartGame is true only when we start a new level,
    if we pause, then StartGame remains False'''
    if StartGame == True:
        # wipe screen first (sprites should be killed already if we're going to play), just to be sure
        screen.fill(BLACK)
        pygame.display.flip()
        print("starting game")
        
        #KEYBOARD
        #pygame.key.set_repeat(KEY_REPEAT_TIME, KEY_REPEAT_TIME)
        
        #position game
        GAME_SCREEN_RECT.centerx = DisplayRect.centerx - 150
        GAME_SCREEN_RECT.centery = DisplayRect.centery
        PLAYABLE_RECT.center = GAME_SCREEN_RECT.center
        # move to bottom part of screen
        PLAYABLE_RECT.y = PLAYABLE_RECT.y + 250
        
        #load level
        enemies, levelbackground, backgroundOverlay = levelCreator.getLevel(0)
        
        #load background
        cloudDraw = cloudDrawer()
        cloudDraw.load(increment = 1)
        #draw background
        screen.blit(levelbackground, (GAME_SCREEN_RECT))
        #create full screen background
        Screenbackground = pygame.Surface(DisplayRect.size)
        Screenbackground.fill(BLACK)
        Screenbackground.blit(levelbackground,(GAME_SCREEN_RECT))
        
        #the player's ship
        skyship = playerShip()
        skyship.load(shipSurface)
        skyship.rect.centerx = PLAYABLE_RECT.centerx
        #draw to bottom of game screen
        skyship.rect.y = PLAYABLE_RECT.bottom - skyship.rect.height
               
        allSprites.add(skyship, layer = 3)
        allSprites.draw(screen)

        #simple counter for stuff that doesn't update every frame
        frame = 0
        
        #update display
        pygame.display.flip()
        
        # pass the game further
        StartGame = False
        Playing = True
    """----------------------------------GAME LOOP-------------------------------"""
    while Playing:
        # if menu loop was left by "PLAY" button, we go to play game:
            
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("game closed from game")
                '''
                clean up the screen before leaving (like a good module!)
                '''
                screen.fill(BLACK)
                pygame.display.flip()
                Playing = False
                Alive = False
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
            if event.type == pl.KEYDOWN and event.key == pl.K_F3:
                '''
                debugging function
                '''
                if DEBUG_MODE:
                    DEBUG_MODE = False
                    CLEAR_DEBUG = True
                    allSprites.remove(fpsdisplay)
                    print("debug mode off")
                else:
                    DEBUG_MODE = True
                    allSprites.add(fpsdisplay, layer = DEBUG_LAYER)
                    print("debug mode on")
            if event.type == pl.KEYDOWN and event.key == _ALLOWED_KEYS[4]:
                # stop game loop
                Paused = True
                Playing = False
        
        keyStates = []
        # get the current state of all allowed buttons,
        # = filter out the unbinded ones
        for key in _ALLOWED_KEYS:
            keyStates.append(pygame.key.get_pressed()[key])
        '''
        ship behaviour goes here
        '''
        oldshiprect = None
        newshiprect = None
        RectsToUpdate = []
        if True in keyStates[:4]:
            # if any of the direction keys are pressed, move the ship:
            moving, oldshiprect, newshiprect = skyship.move(keyStates[:4])

        # animate ship every third frame
        if frame % 3 == 0 or frame == 0:
            #animate the ship
            skyship.update()
        
        #update background only every fourth frame
        cloudoldrectlist = []
        cloudnewrectlist = []
        if frame % 10 == 0 or frame == 0:
            # get new surface of clouds and their updating rects - these are chopped off so that clouds don't leak out of the game screen
            clouds, cloudoldrectlist, cloudnewrectlist = cloudDraw.update(allSprites)
        
        fpsdisplayoldrect = None
        if DEBUG_MODE == True:
            fpsdisplayoldrect = fpsdisplay.rect.copy()
            text = "FPS: {}".format(int(round(clock.get_fps())))
            image = tiny_font.render(text, True, FULL_RED)
            fpsdisplay.image = image
            fpsdisplay.rect = fpsdisplay.image.get_rect().move(10,10)
            
        # frame counter
        if frame == 59:
            frame = 0
        else:
            frame += 1
        
        if CLEAR_DEBUG == True:
            # clear off debugging sprites
            debugSprites.clear(screen, Screenbackground)
            RectsToUpdate = [fpsdisplayoldrect, fpsdisplay.rect]
            CLEAR_DEBUG = False
        
        #draw everything
        allSprites.clear(screen, Screenbackground)
        allSprites.draw(screen)
        
        # update display
        RectsToUpdate = RectsToUpdate + cloudoldrectlist + cloudnewrectlist + [newshiprect, oldshiprect, skyship.rect, fpsdisplayoldrect, fpsdisplay.rect]
        pygame.display.update(RectsToUpdate)
        
        clock.tick(GAME_FPS)

    """----------------------------------PAUSE PREPARATION-------------------------------"""    
    if Paused:
        # cover the screen with a transparent surface and some text
        cover = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), flags = 1011001)
        cover.fill(TRANSPARENT_BLACK)
        screen.blit(cover, (0,0))
        # create title
        text = "Paused"
        image = title_font.render(text, True, FULL_RED)
        title = pygame.sprite.DirtySprite()
        # get its size and position it right
        title.image = image
        title.rect = title.image.get_rect()
        title.rect.centerx = GAME_SCREEN_RECT.centerx
        title.rect.top = GAME_SCREEN_RECT.top + 50
        #add to sprites
        allSprites.add(title, layer = PAUSE_LAYER)
        RectsToUpdate.append(title.rect.copy())
        # do the same with the second text
        # get the key for pause
        text = "press {} to return to game".format(pygame.key.name(_ALLOWED_KEYS[4]))
        image = small_font.render(text, True, FULL_RED)
        Gamereturn = pygame.sprite.DirtySprite()
        # get its size and position it right
        Gamereturn.image = image
        Gamereturn.rect = Gamereturn.image.get_rect()
        Gamereturn.rect.centerx = GAME_SCREEN_RECT.centerx
        Gamereturn.rect.top = GAME_SCREEN_RECT.top + 200
        #add to sprites
        allSprites.add(Gamereturn, layer = PAUSE_LAYER)
        RectsToUpdate.append(Gamereturn.rect.copy())
        # do the same with the third text
        # get the key for pause
        text = "or press {} to return to main menu".format(pygame.key.name(_ALLOWED_KEYS[5]))
        image = small_font.render(text, True, FULL_RED)
        Menureturn = pygame.sprite.DirtySprite()
        # get its size and position it right
        Menureturn.image = image
        Menureturn.rect = Menureturn.image.get_rect()
        Menureturn.rect.centerx = GAME_SCREEN_RECT.centerx
        Menureturn.rect.top = GAME_SCREEN_RECT.top + 260
        #add to sprites
        allSprites.add(Menureturn, layer = PAUSE_LAYER)
        RectsToUpdate.append(Menureturn.rect.copy())
        
        RectsToUpdate.append(GAME_SCREEN_RECT)
        PauseSprites = pygame.sprite.Group(allSprites.get_sprites_from_layer(PAUSE_LAYER))
        PauseSprites.draw(screen)
        pygame.display.update(RectsToUpdate)
    """----------------------------------PAUSE LOOP-------------------------------"""    
    while Paused:
        #refresh stuff
        RectsToUpdate = []
        for event in pygame.event.get():
            # classic quit and screenshot stuff
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                print("game closed from Paused game")
                '''
                clean up the screen before leaving (like a good module!)
                '''
                screen.fill(BLACK)
                pygame.display.flip()
                # leave loop
                Paused = False
                Alive = False
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
            if event.type == pl.KEYDOWN and event.key == pl.K_F3:
                '''
                debugging function
                '''
                if DEBUG_MODE:
                    DEBUG_MODE = False
                    CLEAR_DEBUG = True
                    allSprites.remove(fpsdisplay)
                    print("debug mode off")
                else:
                    DEBUG_MODE = True
                    allSprites.add(fpsdisplay, layer = DEBUG_LAYER)
                    print("debug mode on")
            if event.type == pl.KEYDOWN and event.key == _ALLOWED_KEYS[4]:
                # return to game loop (clear screen and redraw needed stuff)
                screen.blit(Screenbackground, (0,0))
                allSprites.clear(screen, Screenbackground)
                for sprite in allSprites.get_sprites_from_layer(PAUSE_LAYER):
                    RectsToUpdate.append(sprite.rect.copy())
                    #remove pause overlay sprites
                    sprite.kill()
                allSprites.draw(screen)
                RectsToUpdate.append(GAME_SCREEN_RECT)
                pygame.display.update(RectsToUpdate)
                Paused = False
                Playing = True
            if event.type == pl.KEYDOWN and event.key == _ALLOWED_KEYS[5]:
                # return to menu loop (clear screen and kill all sprites and redraw needed stuff)
                # remove the debugsprites
                Debug = allSprites.remove_sprites_of_layer(DEBUG_LAYER)
                #clear screen and kill everything
                screen.fill(BLACK)
                for sprite in allSprites:
                    sprite.kill()
                pygame.display.flip()
                # readd the debugsprites
                allSprites.add(Debug, layer = DEBUG_LAYER)
                Paused = False
                MenuRunning = True
                
        fpsdisplayoldrect = None
        if DEBUG_MODE == True:
            fpsdisplayoldrect = fpsdisplay.rect.copy()
            text = "FPS: {}".format(int(round(clock.get_fps())))
            image = tiny_font.render(text, True, FULL_RED)
            fpsdisplay.image = image
            fpsdisplay.rect = fpsdisplay.image.get_rect().move(10,10)
            RectsToUpdate = RectsToUpdate + [fpsdisplayoldrect, fpsdisplay.rect]
        
        if CLEAR_DEBUG == True:
            # clear off debugging sprites (but only once)
            debugSprites.clear(screen, Screenbackground)
            RectsToUpdate = RectsToUpdate + [fpsdisplayoldrect, fpsdisplay.rect]
            CLEAR_DEBUG = False
        
        allSprites.clear(screen, Screenbackground)
        allSprites.draw(screen)
        pygame.display.update(RectsToUpdate)
        
        clock.tick(GAME_FPS)

print(_ALLOWED_KEYS)
print(_SETTINGS)
print(settings.settingDict)

settings.saveSettings()

# wipe screen 
screen.fill(BLACK)
pygame.display.flip()

# when that is done, quit
print(" ")
print("Quitting, nothing left to do")
pygame.quit()
sys.exit()
        