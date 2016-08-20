from app.settings import *
from app.scene.worldMap.worldMap import WorldMap
from app.scene.titleScreen.titleScreen import TitleScreen
from app.scene.petScreen.petScreen import PetScreen
from app.scene.winScreen import WinScreen
from app.scene.foundAllPetScreen import FoundAllPetScreen

from app.scene.platformScreen.platformScreen import PlatformScreen
from app.gameData import GameData


class SceneHandler:
    def __init__(self, screen, firstScene=None):

        self.handlerRunning = True
        self.runningScene = firstScene
        self.screen = screen
        self.gameData = GameData(firstScene)


    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.runningScene.mainLoop()

            #When we exit the scene, this code executes
            if self.runningScene.nextScene == TITLE_SCREEN:
                self.runningScene = TitleScreen(self.screen, self.gameData)
            elif self.runningScene.nextScene == WORLD_MAP:
                self.runningScene = WorldMap(self.screen, self.gameData)
            elif self.runningScene.nextScene == PET_SCREEN:
                self.runningScene = PetScreen(self.screen, self.gameData)
            elif self.runningScene.nextScene == WIN_SCREEN:
                self.runningScene = WinScreen(self.screen, self.gameData)
            elif self.runningScene.nextScene == FOUND_ALL_PET_SCREEN:
                self.runningScene = FoundAllPetScreen(self.screen, self.gameData)
            elif self.runningScene.nextScene == PLATFORM_SCREEN:
                self.runningScene = PlatformScreen(self.screen, self.gameData)

