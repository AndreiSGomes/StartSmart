import math, random, sys
import pygame
from mapa import Cenario
from jogadores import Jogador, carregarImagem
from pygame.locals import *

#Musica
import pygame # importei o pygame
pygame.init() # iniciando o pygame
pygame.mixer.music.load('sounds/Wandering-the-Streets_Looping.mp3')
pygame.mixer.music.play()
#Musica /


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
cenarioJogo = Cenario("cena.png")
cenarioJogo_group = pygame.sprite.Group()
cenarioJogo_group.add(cenarioJogo)
fundo_velocidade = 0

timer = 0 #tempo
tempo_segundo = 0#tempo

# # # PERSONAGEM -----------------------------------------------------------------------------------

parado = carregarImagem("parado", 1)
andandoFrente = carregarImagem("frente", 4)
andandoTras = carregarImagem("tras", 4)

personagem = Jogador(318, 408, parado)
velocidadePersonagemY = 10
personagem_group = pygame.sprite.Group()
personagem_group.add(personagem)

font = pygame.font.SysFont('arial black', 30) #tempo
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0)) #tempo
pos_texto = texto.get_rect() #tempo
pos_texto.center = (66, 50) #tempo



# # # MOVIMENTAÇÃO ----------------------------------------------------------------
while True:
    #pygame.time.delay(50)

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

        if (timer <20): #tempo
            timer += 1
        else: #tempo
	        tempo_segundo +=1 #tempo
	        texto = font.render("Tempo: " +str(tempo_segundo), True, (255, 0, 255), (1, 1,500))   #tempo

	        timer = 0 #tempo




# # # ROLAGEM DO CENÁRIO ------------------------------------------------------------------


    tela.fill(BLACK)

    cenarioJogo_group.draw(tela)      # DESENHAR PLANO DE FUNDO DO JOGO
    personagem_group.draw(tela)       # DESENHAR PERSONAGEM
    tela.blit(texto, pos_texto)  # tempo

    cenarioJogo.update()
    personagem.update()

    pygame.display.flip()
    CLOCK.tick(FPS)
