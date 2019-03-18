#BlackjackInterfaceClass
#Chris Eilber
#spring 16

import pygame, sys
from pygame.locals import *
from Button_Class import simpleButton

class interface(object):
    def __init__(self, surf):
        self.DisplaySurf = surf
        INFO = pygame.display.Info()
        self.displayWidth = INFO.current_w
        self.displayHeight = INFO.current_h

        #init colors
        BLACK = (0,0,0)
        GOLD =(255,215,0)


        BH = self.displayHeight // 10
        BW = self.displayWidth // 8

        #Need 3 buttons
        __PLAY_BUTTON = simpleButton((self.displayHeight//15), (self.displayWidth//3),(0,0,0,0),BLACK, 'Playgame', self.DisplaySurf, (self.displayWidth *.325,self.displayHeight*.3))
        __HOW_TO_PLAY = simpleButton((self.displayHeight//15), (self.displayWidth//3),(0,0,0,0),BLACK, 'How To Play', self.DisplaySurf, (self.displayWidth *.325,self.displayHeight*.4))
        __BACK_BUTTON = simpleButton((self.displayHeight // 15), (self.displayWidth // 6), (0, 0, 0, 0), BLACK, 'Back', self.DisplaySurf, (self.displayWidth //100, self.displayHeight //10))


        self.BUTTON_LIST =[__PLAY_BUTTON, __HOW_TO_PLAY, __BACK_BUTTON]

        #FLAGS
        self.MMSCREEN = True
        self.HTPSCREEN = False
        self.GAMESCREEN = False


    def all_buttons_inactive(self):
        for x in self.BUTTON_LIST:
            x.active = False

    def play_button_on(self):
        self.BUTTON_LIST[0].active = True
        self.BUTTON_LIST[1].active = True
        self.BUTTON_LIST[2].active = False

    def back_button_on(self):
        self.BUTTON_LIST[0].active = False
        self.BUTTON_LIST[1].active = False
        self.BUTTON_LIST[2].active = True

    def display_buttons(self):
        for x in self.BUTTON_LIST:
            x.display()

    def display(self):
        self.display_buttons()