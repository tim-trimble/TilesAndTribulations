# BINTERFACE.py
# TIM TRIMBLE
# SPRING 2016

import pygame, sys
from pygame.locals import *
from Die_Class import Die

class bInterface(object):

    def __init__(self, blist):
        self.BLIST = blist
        self.BLIST[0].active = True
        self.BLIST[1].active = False
        self.BLIST[2].active = False
        self.DIESURF = pygame.Surface((210, 100), flags=SRCALPHA, depth=32)
        Dice1 = Die(100, self.DIESURF, (0, 0))
        Dice2 = Die(100, self.DIESURF ,(105, 0))
        self.DLIST = [Dice1, Dice2]
        self.PLAYERTURN = 1
        self.HASMOVED = True

    def ifaceDown(self,mousexy): # for when mouse is clicked down
        if self.BLIST[0].clicked(mousexy):
            self.BLIST[0].hilighted = True
            self.HASMOVED = True
        elif self.BLIST[1].clicked(mousexy):
            self.BLIST[1].hilighted = True
            if self.BLIST[1].active == True:
                self.HASMOVED = False
        elif self.BLIST[2].clicked(mousexy):
            self.BLIST[2].hilighted = True
            self.HASMOVED = True
            self.HASMOVED = True
        return self.HASMOVED

    def ifaceUP(self, mousexy):  # This function uses a player input which has to change before being inputed into this function
        if self.BLIST[0].clicked(mousexy):
            self.BLIST[0].hilighted = False
            self.BLIST[0].active = False
            self.BLIST[1].active = True

        elif self.BLIST[1].clicked(mousexy):
            self.BLIST[1].hilighted = False
            self.RollDice()
            self.BLIST[1].active = False
            self.BLIST[2].active = True
        elif self.BLIST[2].clicked(mousexy):
            self.BLIST[2].hilighted = False
            self.BLIST[2].active = False
            self.BLIST[0].active = True
            if self.PLAYERTURN == 1:
                self.PLAYERTURN = 2
            elif self.PLAYERTURN == 2:
                self.PLAYERTURN = 1
        return  self.PLAYERTURN

    def DisplayDiceandButtons(self, surf, dpos,): # to keep the Main function small
        for b in self.BLIST:
            b.display()
        for d in self.DLIST:
            d.displayDie()
        surf.blit(self.DIESURF, dpos)

    def RollDice(self):
        for die in self.DLIST:
            die.setRandValue()

    def WhereCanMove(self, pList, player):
        for piece in pList:
            if ((abs(piece.GRIDPOS[0]-player.LOCATION.GRIDPOS[0]) == 1 and piece.GRIDPOS[1]-player.LOCATION.GRIDPOS[1] == 0) or
                (abs(piece.GRIDPOS[1]-player.LOCATION.GRIDPOS[1]) == 1 and piece.GRIDPOS[0]-player.LOCATION.GRIDPOS[0]==0)):
                piece.ACTIVE = True
            else:
                piece.ACTIVE = False

    def scoreDice(self):
        dvalue = self.DLIST[0].Value + self.DLIST[1].Value
        return dvalue

    def TextScore(self, diceScore, tiletype, surf, pos1, pos2):
        textFont1 = pygame.font.SysFont('timesnewroman.ttf', 36)
        textFont2 = pygame.font.SysFont('timesnewroman.ttf', 36)
        dice_score_font = textFont1.render('Dice Score: '+str(diceScore), True,(0,0,0),None)
        tile_font = textFont2.render(tiletype, True, (0,0,0), None)
        if tiletype == 'MOUNTAIN':
            roll = '6, 7, or 8'
        elif tiletype == 'FARM':
            roll = '7 or less'
        elif tiletype == 'FOREST':
            roll = '8 or greater'
        elif tiletype == 'LAKE':
            roll = '2, 3, 11, 12'
        elif tiletype == 'FLATLAND':
            roll = '4 or greater'
        elif tiletype == 'TREASUREP1' or tiletype == 'TREASUREP2' or tiletype == 'START1' or tiletype == 'START2':
            roll = 'anything'
        toMove = textFont2.render('Roll needed: '+roll, True, (0,0,0), None)
        surf.blit(dice_score_font, pos1)
        surf.blit(tile_font, pos2)
        surf.blit(toMove, (pos2[0], pos2[1] + 50))
