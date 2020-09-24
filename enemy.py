import pygame
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/redEnemy.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.timer = 0

    def update(self,*args):
        self.timer += 0.001

        self.rect.x = 250 + math.sin(self.timer) *200
