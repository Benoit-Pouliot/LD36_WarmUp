import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.screenData = data
        self.updateFeedMenuPlease = False
        self.recreateFeedMenuPlease = False
        self.recreatePetMenuPlease = False

        self.canEvolve = True

        self.winningCondition = None

        #Sound
        self.soundLvlUp = pygame.mixer.Sound('music_pcm/LvlUp.wav')
        self.soundLvlUpFail = pygame.mixer.Sound('music_pcm/LvlUpFail.wav')


    def logicHandle(self):
        self.screenData.messageLog.updateText()
        self.screenData.allSprites.update()

    # Get rabbit back
    def getRabbit(self):
        self.screenData.messageLog.newText()
        self.screenData.messageLog.textList.append('You killed your critter.')
        self.updatePet('rabbit')

    def getTiger(self):
        self.canEvolve = True
        self.screenData.messageLog.newText()
        self.checkInventory('cupcake')
        self.checkInventory('goldBar')
        if self.canEvolve:
            self.screenData.messageLog.textList.append('You killed your critter.')
            self.updatePet('tiger')

    def getUnicorn(self):
        self.canEvolve = True
        self.screenData.messageLog.newText()
        self.checkInventory('cupcake')
        self.checkInventory('goldBar')
        self.checkInventory('apple')
        self.checkInventory('horseshoe')
        if self.canEvolve:
            self.screenData.messageLog.textList.append('You killed your critter.')
            self.updatePet('unicorn')

    def updatePet(self, nextPet):
        self.screenData.allSprites.remove(self.gameData.myPet)

        self.gameData.myPet = self.screenData.petTypeList.pet[nextPet]
        self.gameData.myPet.loadImage()
        self.screenData.messageLog.textList.append('You got a ' + self.gameData.myPet.name + '!')
        if self.gameData.myPet.eventTrigger:
            self.checkTrigger()
        self.screenData.allSprites.add(self.gameData.myPet)

        # need to recreate pat menu
        if self.gameData.petList.pet[nextPet].kind == KEY_ANIMAL:
            if self.gameData.petList.pet[nextPet].found == False:
                self.recreatePetMenuPlease = True

        self.gameData.petList.pet[nextPet].found = True

        self.checkIfAllPetFound()


        if self.gameData.myPet.kind == DEAD_END:
            self.screenData.messageLog.textList.append('This critter won\'t take anything else from you.')
        elif self.gameData.myPet.kind == KEY_ANIMAL:
                self.screenData.messageLog.textList.append('What a cool new pet. Keep going!')
        elif self.gameData.myPet.kind == WINNER:
            self.screenData.messageLog.textList.append('Congratulation! You got your dragon!')
            self.winningCondition = WIN_SCREEN

    def checkIfAllPetFound(self):
        numberPetFound = 0
        for pet in self.gameData.petList.pet:
            if self.gameData.petList.pet[pet].found:
                numberPetFound += 1
        if numberPetFound == len(self.gameData.petList.pet):
            self.winningCondition = FOUND_ALL_PET_SCREEN

    def giveCupcake(self):
        self.give(self.gameData.itemInfoList.item["cupcake"].key)

    def giveGoldBar(self):
        self.give(self.gameData.itemInfoList.item["goldBar"].key)

    def giveHorseshoe(self):
        self.give(self.gameData.itemInfoList.item["horseshoe"].key)

    def giveBone(self):
        self.give(self.gameData.itemInfoList.item["bone"].key)

    def giveCarrot(self):
        self.give(self.gameData.itemInfoList.item["carrot"].key)

    def giveApple(self):
        self.give(self.gameData.itemInfoList.item["apple"].key)

    def giveGun(self):
        self.give(self.gameData.itemInfoList.item["gun"].key)

    def givePokerChip(self):
        self.give(self.gameData.itemInfoList.item["pokerChip"].key)

    def giveTotem(self):
        self.give(self.gameData.itemInfoList.item["totem"].key)


    def give(self, givenItem):
        self.screenData.messageLog.newText()
        self.canEvolve = True
        self.checkInventory(givenItem)

        if self.canEvolve:
            updateHappened = False
            for link in self.gameData.itemInfoList.item[givenItem].linkList:
                if self.gameData.myPet.key == link[0]:
                    self.soundLvlUp.play(0)
                    self.updatePet(link[1])
                    updateHappened = True
                    break
            if updateHappened == False:
                self.nothingHappened()

    def checkInventory(self,item):
        if self.gameData.itemInfoList.item[item].inventory == 0:
            self.screenData.messageLog.textList.append(
                'You have no ' + self.gameData.itemInfoList.item[item].name + ' left. Go get some!')
            self.canEvolve = False

        elif self.gameData.itemInfoList.item[item].inventory > 0:
            self.gameData.itemInfoList.item[item].inventory += -1
            self.updateFeedMenuPlease = True

    def nothingHappened(self):
        self.soundLvlUpFail.play(0)
        self.screenData.messageLog.textList.append('Nothing happened.')
        if self.gameData.myPet.kind == DEAD_END:
            self.screenData.messageLog.textList.append('This critter won\'t take anything else from you.')
        elif self.gameData.myPet.kind == NORMAL:
            self.screenData.messageLog.textList.append('Try something else or find more items.')

    def checkTrigger(self):
        if self.gameData.myPet.key == 'dog':
            self.obtain('carrot')
        if self.gameData.myPet.key == 'alienRabbit':
            self.obtain('apple')
        if self.gameData.myPet.key == 'chocoRabbit':
            self.unlockMap('map2')
        if self.gameData.myPet.key == 'muscularHorse':
            self.unlockMap('map3')
        if self.gameData.myPet.key == 'pimpUnicorn':
            self.unlockMap('map4')

    def obtain(self,key):
        if self.gameData.itemInfoList.item[key].unlock == False:
            self.gameData.itemInfoList.item[key].unlock = True
            self.recreateFeedMenuPlease = True
        numberOfItem = 4
        self.gameData.itemInfoList.item[key].inventory += numberOfItem
        self.screenData.messageLog.textList.append('He brings you ' + str(numberOfItem) + (' ') + self.gameData.itemInfoList.item[key].name + 's!')
        self.updateFeedMenuPlease = True

    def unlockMap(self,map):
        if self.gameData.mapUnlock[map] == False:
            self.gameData.mapUnlock[map] = True
        if map == 'map2':
            self.screenData.messageLog.textList.append('That much gold is enough to buy your way into the desert.')
        if map == 'map3':
            self.screenData.messageLog.textList.append('Your ' + self.gameData.myPet.name + ' wants to go someplace nice. Visit the saloon.')
        if map == 'map4':
            self.screenData.messageLog.textList.append('The indian are impressed by your ' + self.gameData.myPet.name + '. Pay them a visit.')


