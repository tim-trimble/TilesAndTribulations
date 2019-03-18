# PlayerPieceClass.py
# TIM TRIMBLE
# SPRING 2016

import pygame, sys
from pygame.locals import *


class PlayerPiece(object):

    def __init__(self, color, size, imagefile, startingpiece):
        self.LOCATION = startingpiece
        self.COLOR = color
        self.SIZE = size
        self.IMAGE = pygame.image.load(imagefile)
        self.IMAGE = pygame.transform.scale(self.IMAGE,(40,40))
        self.HASTREASURE = False

    def DrawPlayer(self, pos):
        playersurf = pygame.Surface((self.SIZE, self.SIZE), flags=SRCALPHA, depth=32)
        playersurf.blit(self.IMAGE, (0, 0))
        #pygame.draw.circle(playersurf, (100,0,100),(10,10), 10)
        self.LOCATION.TILESURF.blit(playersurf, pos)


