# Tiles_and_Tribulations.py
# TIM TRIMBLE
# SPRING 2016


import pygame, sys
from pygame.locals import *
from PlayerPieceClass import PlayerPiece
from Button_Class import simpleButton
from SquareTilePieces import SquareTile
from PINTERFACE import Pinterface
from BINTERFACE import bInterface
from random import randint

def GAMEmain():

    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((750, 450))
    DISPLAYSURF.fill((170,176,75))
    pygame.display.set_caption('Tiles and Tribulations')

    lengthgrid = 25 # determines how many pieces there are
    GRIDLIST = []
    poslist = []
    gridposlist = []

    # BUTTONS
    MoveButton = simpleButton(60 , 200,(100,0,100),(0,0,0),'MOVE',DISPLAYSURF,(500,150))
    RollButton = simpleButton(60, 200,(100,0,100),(0,0,0),'ROLL',DISPLAYSURF,(500,150))
    EndTurnButon = simpleButton(60, 200, (100,0,100), (0,0,0),'END',DISPLAYSURF,(500,150))
    BLIST = [MoveButton, RollButton, EndTurnButon]

    binterface = bInterface(BLIST)
    pinterface = Pinterface(GRIDLIST)
    # TYLE TYPES (according to grid size)
    temp_type_list = ['FARM','FARM','FARM','FARM','FARM','MOUNTAIN','MOUNTAIN','MOUNTAIN','MOUNTAIN','FOREST','FOREST',
                   'FOREST','FOREST','LAKE','LAKE', 'FLATLAND','FLATLAND','FLATLAND','FLATLAND','FLATLAND','FLATLAND',
                   'TREASUREP1', 'TREASUREP2', 'START1', 'START2']
    type_list = []
    for t in temp_type_list:
        type_list.insert(randint(0,len(type_list)),t) # randomizes the grid

    for x in range(5):
        for y in range(5):
            poslist.append((10+y*75+10*y,10+x*75+10*x)) # Creates the positions for the Grid

    for x in range(5):
        for y in range(5):
            gridposlist.append((x,y)) #creatues the Grid Pos variable


    for x in range(lengthgrid):
        GRIDLIST.append(SquareTile(75,type_list[x]+".png", type_list[x],poslist[x],DISPLAYSURF, gridposlist[x])) # makes the list of Grid pieces
    #[TandT] D:\School\University of Utah\Spring 2016\EAE 1410\TandT\Final_Game\Tiles_and_Tribulations.py
    # Finds the starting player pieces
    start1 = 0
    start2 = 0
    for p in GRIDLIST:
        if p.TYPE == 'START1':
            start1 = GRIDLIST.index(p)
        if p.TYPE == 'START2':
            start2 = GRIDLIST.index(p)

    # sets up players
    player1 = PlayerPiece('red', 100, 'RED.png',GRIDLIST[start1])
    player2 = PlayerPiece('blue', 100, 'BLUE.png', GRIDLIST[start2])
    playerturn = 1
    playerlist = [0, player1, player2]
    PlayGame = True
    diceValue = 2
    HasMoved = True


    pygame.mixer.init()
    pygame.mixer.music.load('bgmusic.mp3')
    pygame.mixer.music.play(-1)
    while PlayGame == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            CanMove = False
            if event.type == MOUSEBUTTONDOWN:
                mousexy = pygame.mouse.get_pos()
                HasMoved = binterface.ifaceDown(mousexy)

            elif event.type == MOUSEBUTTONUP:
                playerturn = binterface.ifaceUP(mousexy)
                diceValue = binterface.scoreDice()
                CanMove = playerlist[playerturn].LOCATION.canmove(diceValue)
                if CanMove:
                    if HasMoved == False:
                        binterface.WhereCanMove(GRIDLIST, playerlist[playerturn])
                        HasMoved = pinterface.pfaceUP(mousexy, playerlist[playerturn])
                        if HasMoved == True:
                            binterface.HASMOVED = True
                            pinterface.CLICKED = False
            DISPLAYSURF.fill((170,176,75))

            for p in GRIDLIST:
                if p == player1.LOCATION or p == player2.LOCATION:
                    p.HIDDEN = False
                p.drawtile()
            player1.DrawPlayer((0,5))
            player2.DrawPlayer((35,30))
            for p in GRIDLIST:
                DISPLAYSURF.blit(p.TILESURF, p.POS)
            binterface.DisplayDiceandButtons(DISPLAYSURF, (500,10))

            if player1.LOCATION.TYPE == 'TREASUREP1':
                player1.HASTREASURE = True
            if player2.LOCATION.TYPE == 'TREASUREP2':
                player2.HASTREASURE = True

            if player1.HASTREASURE == True and player1.LOCATION.TYPE == 'START1':
                PlayGame = False
                winningPlayer = 'Player 1'
            if player2.HASTREASURE == True and player2.LOCATION.TYPE == 'START2':
                PlayGame = False
                winningPlayer = 'Player 2'

            binterface.TextScore(diceValue, playerlist[playerturn].LOCATION.TYPE, DISPLAYSURF, (450,120), (450, 300))
            GAMEFONT = pygame.font.SysFont('timesnewroman.ttf', 36)
            PLAYERTURNFONT = GAMEFONT.render('Player '+str(playerturn)+"'s turn",True, (0,0,0), None)
            DISPLAYSURF.blit(PLAYERTURNFONT, (450, 250))

            pygame.display.update()


    else:

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if winningPlayer == 'Player 1':
                end_image = pygame.image.load('END_SCREEN_RED.png')
            elif winningPlayer == 'Player 2':
                end_image = pygame.image.load('END_SCREEN_BLUE.png')
            DISPLAYSURF.blit(end_image,(0,0))
            FONT = pygame.font.SysFont('anirm.ttf',48)
            FONTSURF = FONT.render('TREASURE COLLECTED: ', True, (0, 0, 0), None)
            FONTSURF2 = FONT.render('PLAYER '+str(winningPlayer)+' WINS!', True, (0,0,0), None)
            pygame.draw.rect(DISPLAYSURF,(170,176,75),((35,45),(420,75)))
            DISPLAYSURF.blit(FONTSURF, (40,50))
            DISPLAYSURF.blit(FONTSURF2, (50, 80))

            pygame.display.update()


if __name__ == '__main__':
    GAMEmain()

