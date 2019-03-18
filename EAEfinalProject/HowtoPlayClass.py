#how to play class
import pygame, sys
from pygame.locals import *

from Button_Class import simpleButton
import random
pygame.init()

class howtoplay(object):

    def __init__(self, surf):
        self.DisplaySurf = surf
        self.BGCOLOR = (190, 200, 135)
        self.black = (0,0,0)
        self.white = (255,255,255)


        self.displayWidth = int(surf.get_width())
        self.displayHeight = int(surf.get_height())

        self.DisplaySurf.fill(self.BGCOLOR)
        pygame.display.set_caption('How To Play')

        self.imagex = int(self.displayWidth *.666)
        self.imagey = self.displayHeight
        self.textx = self.displayWidth-(self.displayWidth/3)
        self.liney = 0
        self.WIDTH = 40
        self.HEIGHT = 40
        self.__RADIUS = self.HEIGHT//2

        self.__1= pygame.Surface((self.WIDTH, self.HEIGHT),flags=SRCALPHA, depth = 32)
        self.__1.fill((0,0,0,0))
        self.__2= pygame.Surface((self.WIDTH, self.HEIGHT),flags=SRCALPHA, depth = 32)
        self.__2.fill((0,0,0,0))
        self.__3= pygame.Surface((self.WIDTH, self.HEIGHT),flags=SRCALPHA, depth = 32)
        self.__3.fill((0,0,0,0))
        self.__4= pygame.Surface((self.WIDTH, self.HEIGHT),flags=SRCALPHA, depth = 32)
        self.__4.fill((0,0,0,0))
        self.__5= pygame.Surface((self.WIDTH, self.HEIGHT),flags=SRCALPHA, depth = 32)
        self.__5.fill((0,0,0,0))
        #FLAGS
        tutorial = False


        #self.B1 = simpleButton((self.displayHeight//15), (self.displayWidth//6),(0,0,0,0),self.black, 'Back', self.DisplaySurf, (self.displayWidth *.325,self.displayHeight*.3))
    def drawgameboard(self):
        self.gameboard = pygame.image.load('gameboard.png')
        self.gameboard = pygame.transform.scale(self.gameboard,(self.imagex,self.imagey))

        self.DisplaySurf.blit(self.gameboard,(0,0))

    def textsurf(self):
        Font = pygame.font.Font('anirm.ttf', int(self.displayHeight/38))
        self.L1 = Font.render('The goal of this game is simple', True, self.black)
        self.L2 = Font.render('Collect your players treasure', True, self.black)
        self.L3 = Font.render('And return it to your staring tile.', True, self.black)
        self.L4 = Font.render('The challenge of this game comes', True, self.black)
        self.L5 = Font.render('From the randomly generated board:', True, self.black)
        self.L6 = Font.render('The starting, treasure and,', True, self.black)
        self.L7 = Font.render('Terrain tiles are all randomly', True, self.black)
        self.L8 = Font.render('Generated.', True, self.black)
        self.L9 = Font.render('1.This displays your current roll', True, self.black)
        self.L10 = Font.render('2.This is the action button,', True, self.black)
        self.L11 = Font.render('After choosing to move you roll', True, self.black)
        self.L12 = Font.render('The dice, and you can click on a ', True, self.black)
        self.L13 = Font.render('Tile to move if you have the correct', True, self.black)
        self.L14 = Font.render('Roll.', True, self.black)
        self.L15 = Font.render("3.Displays who's turn it is.", True, self.black)
        self.L16 = Font.render('4.Shows what type of tile the', True, self.black)
        self.L17 = Font.render('Player is on.', True, self.black)
        self.L18 = Font.render('5.Shows the player what roll is', True, self.black)
        self.L19 = Font.render('Required to move from the tile', True, self.black)





        self.DisplaySurf.blit(self.L1,(self.textx, self.liney))
        self.DisplaySurf.blit(self.L2,(self.textx, self.liney+ 35))
        self.DisplaySurf.blit(self.L3,(self.textx, self.liney+ 70))
        self.DisplaySurf.blit(self.L4,(self.textx, self.liney+ 110))#
        self.DisplaySurf.blit(self.L5,(self.textx, self.liney+ 145))
        self.DisplaySurf.blit(self.L6,(self.textx, self.liney+ 180))
        self.DisplaySurf.blit(self.L7,(self.textx, self.liney+ 215))
        self.DisplaySurf.blit(self.L8,(self.textx, self.liney+ 250))
        self.DisplaySurf.blit(self.L9,(self.textx, self.liney+ 280))#
        self.DisplaySurf.blit(self.L10,(self.textx, self.liney+ 310))#
        self.DisplaySurf.blit(self.L11,(self.textx, self.liney+ 335))
        self.DisplaySurf.blit(self.L12,(self.textx, self.liney+ 360))
        self.DisplaySurf.blit(self.L13,(self.textx, self.liney+ 385))
        self.DisplaySurf.blit(self.L14,(self.textx, self.liney+ 410))
        self.DisplaySurf.blit(self.L15,(self.textx, self.liney+ 440))#
        self.DisplaySurf.blit(self.L16,(self.textx, self.liney+ 470))#
        self.DisplaySurf.blit(self.L17,(self.textx, self.liney+ 495))
        self.DisplaySurf.blit(self.L18,(self.textx, self.liney+ 525))#
        self.DisplaySurf.blit(self.L19,(self.textx, self.liney+ 550))


    def infocircles(self):
        Font = pygame.font.SysFont('Calibri', int(self.displayHeight/20))
        #Info 1
        self.info1 = Font.render('1', True, self.black)
        pygame.draw.circle(self.__1, self.black, (self.__RADIUS, self.__RADIUS),self.__RADIUS)
        pygame.draw.circle(self.__1, self.white, (self.__RADIUS, self.__RADIUS),self.__RADIUS -5)

        self.__1.blit(self.info1, (12, 2))

        self.DisplaySurf.blit(self.__1, (self.displayWidth* .4,self.displayHeight//6))
        #Info 2
        self.info2 = Font.render('2', True, self.black)
        pygame.draw.circle(self.__2, self.black, (self.__RADIUS, self.__RADIUS),self.__RADIUS)
        pygame.draw.circle(self.__2, self.white, (self.__RADIUS, self.__RADIUS),self.__RADIUS -5)

        self.__2.blit(self.info2, (12, 2))

        self.DisplaySurf.blit(self.__2, (self.displayWidth* .4,self.displayHeight*.4))
        #Info 3
        self.info3 = Font.render('3', True, self.black)
        pygame.draw.circle(self.__3, self.black, (self.__RADIUS, self.__RADIUS),self.__RADIUS)
        pygame.draw.circle(self.__3, self.white, (self.__RADIUS, self.__RADIUS),self.__RADIUS -5)

        self.__3.blit(self.info3, (12, 2))

        self.DisplaySurf.blit(self.__3, (self.displayWidth* .56,self.displayHeight*.55))
        #Info 4
        self.info4 = Font.render('4', True, self.black)
        pygame.draw.circle(self.__4, self.black, (self.__RADIUS, self.__RADIUS),self.__RADIUS)
        pygame.draw.circle(self.__4, self.white, (self.__RADIUS, self.__RADIUS),self.__RADIUS -5)

        self.__4.blit(self.info4, (12, 2))

        self.DisplaySurf.blit(self.__4, (self.displayWidth* .5,self.displayHeight*.67))
        #Info 5
        self.info5 = Font.render('5', True, self.black)
        pygame.draw.circle(self.__5, self.black, (self.__RADIUS, self.__RADIUS),self.__RADIUS)
        pygame.draw.circle(self.__5, self.white, (self.__RADIUS, self.__RADIUS),self.__RADIUS -5)

        self.__5.blit(self.info5, (12, 2))

        self.DisplaySurf.blit(self.__5, (self.displayWidth* .5,self.displayHeight*.85))



    def display(self):

        self.DisplaySurf.fill(self.BGCOLOR)
        self.drawgameboard()
        self.textsurf()
        self.infocircles()




