'''

@author: DannyUfonek

'''

import sys
import pygame
import pygame.locals as pl
import pygame.mouse as mouse
import core.menuCreator as menuCreator
import core.selectionTip as selectionTip
import core.colourPicker as colourPicker
import core.levelCreator as levelCreator
from core.backgroundDrawer import backgroundDrawer
from core.constants import *


pygame.init()

# start up the window
screensize = pl.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(screensize.size) 
pygame.display.set_caption("Yet another pygame window")
print("window fired up")

#FPS control
clock = pygame.time.Clock()

#group for drawing sprites
allSprites = pygame.sprite.LayeredUpdates(layer = 0)
titleSprites = pygame.sprite.Group()
#group for holding button to update
buttonToDraw = pygame.sprite.GroupSingle()

#Create bottom tip field
def tipFieldInit():
    x = pygame.Surface(TIP_FIELD_RECT.size)
    x.fill(WHITE)
    return x

#default save file (0 will create a new one)
userSave = 0
#default ship surface
shipSurface = GAME_IMAGE_COLLECTION.skyship

#some vars to control further action
playing = False
menuRunning = True
alive = True
'''
One Loop to rule them all, One Loop to find them,
One Loop to bring them all and in the darkness bind them
'''
while alive:
    
    """----------------------------------MAIN MENU CREATION-------------------------------"""
    
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
                            playing = True
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
                            shipImage = colourPicker.setColour(pickedColour)
                            shipColoured.image.blit(shipImage, (0,0))
                            #draw background over both
                            screen.blit(MENU_BACKGROUND, colourOutput.rect.topleft, colourOutput.rect)
                            screen.blit(MENU_BACKGROUND, shipColoured.rect.topleft, shipColoured.rect)
                            #redraw both and update display
                            colourPickShow.draw(screen)
                            rectlist = [colourOutput.rect, shipColoured.rect]
                            pygame.display.update(rectlist)
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
                        tipField.blit(selectionTip.getTip(button.destination), (10,10))
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
            
            if not True in buttonsCursorStatus.values():
                #basically, if no button has the cursor on it, the tipField is cleared.
                screen.blit(MENU_BACKGROUND, (TIP_FIELD_RECT), TIP_FIELD_RECT)
                tipField.blit((selectionTip.getTip("DEFAULT")), (0,0))
                screen.blit(tipField, TIP_FIELD_RECT)
                pygame.display.update(TIP_FIELD_RECT)
                buttonsCursorStatus.clear()

    # wipe screen (sprites should be killed already if we're going to play)
    screen.fill(BLACK)
    pygame.display.flip()
    """----------------------------------GAME STUFF-------------------------------"""
    print("starting game")
    enemies, levelbackground, backgroundOverlay = levelCreator.getLevel(0)
    bgDraw = backgroundDrawer()
    bgDraw.setBackground(levelbackground, increment = 1)
    
    """----------------------------------GAME LOOP-------------------------------"""
    while playing:
        # if menu loop was left by "PLAY" button, we go to play game:

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
        clock.tick(GAME_FPS)
        screen.blit(bgDraw.updateClouds(), (0,0))
        pygame.display.flip()
# when that is done, quit
print(" ")
print("Quitting, nothing left to do")
pygame.quit()
sys.exit()
        