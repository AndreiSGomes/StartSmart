import pygame, sys
from pygame.locals import *

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 130, 130)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('▶', 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Iniciar"
        self.startx, self.starty = self.mid_w, self.mid_h
        self.tutorialx, self.tutorialy = self.mid_w, self.mid_h + 40
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 80
        self.exitx, self.exity = self.mid_w, self.mid_h + 120
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self): # Aparência do Menu
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK) #Preenchendo tela da cor preta
            self.game.draw_text('Menu Inicial', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 8)
            self.game.draw_text("Recorde Atual: ", 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 4)
            self.game.draw_text("Jogar", 20, self.startx, self.starty)
            self.game.draw_text("Como Jogar?", 20, self.tutorialx, self.tutorialy)
            self.game.draw_text("Créditos", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Sair", 20, self.exitx, self.exity)
            self.game.draw_text("Voltar: Backspace", 10, self.mid_w - 200, self.mid_h + 190)
            self.game.draw_text("Avançar: Enter", 10, self.mid_w + 200, self.mid_h + 190)
            self.draw_cursor()
            self.blit_screen()
 
    def move_cursor(self): #Movimentação do Cursor (Setinha)
        if self.game.DOWN_KEY:#Usando ceta pra baixo
            if self.state == 'Iniciar':
                self.cursor_rect.midtop = (self.tutorialx + self.offset, self.tutorialy)
                self.state = 'Como Jogar?'
            elif self.state == 'Como Jogar?':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Créditos'
            elif self.state == 'Créditos':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Sair'
            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Iniciar'
        elif self.game.UP_KEY: #Usando ceta pra cima
            if self.state == 'Iniciar':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Sair'
            elif self.state == 'Sair':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Créditos'
            elif self.state == 'Como Jogar?':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Iniciar'
            elif self.state == 'Créditos':
                self.cursor_rect.midtop = (self.tutorialx + self.offset, self.tutorialy)
                self.state = 'Como Jogar?'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Iniciar':
                self.game.playing = True
            elif self.state == 'Como Jogar?':
                self.game.curr_menu = self.game.options
            elif self.state == 'Créditos':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Sair':
                self.game.exiting = sys.exit()
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.arrowx, self.arrowy = self.mid_w, self.mid_h + 0
        self.rightx, self.righty = self.mid_w, self.mid_h + 60
        self.leftx, self.lefty = self.mid_w, self.mid_h + 90
        self.shotx, self.shoty = self.mid_w, self.mid_h + 120
        self.shotz, self.shoth = self.mid_w, self.mid_h + 150
           
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Tutorial', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)
            self.game.draw_text("Teclado", 30, self.arrowx, self.arrowy)
            self.game.draw_text("Andar para Direira:  →", 15, self.rightx, self.righty)
            self.game.draw_text("Andar para Esquerda: ←", 15, self.leftx, self.lefty)
            self.game.draw_text("Disparar Cura:  F", 15, self.shotx, self.shoty)
            self.game.draw_text("Pular:  Barra de Espaço", 15, self.shotz, self.shoth)
            self.game.draw_text("Voltar: Backspace", 10, self.mid_w - 200, self.mid_h + 190)
            self.game.draw_text("Avançar: Enter", 10, self.mid_w + 200, self.mid_h + 190)
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('CRIADORES DE WAR C-19', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 4 - 20)
            self.game.draw_text('KAIQUE SOUSA FARIAS', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('WEVERTON DE MELLO MACHADO', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('PEDRO DE OLIVEIRA MORAES', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('ANDREI DE SOUZA GOMES', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.game.draw_text("Voltar: Backspace", 10, self.mid_w-200, self.mid_h + 190)
            self.game.draw_text("Avançar: Enter", 10, self.mid_w+200, self.mid_h + 190)
            self.blit_screen()