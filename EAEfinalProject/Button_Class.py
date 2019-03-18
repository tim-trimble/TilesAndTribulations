##Button_Class.py
##TIM TRIMBLE
##SPRING 2016

import pygame,sys
from pygame.locals import*

class simpleButton:

    def __init__(self,height,width,color,textColor,label,surf,position):
        ##VALUES
        self.__SURF = surf
        self.POS = position
        self.BUTCOLOR = color
        self.RIMCOLOR = [250,250,250]
        self.HIGHLIGHTCOLOR = (color[0]+((255-color[0])//3),
                               color[1]+((225-color[1])//3),
                               color[2]+((225-color[2])//3))

        self.HRIM = (self.HIGHLIGHTCOLOR[0]+((225-self.HIGHLIGHTCOLOR[0])//3),
                     self.HIGHLIGHTCOLOR[1]+((225-self.HIGHLIGHTCOLOR[1])//3),
                     self.HIGHLIGHTCOLOR[2]+((225-self.HIGHLIGHTCOLOR[2])//3))

        self.TEXTCOLOR = textColor

        self.HEIGHT = height
        self.WIDTH = width
        self.__RADIUS = self.HEIGHT//2
        THEIGHT = int(self.HEIGHT*.72)

        self.active = True
        self.hilighted = False

        BUTFONT = pygame.font.SysFont('anirm.ttf', 48)
        #Rendering surface

        self.TEXT__SURF = BUTFONT.render(label,True,textColor,None)

        w, h = self.TEXT__SURF.get_size()

        self.XPOS = (self.WIDTH-w)//2
        self.YPOS = int((self.HEIGHT-h))//2

        self.__BUTTON__SURF= pygame.Surface((self.WIDTH, self.HEIGHT),
                                            flags=SRCALPHA, depth = 32)
        self.__BUTTON__SURF.fill((0,0,0,0))


    def __buttonBG(self, color,color2):
        pygame.draw.circle(self.__BUTTON__SURF, color, (self.__RADIUS, self.__RADIUS),
                            self.__RADIUS)
        pygame.draw.circle(self.__BUTTON__SURF, color,
                           (self.WIDTH - self.__RADIUS, self.__RADIUS),self.__RADIUS)

        pygame.draw.rect(self.__BUTTON__SURF, color, Rect((self.__RADIUS, 0),
                                                          (self.WIDTH-2*self.__RADIUS,self.HEIGHT)))
        

        pygame.draw.circle(self.__BUTTON__SURF, color2, (self.__RADIUS, self.__RADIUS),
                           int(self.__RADIUS*.8))
        pygame.draw.circle(self.__BUTTON__SURF, color2, (self.WIDTH - self.__RADIUS, self.__RADIUS),
                           int(self.__RADIUS*.8))
        pygame.draw.rect(self.__BUTTON__SURF, color2, Rect((int(self.__RADIUS*.8),int(self.__RADIUS*.2)),
                                                                  (self.WIDTH-2*self.__RADIUS,int(2*self.__RADIUS*.8))))
        

    def __buttonText(self):
        self.__BUTTON__SURF.blit(self.TEXT__SURF, (self.XPOS, self.YPOS))

    def clicked(self, MOUSEXY):

        yesORno=False
        P1 = self.POS
        P2 = (P1[0]+self.WIDTH,P1[1]+self.HEIGHT)
        yesORno = (self.active and P1[0] <= MOUSEXY[0] <= P2[0] and
                   P1[1] <= MOUSEXY[1] <= P2[1])
        return yesORno

    def display(self):

        if self.active:
            if self.hilighted:
                self.__buttonBG(self.HIGHLIGHTCOLOR,self.HRIM)
                self.__buttonText()
                self.__SURF.blit(self.__BUTTON__SURF,self.POS)
            else:
                self.__buttonBG(self.BUTCOLOR,self.RIMCOLOR)
                self.__buttonText()
                self.__SURF.blit(self.__BUTTON__SURF, self.POS)
                





        
                
                   






        
