'''

@author: DannyUfonek

This is the pregame menu, where the player is able to load his progress, choose level, set some settings, etc.
OR return back to the main menu. Basically it's going to be again a load of buttons that point you somewhere
or do something else. (Change-colour-of-ship type of thing)

This module is a copy of mainMenu

but now this module should include the colourPicker
'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
import core.colourPicker as colourPicker
import core.selectionTip as selectionTip
from core.constants import *
from core.menuButton import menuButton
from core.colourPicker import ColourPicker

buttons = pygame.sprite.Group()

allSprites = pygame.sprite.LayeredUpdates(layer = 0)
#array which holds all button destinations' values (used for acting based on them)

def start(screen, tipField):
    
    print("Firing up pregame menu........")
    pygame.init()
    
    #coordinates of button column
    buttonColumnTop = 200
    buttonColumnLeft = 100
    
    #for fps control
    clock = pygame.time.Clock()
       
    #create all the buttons
    button1 = menuButton()
    button1.start("New Game", "NEW", 0.9)
    button1.rect.x  = (buttonColumnLeft)
    button1.rect.y = (buttonColumnTop + 100)
    button1.add(buttons)
    
    button2 = menuButton()
    button2.start("Load Game", "LOAD", 0.9)
    button2.rect.x  = (buttonColumnLeft)
    button2.rect.y = (buttonColumnTop + 190)
    button2.add(buttons)
    
    button3 = menuButton()
    button3.start("Save colour", "COLOUR", 0.5)
    button3.rect.x  = (buttonColumnLeft + 460)
    button3.rect.y = (buttonColumnTop + 400)
    button3.add(buttons)
    
    button4 = menuButton()
    button4.start("Back to menu", "BACKTOMAIN", 0.9)
    button4.rect.x  = (buttonColumnLeft)
    button4.rect.y = (buttonColumnTop + 280)
    button4.add(buttons)
    
    #add buttons to bottom layer
    allSprites.add(buttons, layer = 1)
    print("buttons created on layer 1")
    
    #the group which holds the button to be drawn (for optimisation)
    buttonToDraw = pygame.sprite.GroupSingle()
    
    # load font for title
    title_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 100)
    #create the title as sprites with text as their source image
    title1 = pygame.sprite.DirtySprite() 
    text1 = (title_font.render("THE GAME", True, FULL_RED))
    title1.image = text1
    title1.rect = title1.image.get_rect()
    title1._layer = 5
    #coordinates of title
    title1.rect.x = 200
    title1.rect.y = 20
    title1.add(allSprites)
    print("title created on layer " + str(title1._layer))
    
    # load font for smalltitle
    smalltitle_font = pygame.font.Font(MAIN_MENU_FONT_PATH, 30)
    #create the title as sprites with text as their source image
    smalltitle1 = pygame.sprite.DirtySprite() 
    text2 = (smalltitle_font.render("Pick your colour:", True, FULL_RED))
    smalltitle1.image = text2
    smalltitle1.rect = title1.image.get_rect()
    smalltitle1._layer = 5
    #coordinates of title
    smalltitle1.rect.x = buttonColumnLeft + 400
    smalltitle1.rect.y = buttonColumnTop - 50
    smalltitle1.add(allSprites)
    
    #the group that holds the colourpicker output sprites
    colourPickShow = pygame.sprite.Group()
    
    #create a colourpicker instance and draw it on the screen
    ColorPicker = ColourPicker()
    ColorPicker.rect.x = buttonColumnLeft + 400
    ColorPicker.rect.y = buttonColumnTop
    allSprites.add(ColorPicker, layer = 2)
    
    #output of colourpicker:
    #colour square:
    colourOutput = pygame.sprite.DirtySprite()
    colourOutput.image = pygame.Surface((50,50))
    colourOutput.image.fill(FULL_GREEN)
    colourOutput.rect = colourOutput.image.get_rect()
    colourOutput.rect.topleft = (buttonColumnLeft+480, buttonColumnTop+325)
    colourOutput.add(colourPickShow)
    #colour on ship:
    shipColoured = pygame.sprite.DirtySprite()
    shipColoured.image = pygame.Surface([100,100]).convert()
    shipColoured.image.blit(GAME_IMAGE_COLLECTION.ship.copy(), (0,0))
    shipColoured.rect = shipColoured.image.get_rect()
    shipColoured.rect.topleft = (buttonColumnLeft+550, buttonColumnTop+280)
    shipColoured.image.set_colorkey(FULL_MAGENTA)
    print("the colourkey of shipColoured.image is " + str(shipColoured.image.get_colorkey()))
    shipColoured.add(colourPickShow)

    # add the group to allSprites
    allSprites.add(colourPickShow, layer = 2)
    
    #draw sprites
    print("top layer of all sprites has the number " + str(allSprites.get_top_layer()))
    print("bottom layer of all sprites has the number " + str(allSprites.get_bottom_layer()))
    allSprites.draw(screen)

    pygame.display.flip()
    print ("sprites created and drawn on screen")
    
    # Main Menu event loop
    pregameMenuRunning = True
    
    print ("pregame menu waiting........")
    
    
    while pregameMenuRunning:
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                pregameMenuRunning = False
                print("game closed from pregame menu")
                '''
                clean up the screen before leaving (like a good module!)
                '''
                screen.blit(MENU_BACKGROUND, (0,0))
                pygame.display.flip()
                return "PREGAMEQUIT"
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
                7. then the destination is outputted to core.init, which then decides based on that where
                to go or what to do next.
                8. then clean up the screen.
                The same thing happens when the button is mouseovered or something else,
                only steps 7, 8, and/or 1 are skipped.
                KEYWORD: OPTIMISATION
                '''
                for button in buttons:
                    if button.getMouseOver():
                        screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                        button.update(event)
                        buttonToDraw.add(button)
                        buttonToDraw.draw(screen)
                        pygame.display.update(button.rect)
                        '''
                        clean up the screen before leaving (like a good module!) (but only on the buttons area)
                        '''
                        screen.blit(MENU_BACKGROUND, (0, buttonColumnTop-50), (0, buttonColumnTop-50, SCREEN_WIDTH, SCREEN_HEIGHT-buttonColumnTop-50))
                        pygame.display.flip()
                        return button.destination
                '''
                Now let's check the colourPicker instance we have there:
                '''
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
                    
            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.getMouseOver():
                        screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                        button.update(event)
                        buttonToDraw.add(button)
                        buttonToDraw.draw(screen)
                        pygame.display.update((button.rect))
                        #change tip according to button and blit it onto the tipField, then onto the screen, then update
                        tipField.blit(selectionTip.getTip(button.destination), (10,10))
                        screen.blit(tipField, (TIP_FIELD_RECT))
                        pygame.display.update(TIP_FIELD_RECT)
            clock.tick(GAME_FPS)
            #we update twice, so that the button doesn't freeze after mouseover/pressing
            '''
            This updates the buttons as well as the tip Field
            - if no button has the mouse on it, the tip field is cleared
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


