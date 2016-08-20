# Imports
import os
import sys

import pygame

from app.menu.menu import Menu
from app.scene.titleScreen.eventHandlerTitleScreen import EventHandlerTitleScreen
from app.mapData import MapData
from app.settings import *
from app.scene.musicFactory import MusicFactory


class WinScreen:
    def __init__(self, screen, gameData=None):
        self.screen = screen

        self.gameData = gameData

        self.screen.fill((0,0,0))
        titleImage = pygame.image.load(os.path.join('img', 'winSceneBackground.png'))
        self.screen.blit(titleImage, (0, 0))

        self.type = WIN_SCREEN
        self.nextScene = None

        MusicFactory(TITLE_SCREEN)


    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandle() # EventHandle in THIS file, below
            # This would be in the logic
            self.draw()  # Drawer in THIS file, below

    def eventHandle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.goToPetScreen()
                elif event.key == pygame.K_RETURN:
                    self.goToPetScreen()

    def draw(self):
        pygame.display.flip()


    def goToPetScreen(self):
        self.nextScene = PET_SCREEN
        self.sceneRunning = False
        self.gameData.typeScene = PET_SCREEN
        self.gameData.mapData = None