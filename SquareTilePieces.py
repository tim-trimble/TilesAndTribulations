# SquareTilePieces.py
# TIM TRIMBLE
# SPRING 2016

import pygame, sys
from pygame.locals import*


class SquareTile(object):

    def __init__(self, size, imagefile, tiletype, tilepos, surf, gridpos):
        # Variable Set Up
        self.SIZE = size
        self.IMAGE = pygame.image.load(imagefile)
        self.TYPE = tiletype
        self.POS = tilepos
        self.SURF = surf
        self.TILESURF = pygame.Surface((self.SIZE, self.SIZE), flags=SRCALPHA, depth=32)
        self.HIDDEN = True
        self.ACTIVE = False
        # Thi is to help test if Player is within moving distance
        self.CENTER = (self.SIZE//2, self.SIZE//2)
        self.GRIDPOS = gridpos

    def drawtile(self):
        black = (0, 0, 0)
        # Checking for Hidden
        if self.HIDDEN == True:
            self.TILESURF.fill(black)
        elif self.HIDDEN == False:
            
            if self.TYPE == 'MOUNTAIN':
                self.TILESURF.fill((50,50,50))
            elif self.TYPE == 'FARM':
                self.TILESURF.fill ((100,100,10))
            elif self.TYPE == 'FOREST':
                self.TILESURF.fill ((0, 150, 0))
            elif self.TYPE == 'LAKE':
                self.TILESURF.fill((0,0,100))
            elif self.TYPE == 'FLATLAND':
                self.TILESURF.fill((100,30,0))
            elif self.TYPE == 'TREASUREP1':
                self.TILESURF.fill((0,0,250))
            elif self.TYPE == 'TREASUREP2':
                self.TILESURF.fill((250,0,0))
            elif self.TYPE == 'START1' or self.TYPE == 'START2':
                self.TILESURF.fill((250,250,250))
            self.TILESURF.blit(self.IMAGE, (0, 0))
        # To help debug if this should become and error
        else:
            print("TILE HIDDEN ERROR")

        self.SURF.blit(self.TILESURF,self.POS)

    def canmove(self, dicevalue):
        # Testing type, all types must be ALL CAPS
        if self.TYPE == 'MOUNTAIN':
            if dicevalue == 7 or dicevalue == 8 or dicevalue == 6:
                canMove = True
            else:
                canMove = False
        elif self.TYPE == 'FARM':
            if dicevalue <= 7:
                canMove = True
            else:
                canMove = False
        elif self.TYPE == 'FOREST':
            if dicevalue >= 8:
                canMove = True
            else:
                canMove = False
        elif self.TYPE == 'LAKE':
            if dicevalue == 2 or dicevalue == 3 or dicevalue == 11 or dicevalue == 12:
                canMove = True
            else:
                canMove = False
        elif self.TYPE == 'FLATLAND':
            if dicevalue >=4:
                canMove = True
            else:
                canMove = False
        elif self.TYPE == 'TREASUREP1' or self.TYPE == 'TREASUREP2' or self.TYPE == 'START1' or self.TYPE == 'START2':
            canMove = True
        else:
            print('Tile Type Eror')

        return canMove

    def isClicked(self, mousexy):
        yesORno = False
        P1 = self.POS
        P2 = (self.SIZE+self.POS[0],self.SIZE+self.POS[1])
        yesORno = (self.ACTIVE and P1[0] <= mousexy[0] <= P2[0] and P1[1] <= mousexy[1] <= P2[1])
        return yesORno
