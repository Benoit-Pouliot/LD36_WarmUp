from app.settings import *

#To initialize my pet
import os
import pygame
from app.sprites.pet.petList import PetList
from app.sprites.item.itemInfoList import ItemInfoList


# All the global data for the game and player
class GameData:
    def __init__(self, scene=None):

        #Item info list
        #Go see ItemInfo class in sprite to look at lock, and inventory
        self.itemInfoList = ItemInfoList()

        #Was map unlocked?
        self.mapUnlock = {}
        self.mapUnlock["map1"] = True
        self.mapUnlock["map2"] = False
        self.mapUnlock["map3"] = False
        self.mapUnlock["map4"] = False

        #My pet: rabbit at first
        self.petList = PetList()
        self.myPet = self.petList.pet['rabbit']
        self.petList.pet[self.myPet.key].found = True
        self.myPet.loadImage()

        self.maxItemOfAType = 99


        self.scene = scene
        self.showFoundAllPet = True  # We want to show foundAllPetScreen only once.

        self.mapData = None

    # When u pick up  and item, add it to the item list
    def registerItemPickedUp(self, item):
        if item.imageName in self.itemInfoList.item:
            numberOfItem = self.itemInfoList.item[item.imageName].inventory
            self.itemInfoList.item[item.imageName].inventory = min(numberOfItem+1, self.maxItemOfAType)
            self.itemInfoList.item[item.imageName].unlock = True
