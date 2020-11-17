import pygame #Biblioteca pygame
from menu import * #pegando o arquivo Menu / o uso de "*" aparentemente é para incluir tudo
from pygame.locals import* #
from sys import exit
from random import randint # Números aleatórios / Números entre X e Y
import math, random, sys, os

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("War C-19")
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 720, 480 # Tamanho da tela
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'fonte/PressStart2P-vaV7.ttf'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255) #Definindo cores
        self.main_menu = MainMenu(self) #Classes
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.draw_text('Obrigado por Jogar', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            #ÁREA DE ADICIONAR JOGO
            pygame.init() # Iniciando o Pygame

            preto = (0, 0, 0) # Cores para facilitar
            branco = (255, 255, 255)

            screen = pygame.display.set_mode((890, 550), 0, 32)

            # define o titulo da janela
            pygame.display.set_caption("Duck Hunt - PyGame")

            # variáveis que armazenarão a posicao em que o mouse se encontra
            x_pos = 0
            y_pos = 0

            # variáveis que armazenarão a posicao em que um clique no mouse foi efetuado
            x_clique = 0
            y_clique = 0

            # variáveis que armazenarão a posicao em que o pato se encontra
            x_duck = 0
            y_duck = randint(0, 450)

            pontos = 0
            velocidade = 2
            errou = False

            # inicia o player
            pygame.mixer.init(44100, -16, 2, 1024)

            # configura o volume da música
            pygame.mixer.music.set_volume(0.8)

            while True:
                for event in pygame.event.get():
                    # se ele capturar um evento de fechar a tela (clicar no botao "X" no topo da janela), o programa é fechado
                    if event.type == QUIT:
                        exit()
                    elif event.type == MOUSEMOTION:
                        x_pos, y_pos = pygame.mouse.get_pos()
                    elif event.type == MOUSEBUTTONDOWN:
                        x_clique, y_clique = pygame.mouse.get_pos()

                posicao = (x_pos - 50, y_pos - 50)

                x_duck += 1

                if x_duck * velocidade > 890 and not errou:
                    x_duck = 0
                    y_duck = randint(0, 450)

                    # errou, toca a música do game over
                    pygame.mixer.music.load("gameover.mp3")
                    pygame.mixer.music.play()

                    errou = True

                # colore o fundo de preto, deve sempre vir antes de desenharmos os objetos, no caso o circulo, pois se nao, tudo vai ficar preto!
                screen.fill(preto)
                pygame.mouse.set_visible(False)

                # o blit do background deve vir anter do blit da mira, pois assim o background sera desenhado
                # primeiro e a mira depois, ficando o background atras da mira e nao o contrario!
                screen.blit(pygame.image.load("background.png"), (0, 0))
                screen.blit(pygame.font.SysFont("tahoma", 72).render("Pontos: " + str(pontos), True, branco), (500, 450))

                # para serem contabilizados pontos, a posicao do clique deve estar mais ou menos onde o pato esta exatamente,
                # por conta desse mais ou menos usamos a funcao range
                if x_clique in range(x_duck * velocidade - 30, x_duck * velocidade + 30) and y_clique in range(y_duck - 30, y_duck + 30):
                    # acertou, toca a musica do acerto
                    pygame.mixer.music.load("hit.mp3")
                    pygame.mixer.music.play()

                    pontos += 1
                    velocidade += 1
                    x_duck = 0
                    y_duck = randint(50, 500)

                screen.blit(pygame.image.load("greenduck.gif"), (x_duck * velocidade, y_duck))

                if errou:
                    x_duck = -50
                    y_duck = -50
                    screen.blit(pygame.image.load("dog.gif"), (400, 340))

                screen.blit(pygame.image.load("mira.gif").convert(), posicao)

                pygame.display.update()
                #FINAL


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ): #Cor da letra, tamanho
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)