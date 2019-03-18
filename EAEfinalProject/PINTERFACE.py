# PINTERFACE.py
# TIM TRIMBLE
# SPRING 2016

import pygame, sys
from pygame.locals import *


class Pinterface(object):

    def __init__(self, piecelist):
        self.PLIST = piecelist
        self.CLICKED = False

    def pfaceUP(self, mousexy, player):
        for piece in self.PLIST:
            if piece.isClicked(mousexy):
                print('piece clicked: ', piece.GRIDPOS)
                player.LOCATION = piece
                self.CLICKED = True
        return self.CLICKED

