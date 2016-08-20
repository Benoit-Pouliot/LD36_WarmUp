import pygame
from sys import exit

class EventHandlerPetScreen():
    def __init__(self):
        self.menuPause = None
        # Default selector
        self.hPos = 0

    def eventHandle(self,optionList,selectorList):
        self.optionList = optionList
        self.selectorList = selectorList

        self.hMax = len(self.selectorList)
        self.selector = self.selectorList[self.hPos]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.menuPause.mainLoop()
                elif event.key == pygame.K_ESCAPE:
                    self.menuPause.mainLoop()
                elif event.key == pygame.K_RIGHT:
                    self.optionList[self.hPos][self.selector.vPos].deselect()
                    if self.hPos < self.hMax-1:
                        self.hPos += 1
                    elif self.hPos == self.hMax-1:
                        self.hPos = 0
                    self.selector = self.selectorList[self.hPos]
                    self.optionList[self.hPos][self.selector.vPos].select()
                elif event.key == pygame.K_LEFT:
                    self.optionList[self.hPos][self.selector.vPos].deselect()
                    if self.hPos > 0:
                        self.hPos += -1
                    elif self.hPos == 0:
                        self.hPos = self.hMax - 1
                    self.selector = self.selectorList[self.hPos]
                    self.optionList[self.hPos][self.selector.vPos].select()
                elif event.key == pygame.K_UP:
                    self.optionList[self.hPos][self.selector.vPos].deselect()
                    self.selector.moveUp()
                    self.optionList[self.hPos][self.selector.vPos].select()
                elif event.key == pygame.K_DOWN:
                    self.optionList[self.hPos][self.selector.vPos].deselect()
                    self.selector.moveDown()
                    self.optionList[self.hPos][self.selector.vPos].select()
                elif event.key == pygame.K_SPACE:
                    self.optionList[self.hPos][self.selector.vPos].doOption()
                elif event.key == pygame.K_RETURN:
                    self.optionList[self.hPos][self.selector.vPos].doOption()
