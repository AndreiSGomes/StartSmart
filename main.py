import math, random, sys
import pygame
from mapa import Cenario
from jogadores import Jogador, carregarImagem
from pygame.locals import *


# # #  CONFIGURAÇÕES DE TELA ---------------------------------------------
larguraTela, alturaTela = 800, 600
metadeLargura = larguraTela / 2
metadeAltura = alturaTela / 2
areaTela = larguraTela * alturaTela
tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("War C-19")

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)




# # # CENÁRIO ----------------------------------------------------------------------------------
cenarioJogo = Cenario("cena2.png")
cenarioJogo_group = pygame.sprite.Group()
cenarioJogo_group.add(cenarioJogo)
fundo_velocidade = 0


# # # PERSONAGEM -----------------------------------------------------------------------------------

parado = carregarImagem("parado", 1)
andandoFrente = carregarImagem("frente", 4)
andandoTras = carregarImagem("tras", 4)

personagem = Jogador(100, 408, parado)
velocidadePersonagemY = 10
personagem_group = pygame.sprite.Group()
personagem_group.add(personagem)



# # # MOVIMENTAÇÃO ----------------------------------------------------------------
while True:

    # # # FECHAR TELA ------------------------------------------------------------
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # # # CONTROLES ---------------------------------------------------------------
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                fundo_velocidade += -4
                cenarioJogo.velocidadeFundo(fundo_velocidade)
                personagem.mudarImagem(andandoFrente)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                fundo_velocidade = 0
                cenarioJogo.velocidadeFundo(fundo_velocidade)
                personagem.mudarImagem(parado)
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                fundo_velocidade += 4
                cenarioJogo.velocidadeFundo(fundo_velocidade)
                personagem.mudarImagem(andandoTras)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                fundo_velocidade = 0
                cenarioJogo.velocidadeFundo(fundo_velocidade)
                personagem.mudarImagem(parado)




# # # ROLAGEM DO CENÁRIO ------------------------------------------------------------------


    tela.fill(BLACK)

    cenarioJogo_group.draw(tela)      # DESENHAR PLANO DE FUNDO DO JOGO
    personagem_group.draw(tela)       # DESENHAR PERSONAGEM


    cenarioJogo.update()
    personagem.update()

    pygame.display.flip()
    CLOCK.tick(FPS)
