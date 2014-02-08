'''

@author: DannyUfonek

this module should deal with the main menu -> load, create, and do anything that is required
'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
import selectionTip
from core.constants import *
from core.menuButton import menuButton

buttons = pygame.sprite.Group()

allSprites = pygame.sprite.LayeredUpdates(layer = 0)
#array which holds all button destinations' values (used for acting based on them)

def start(screen, tipField):
    
    
    print("Firing up menu........")
    pygame.init()
    
    #coordinates of button column
    buttonColumnTop = 200
    buttonColumnLeft = 200
       
    #for fps control
    clock = pygame.time.Clock()
       
    #create all the buttons
    button1 = menuButton()
    button1.start("Start Game", "GAME")
    button1.rect.x  = (buttonColumnLeft)
    button1.rect.y = (buttonColumnTop)
    button1.add(buttons)
    
    button2 = menuButton()
    button2.start("Options", "OPTIONS")
    button2.rect.x  = (buttonColumnLeft)
    button2.rect.y = (buttonColumnTop + 100)
    button2.add(buttons)
    
    button3 = menuButton()
    button3.start("Extras", "EXTRAS")
    button3.rect.x  = (buttonColumnLeft)
    button3.rect.y = (buttonColumnTop + 200)
    button3.add(buttons)
    
    button4 = menuButton()
    button4.start("Exit", "MAINQUIT")
    button4.rect.x  = (buttonColumnLeft)
    button4.rect.y = (buttonColumnTop + 300)
    button4.add(buttons)
    
    #add buttons to bottom layer
    allSprites.add(buttons, layer = 1)
    print("buttons created on layer 1")
    # draw them on screen and update
    #buttons.draw(screen)
    
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
    #draw sprites
    print("title created and drawn on layer " + str(title1._layer))
    print("top layer of all sprites has the number " + str(allSprites.get_top_layer()))
    print("bottom layer of all sprites has the number " + str(allSprites.get_bottom_layer()))
    allSprites.draw(screen)

    pygame.display.flip()
    print ("sprites created and drawn on screen")
    
    # Main Menu event loop
    menuRunning = True
    
    print ("main menu waiting........")
    
    while menuRunning:
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                menuRunning = False
                print("game closed from main menu")
                '''
                clean up the screen before leaving (like a good module!)
                '''
                screen.blit(MENU_BACKGROUND, (0,0))
                pygame.display.flip()
                return "MAINQUIT"
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
                The same thing happens when the button is mouseovered or something else,
                only steps 7 (and/or 1) are skipped.
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
                        screen.blit(MENU_BACKGROUND, (0, buttonColumnTop), (0, buttonColumnTop, 2000, 2000))
                        pygame.display.flip()
                        return button.destination
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
            #tipField.blit(selectionTip.getTip(), (0,0))
            #pygame.display.update(tipField.get_rect())
            buttonsCursorStatus = []
            for button in buttons:
                screen.blit(MENU_BACKGROUND, (button.rect.x, button.rect.y), button.rect)
                button.update(event)
                buttonToDraw.add(button)
                buttonToDraw.draw(screen)
                pygame.display.update((button.rect))
                buttonsCursorStatus.append(button.getMouseOver())
            
            print(buttonsCursorStatus)
            if buttonsCursorStatus.count(False) == len(buttons.sprites()):
                #basically, if no button has the cursor on it, the tipField is cleared.
                screen.blit(MENU_BACKGROUND, (TIP_FIELD_RECT), TIP_FIELD_RECT)
                tipField.blit((selectionTip.getTip("DEFAULT")), (0,0))
                screen.blit(tipField, TIP_FIELD_RECT)
                pygame.display.update(TIP_FIELD_RECT)
                buttonsCursorStatus = []
                


