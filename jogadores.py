import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self, jogadorEixoX, jogadorEixoY, animacao):
        super().__init__()
        self.jogadorEixoX = jogadorEixoX
        self.jogadorEixoY = jogadorEixoY
        self.animacao = animacao
        self.animacaoAtual = 0
        self.image = self.animacao[self.animacaoAtual].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.jogadorEixoX, self.jogadorEixoY]

    def mudarImagem(self, image):
        self.animacao = image

    def update(self):
        self.animacaoAtual += 0.3
        if self.animacaoAtual >= len(self.animacao):
            self.animacaoAtual = 0
        self.image = self.animacao[int(self.animacaoAtual)]


def carregarImagem(nome, valor):
    image = []
    for i in range(1, valor + 1):
        image.append(pygame.image.load("data/person/%s (%d).png" % (nome, i)))
    return image