import pygame

class Cenario(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.fundo = pygame.image.load("data/%s"% image)
        self.image = self.fundo
        self.rect = self.image.get_rect()
        self.vel_fundo = 0

    def velocidadeFundo(self, valor):
        self.vel_fundo = valor

    def update(self):
        self.rect.move_ip(self.vel_fundo, 0)
        if self.rect.right <= 790:
            self.rect.right = 2400
        if self.rect.left >= 0:
            self.rect.right = 2000



