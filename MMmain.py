# MMmain.py
# TIM TRIMBLE, CHRIS ELBER
# SPRING 2016

import pygame, sys
from pygame.locals import *
from MMclass import mainMenu
from HowtoPlayClass import howtoplay
from MMINTERFACE import  interface

def MMmain():
    pygame.init()
    displayWidth = 1200
    displayHeight = 600

    DisplaySurf = pygame.display.set_mode((displayWidth, displayHeight))

    tan = (190,182,15)

    DisplaySurf.fill((0,0,0))
    pygame.display.set_caption('Main Menu')
    mainmenu = mainMenu(DisplaySurf)
    info = howtoplay(DisplaySurf)

    IFACE = interface(DisplaySurf)

    IFACE.all_buttons_inactive()
    IFACE.BUTTON_LIST[0].active = True
    IFACE.BUTTON_LIST[1].active = True
    IFACE.MMSCREEN = True
    IFACE.HTPSCREEN = False
    IFACE.GAMESCREEN = False
    MENU = True
    while MENU == True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


                elif event.type == MOUSEBUTTONDOWN:
                    mouseXY = pygame.mouse.get_pos()
                    if IFACE.BUTTON_LIST[0].clicked(mouseXY):
                        print('B1 HIT')
                        IFACE.BUTTON_LIST[0].hilighted = True
                    elif IFACE.BUTTON_LIST[1].clicked(mouseXY):
                        print('B2 HIT')
                        IFACE.BUTTON_LIST[1].hilighted = True # was orignally BLIST[0]
                    elif IFACE.BUTTON_LIST[2].clicked(mouseXY):
                        print('back')
                        IFACE.BUTTON_LIST[2].hilighted = True

                elif event.type == MOUSEBUTTONUP:
                    if IFACE.BUTTON_LIST[0].clicked(mouseXY):
                        IFACE.BUTTON_LIST[0].hilighted = False
                        IFACE.MMSCREEN = False
                        IFACE.HTPSCREEN = False
                        IFACE.GAMESCREEN = True
                    ##sets the vairaible to true that goes to the gameplay


                #Button 2
                    elif IFACE.BUTTON_LIST[1].clicked(mouseXY):
                        IFACE.BUTTON_LIST[1].hilighted = False
                        IFACE.back_button_on()
                        IFACE.MMSCREEN = False
                        IFACE.HTPSCREEN = True


                    elif IFACE.BUTTON_LIST[2].clicked(mouseXY):
                        IFACE.BUTTON_LIST[2].hilighted = False
                        IFACE.play_button_on()
                        IFACE.MMSCREEN = True
                        IFACE.HTPSCREEN = False

                if IFACE.MMSCREEN:

                    mainmenu.display()
                    IFACE.display()

                elif IFACE.HTPSCREEN:
                    info.display()
                    IFACE.display()

                elif IFACE.GAMESCREEN:
                    MENU = False

                pygame.display.update()