'''

@author: DannyUfonek

this module should deal with the main menu -> load, create, and do anything that is required
'''

import pygame
import pygame.locals as pl
import pygame.mouse as mouse
from core.constants import *
from menuButton import menuButton

buttons = pygame.sprite.Group()

allSprites = pygame.sprite.LayeredUpdates(layer = 0)
#array which holds all button destinations' values (used for acting based on them)

def start(screen):
    
    
    print "Firing up menu........"
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
    button1.add(allSprites)
    
    button2 = menuButton()
    button2.start("Options", "OPTIONS")
    button2.rect.x  = (buttonColumnLeft)
    button2.rect.y = (buttonColumnTop + 100)
    button2.add(buttons)
    button2.add(allSprites)
    
    button3 = menuButton()
    button3.start("Extras", "EXTRAS")
    button3.rect.x  = (buttonColumnLeft)
    button3.rect.y = (buttonColumnTop + 200)
    button3.add(buttons)
    button3.add(allSprites)
    
    button4 = menuButton()
    button4.start("Exit", "QUIT")
    button4.rect.x  = (buttonColumnLeft)
    button4.rect.y = (buttonColumnTop + 300)
    button4.add(buttons)
    button4.add(allSprites)
    
    #add buttons to bottom layer
    allSprites.add(buttons, layer = 1)
    print "buttons created on layer 1"
    # draw them on screen and update
    #buttons.draw(screen)
    
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
    title1.rect.y = 60

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
    
    print ("main menu running........")
    
    while menuRunning:
        for event in pygame.event.get():
            if event.type == pl.QUIT or (event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE):
                menuRunning = False
                print("game closed from main menu")
                return 0
            if event.type == pl.MOUSEBUTTONDOWN and mouse.get_pressed()[0]:
                screen.blit(MENU_BACKGROUND, (0,0))
                buttons.update(event)
                allSprites.draw(screen)
                pygame.display.flip()
                '''
                This is where the button's destination kicks in
                Unfortunately, we have to check each button separately,
                as the pygame.sprite.Group.update() can't return sprites' .update()
                return values.
                What happens here:
                When the user clicks a button, all buttons are checked to see which one the mouse is on,
                then the destination is outputted to core.init, which then decides based on that where
                to go or what to do next.
                '''
                print("A button was clicked, checking which one it was")
                for button in buttons:
                    if button.getMouseOver():
                        return button.destination
            if event.type == pl.MOUSEMOTION:
                #update buttons for mouseover, we can afford to do it every time the mouse moves and reload all sprites
                screen.blit(MENU_BACKGROUND, (0,0))
                buttons.update(event)
                allSprites.draw(screen)
                pygame.display.flip()
            clock.tick(GAME_FPS)
            #we update twice, so that the button doesn't freeze after pressing         
            screen.blit(MENU_BACKGROUND, (0,0))  
            buttons.update(event)
            allSprites.draw(screen)
            pygame.display.flip()

    #clear the screen
    screen.blit(MENU_BACKGROUND, (0,0))
    pygame.display.flip()
    print "menu closing"

