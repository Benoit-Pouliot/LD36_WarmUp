import pygame
import os
from app.settings import *


#Objets
class OptionPetScreen(pygame.sprite.Sprite):
    def __init__(self,item,method):
        super().__init__()

        self.item = item

        self.optFont = pygame.font.SysFont(FONT_NAME, 24)
        self.number = self.item.inventory
        self.name = ' = ' + str(self.number)
        self.printedName = self.optFont.render(self.name, True, COLOR_MENU_FONTS)
        self.textPos = [0,0] #Par rapport au bouton

        self.image = pygame.Surface([1, 1])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.iconName = self.item.imageNamePNG
        self.icon = pygame.image.load(os.path.join('img', self.iconName))
        self.iconPos = [0,0]

        self.button = pygame.Rect(0,0,0,0)

        self.isSelected = False
        self.method = method
        self.soundSelect = pygame.mixer.Sound('music_pcm/menu_select.wav')
        self.soundSelect.set_volume(.3)
        self.soundChange = pygame.mixer.Sound('music_pcm/menu_change.wav')
        self.soundChange.set_volume(.3)

        #Color
        self.color1 = COLOR_MENU_1
        self.color2 = COLOR_MENU_2

    def update(self):
        self.name = ' = ' + str(self.number)

        if self.isSelected:
            self.color1 = COLOR_MENU_SELECT_1
            self.color2 = COLOR_MENU_SELECT_2
            self.printedName = self.optFont.render(self.name, True, COLOR_MENU_FONTS_SELECT)
        else:
            self.color1 = COLOR_MENU_1
            self.color2 = COLOR_MENU_2
            self.printedName = self.optFont.render(self.name, True, COLOR_MENU_FONTS)

        self.image.fill(self.color2)
        self.image.fill(self.color1,self.button)
        self.image.blit(self.icon, self.iconPos)
        self.image.blit(self.printedName,self.textPos)

    def scalingDim(self, height):
        self.imagePrintedWidth = self.icon.get_width() * height / self.icon.get_height()
        self.icon = pygame.transform.scale(self.icon, (int(self.imagePrintedWidth), int(height)))

    def select(self):
        self.isSelected = True
        self.soundChange.play(0)

    def deselect(self):
        self.isSelected = False

    def doOption(self):
        self.method()


