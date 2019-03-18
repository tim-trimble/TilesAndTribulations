##DIECLASS
##TIM TRIMBLE
##SPRING 2015

import pygame
from pygame.locals import*
from random import randint

class Die(object):

    def __init__(self,size,surf,pos):

        self.SURF = surf
        self.POS = pos
        self.SIZE = size
        TRANP = (0,0,0,0)

        self.DIESURF = pygame.Surface((self.SIZE,self.SIZE) ,flags=SRCALPHA, depth=32)
        self.DIESURF.fill(TRANP)

        self.DIERED = (250,0,0)
        self.TCOLOR = (0,0,0)

        self.DIEHILIGHT = (84,6,90)


        self.RAD = self.SIZE//10
        HSIZE = self.SIZE//2

        self.THEIGHT = int(self.SIZE*.7)

        self.Value = 1

        self.TEXT = randint(0,5)

        self.hilighted = False

    def setRandValue(self):
        self.Value = randint(1,6)

    def clicked(self,MOUSEXY):
        yesORno = False
        P1 = self.POS
        P2 = (P1[0]+self.SIZE,P1[1]+self.SIZE)
        yesORno = (P1[0] <= MOUSEXY[0] <= P2[0] and P1[1] <= MOUSEXY[1] <= P2[1])
        return yesORno

    def hilight(self,mouse):
        if self.clicked(mouse):
            if self.hilighted == True:
                self.hilighted = False
            elif self.hilighted == False:
                self.hilighted = True
    def __drawDIE(self):
        if self.hilighted:
            pygame.draw.circle(self.DIESURF,self.DIEHILIGHT,(self.RAD,self.RAD),self.RAD)
            pygame.draw.circle(self.DIESURF,self.DIEHILIGHT,(self.RAD,self.SIZE-self.RAD),self.RAD)
            pygame.draw.circle(self.DIESURF,self.DIEHILIGHT,(self.SIZE-self.RAD,self.RAD),self.RAD)
            pygame.draw.circle(self.DIESURF,self.DIEHILIGHT,(self.SIZE-self.RAD,self.SIZE-self.RAD),self.RAD)

            pygame.draw.rect(self.DIESURF,self.DIEHILIGHT, ((0,self.RAD),(self.SIZE,(self.SIZE-2*self.RAD))))
            pygame.draw.rect(self.DIESURF,self.DIEHILIGHT, ((self.RAD,0),(self.SIZE-2*self.RAD,self.SIZE)))

        else:
            pygame.draw.circle(self.DIESURF,self.DIERED,(self.RAD,self.RAD),self.RAD)
            pygame.draw.circle(self.DIESURF,self.DIERED,(self.RAD,self.SIZE-self.RAD),self.RAD)
            pygame.draw.circle(self.DIESURF,self.DIERED,(self.SIZE-self.RAD,self.RAD),self.RAD)
            pygame.draw.circle(self.DIESURF,self.DIERED,(self.SIZE-self.RAD,self.SIZE-self.RAD),self.RAD)

            pygame.draw.rect(self.DIESURF,self.DIERED, ((0,self.RAD),(self.SIZE,(self.SIZE-2*self.RAD))))
            pygame.draw.rect(self.DIESURF,self.DIERED, ((self.RAD,0),(self.SIZE-2*self.RAD,self.SIZE)))


        DIEFONT = pygame.font.SysFont("anirm.ttf", self.THEIGHT//2)
        if self.Value == 1:
            self.TEXTSURF = DIEFONT.render('I',True,self.TCOLOR,None)
            Dievalue = 1
        elif self.Value == 2:
            self.TEXTSURF = DIEFONT.render('II',True,self.TCOLOR,None)
            Dievalue = 2
        elif self.Value == 3:
            self.TEXTSURF = DIEFONT.render('III',True,self.TCOLOR,None)
            Dievalue = 3
        elif self.Value == 4:
            self.TEXTSURF = DIEFONT.render('IV',True,self.TCOLOR,None)
            Dievalue =4
        elif self.Value == 5:
            self.TEXTSURF = DIEFONT.render('V',True,self.TCOLOR,None)
            Dievalue = 5
        elif self.Value == 6:
            self.TEXTSURF = DIEFONT.render('VI',True,self.TCOLOR,None)
            Dievalue = 6


        w, h = self.TEXTSURF.get_size()

        self.XPOS = (self.SIZE-w)//2
        self.YPOS = int((self.SIZE-h)//2)



        self.PIP = self.DIESURF.blit(self.TEXTSURF, (self.XPOS,self.YPOS))
        return Dievalue


    def displayDie(self):
        self.__drawDIE()
        self.SURF.blit(self.DIESURF,self.POS)


        

    

    
