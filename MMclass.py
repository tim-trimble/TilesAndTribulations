#main Main
#chris Eilber
#final prodject



import pygame, sys
from pygame.locals import *
from Button_Class import simpleButton
from MMINTERFACE import interface
import random
pygame.init()

class mainMenu(object):
    def __init__(self, surf):

        self.DisplaySurf = surf

        self.black = (0,0,0)
        self.tan = (190,182,15)


        self.displayWidth = int(surf.get_width())
        self.displayHeight = int(surf.get_height())

    #DisplaySurf = pygame.display.set_mode((displayWidth, displayHeight))
#DisplaySurf2 = rainbowBackground()

        self.DisplaySurf.fill(self.tan)
        pygame.display.set_caption('Main Menu')




        #self.B1 = simpleButton((self.displayHeight//15), (self.displayWidth//3),(0,0,0,0),self.black, 'Playgame', self.DisplaySurf, (self.displayWidth *.325,self.displayHeight*.3))
        #self.B2 = simpleButton((self.displayHeight//15), (self.displayWidth//3),(0,0,0,0),self.black, 'How To Play', self.DisplaySurf, (self.displayWidth *.325,self.displayHeight*.4))


    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, self.black)
        return self.textSurface, self.textSurface.get_rect()





    def displayText(self, txt):
        self.Text = pygame.font.Font('Triforce.ttf', int(self.displayHeight/10))
        self.TextSurf, self.TextRect = self.text_objects(txt,self.Text)
        self.TextRect.center = ((self.displayWidth/2), (self.displayHeight/10))
        self.DisplaySurf.blit(self.TextSurf,self.TextRect)


    def displayTile1(self):

        self.farms = pygame.image.load('Farms 2.png')
        self.imgpxX =int(self.displayWidth / 6)


        self.xbuffer = self.imgpxX/10
        self.border = self.imgpxX + 10
        self.buffer = self.xbuffer - 5
        self.T1= pygame.Surface((self.border, self.border))
        self.T1.fill(self.black)

        self.farms =pygame.transform.scale(self.farms, (self.imgpxX, self.imgpxX))
        self.mountainsrect = ((0 + self.xbuffer, self.displayHeight * (3 / 5) + self.xbuffer))
        self.borderrect = ((0 + self.buffer, self.displayHeight * (3 / 5) + self.buffer))
        self.DisplaySurf.blit(self.T1,(self.borderrect))
        self.DisplaySurf.blit(self.farms, (self.mountainsrect))

    def displayTile2(self):

        self.fields = pygame.image.load('fields.png')
        self.imgpxX =int(self.displayWidth / 6)

        self.xbuffer = self.imgpxX/10
        self.border = self.imgpxX + 10

        self.buffer = self.xbuffer - 5

        self.T1= pygame.Surface((self.border, self.border))
        self.fields =pygame.transform.scale(self.fields, (self.imgpxX, self.imgpxX))
        self.T1.fill(self.black)
        self.mountainsrect = (self.displayWidth * (1 / 5) + self.xbuffer, self.displayHeight * (3 / 5) + self.xbuffer)
        self.borderrect = (self.displayWidth * (1 / 5) + self.buffer, self.displayHeight * (3 / 5) + self.buffer)
        self.DisplaySurf.blit(self.T1,(self.borderrect))
        self.DisplaySurf.blit(self.fields, (self.mountainsrect))
    def displayTile3(self):
        self.lake = pygame.image.load('Lake 2.png')
        self.imgpxX =int(self.displayWidth / 6)


        self.xbuffer = self.imgpxX/10
        self.border = self.imgpxX + 10
        self.buffer = self.xbuffer - 5
        self.T1= pygame.Surface((self.border, self.border))
        self.T1.fill(self.black)


        self.lake =pygame.transform.scale(self.lake, (self.imgpxX, self.imgpxX))
        self.mountainsrect = (self.displayWidth * (2 / 5) + self.xbuffer, self.displayHeight * (3 / 5) + self.xbuffer)
        self.borderrect = (self.displayWidth * (2 / 5) + self.buffer, self.displayHeight * (3 / 5) + self.buffer)
        self.DisplaySurf.blit(self.T1,(self.borderrect))
        self.DisplaySurf.blit(self.lake, (self.mountainsrect))
    def displayTile4(self):
        self.mountains = pygame.image.load('Mountains 5.png')
        self.imgpxX =int(self.displayWidth / 6)

        self.xbuffer = self.imgpxX/10
        self.border = self.imgpxX + 10
        self.buffer = self.xbuffer - 5
        self.T1= pygame.Surface((self.border, self.border))
        self.T1.fill(self.black)

        self.mountains =pygame.transform.scale(self.mountains, (self.imgpxX, self.imgpxX))
        self.mountainsrect = (self.displayWidth * (3 / 5) + self.xbuffer, self.displayHeight * (3 / 5) + self.xbuffer)
        self.borderrect = (self.displayWidth * (3 / 5) + self.buffer, self.displayHeight * (3 / 5) + self.buffer)
        self.DisplaySurf.blit(self.T1,(self.borderrect))
        self.DisplaySurf.blit(self.mountains, (self.mountainsrect))
    def displayTile5(self):
        self.woods = pygame.image.load('Woods Tile 3.png')
        self.imgpxX =int(self.displayWidth / 6)


        self.xbuffer = self.imgpxX/10
        self.border = self.imgpxX + 10
        self.buffer = self.xbuffer - 5
        self.T1= pygame.Surface((self.border, self.border))
        self.T1.fill(self.black)

        self.woods =pygame.transform.scale(self.woods, (self.imgpxX,self.imgpxX))
        self.woodsrect = (self.displayWidth * (4 / 5) + self.xbuffer, self.displayHeight *(3/5) +self.xbuffer)
        self.borderrect = (self.displayWidth * (4 / 5) + self.buffer, self.displayHeight * (3 / 5) + self.buffer)
        self.DisplaySurf.blit(self.T1,(self.borderrect))
        self.DisplaySurf.blit(self.woods,(self.woodsrect))




    def display(self):

        self.DisplaySurf.fill((170, 176, 75))
        self.displayText('Tiles And Tribulations')
        self.displayTile1()
        self.displayTile2()
        self.displayTile3()
        self.displayTile4()
        self.displayTile5()








