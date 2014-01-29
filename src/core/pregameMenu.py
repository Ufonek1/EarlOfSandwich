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
from core.constants import *
from menuButton import menuButton
from colourPicker import ColourPicker

buttons = pygame.sprite.Group()

allSprites = pygame.sprite.LayeredUpdates(layer = 0)
#array which holds all button destinations' values (used for acting based on them)

def start(screen):
    
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
    button1.rect.y = (buttonColumnTop + 300)
    button1.add(buttons)
    
    button2 = menuButton()
    button2.start("Load Game", "LOAD", 0.9)
    button2.rect.x  = (buttonColumnLeft)
    button2.rect.y = (buttonColumnTop + 390)
    button2.add(buttons)
    
    button3 = menuButton()
    button3.start("Save colour", "COLOUR", 0.5)
    button3.rect.x  = (buttonColumnLeft + 500)
    button3.rect.y = (buttonColumnTop + 300)
    button3.add(buttons)
    
    button4 = menuButton()
    button4.start("Back to menu", "BACKTOMAIN", 0.9)
    button4.rect.x  = (buttonColumnLeft)
    button4.rect.y = (buttonColumnTop + 480)
    button4.add(buttons)
    
    #add buttons to bottom layer
    allSprites.add(buttons, layer = 1)
    print("buttons created on layer 1")
    
    #the group which holds the button to be drawn (for optimisation)
    buttonToDraw = pygame.sprite.GroupSingle()
    
    #the group that holds the colourpicker output sprite
    colourPickShow = pygame.sprite.GroupSingle()
    
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
    
    #@TODO temp code for layout
    '''
    spectrum = pygame.sprite.Sprite()
    spectrum.image = GAME_IMAGE_COLLECTION.spectrum
    spectrum.rect = spectrum.image.get_rect()
    spectrum.rect.x = buttonColumnLeft + 500
    spectrum.rect.y = buttonColumnTop + 50
    spectrum.add(allSprites)
    '''
    #create a colourpicker instance and draw it on the screen
    ColorPicker = ColourPicker()
    ColorPicker.rect.x = buttonColumnLeft + 300
    ColorPicker.rect.y = buttonColumnTop
    allSprites.add(ColorPicker, layer = 2)
    
    #output of colourpicker:
    colourOutput = pygame.sprite.DirtySprite()
    colourOutput.image = pygame.Surface((50,50))
    colourOutput.rect = colourOutput.image.get_rect()
    colourOutput.rect.topleft = (buttonColumnLeft+440, buttonColumnTop+300)
    allSprites.add(colourOutput, layer = 2)
    colourPickShow.add(colourOutput)
    
    #draw sprites
    print("top layer of all sprites has the number " + str(allSprites.get_top_layer()))
    print("bottom layer of all sprites has the number " + str(allSprites.get_bottom_layer()))
    allSprites.draw(screen)

    pygame.display.flip()
    print ("sprites created and drawn on screen")
    
    # Main Menu event loop
    pregameMenuRunning = True
    
    print ("pregame menu waiting........")
    click1, click2, click3 = mouse.get_pressed()
    
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
            if event.type == pl.MOUSEBUTTONDOWN and click1:
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
                        screen.blit(MENU_BACKGROUND, (buttonColumnLeft, buttonColumnTop-50), (buttonColumnLeft, buttonColumnTop-50, 2000, 2000))
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
                    colourOutput.image.fill(ColorPicker.pickColour())
                    screen.blit(MENU_BACKGROUND, colourOutput.rect.topleft, colourOutput.rect)
                    colourPickShow.add(colourOutput)
                    colourPickShow.draw(screen)
                    pygame.display.update((colourOutput.rect))
                    
            if event.type == pl.MOUSEMOTION:
                for button in buttons:
                    if button.getMouseOver():
                        screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                        button.update(event)
                        buttonToDraw.add(button)
                        buttonToDraw.draw(screen)
                        pygame.display.update((button.rect))
            clock.tick(GAME_FPS)
            #we update twice, so that the button doesn't freeze after mouseover/pressing  
            for button in buttons:
                screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                button.update(event)
                buttonToDraw.add(button)
                buttonToDraw.draw(screen)
                pygame.display.update((button.rect))


