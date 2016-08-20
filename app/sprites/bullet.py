import os
import pygame

from app.sprites.enemy.enemy import Enemy
from app.scene.platformScreen.collisionPlayerPlatform import *
# from app.tool.animation import Animation


class Bullet(Enemy):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('img', 'Bullet.png'))

        self.name = "bullet"

        self.imageBulletRight = list()
        self.imageBulletRight.append(pygame.image.load(os.path.join('img', 'Bullet.png')))

        self.imageBulletLeft = list()
        self.imageBulletLeft.append(pygame.image.load(os.path.join('img', 'Bullet.png')))

        self.image = self.imageBulletRight[0]

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height/2

        if direction == RIGHT:
            self.speedx = 10
            self.image = self.imageBulletRight[0]
            self.imageBulletList = self.imageBulletRight
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.image = self.imageBulletLeft[0]
            self.imageBulletList = self.imageBulletLeft
            self.rect.x = x - self.rect.width
        self.speedy = 0

        # self.animation = Animation(self.image, {RIGHT: self.imageBulletRight, LEFT: self.imageBulletLeft})

        self.friendly = friendly

    def update(self):
        self.rect.x += self.speedx
        # self.animation.update(self)

class HeartBullet(Bullet):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('img', 'HeartBullet.png'))

        self.name = "bullet"

        self.image = pygame.image.load(os.path.join('img', 'HeartBullet.png'))

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height / 2

        if direction == RIGHT:
            self.speedx = 10
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.rect.x = x - self.rect.width
        self.speedy = 0

        self.friendly = friendly

class BeerBullet(Bullet):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('img', 'biere32x32.png'))

        self.name = "bullet"

        self.image = pygame.image.load(os.path.join('img', 'biere32x32.png'))

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height / 2

        if direction == RIGHT:
            self.speedx = 10
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.rect.x = x - self.rect.width
        self.speedy = 0

        self.friendly = friendly

class SpiritBullet(Bullet):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('img', 'biere32x32.png'))

        self.name = "bullet"

        self.image = pygame.image.load(os.path.join('img', 'BulletBlue.png'))

        self.direction = direction


        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height / 2

        if direction == RIGHT:
            self.speedx = 10
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.rect.x = x - self.rect.width
        self.speedy = 0

        self.friendly = friendly