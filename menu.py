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
        self.game.draw_text('→', 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Iniciar"
        self.startx, self.starty = self.mid_w, self.mid_h + 20
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 100
        self.exitx, self.exity = self.mid_w, self.mid_h + 140
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self): # Aparência do Menu
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK) #Preenchendo tela da cor preta
            self.game.draw_text('Menu Inicial', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
            self.game.draw_text("Jogar", 20, self.startx, self.starty)
            self.game.draw_text("Configurações", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Créditos", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Sair", 20, self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()
 
    def move_cursor(self): #Movimentação do Cursor (Setinha)
        if self.game.DOWN_KEY:#Usando ceta pra baixo
            if self.state == 'Iniciar':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Configurações'
            elif self.state == 'Configurações':
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
            elif self.state == 'Configurações':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Iniciar'
            elif self.state == 'Créditos':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Configurações'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Iniciar':
                self.game.playing = True
            elif self.state == 'Configurações':
                self.game.curr_menu = self.game.options
            elif self.state == 'Créditos':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Sair':
                self.game.exiting = True
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Configurações', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 130)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controles", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controles'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controles':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
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
            self.game.draw_text('Créditos', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 4 - 20)
            self.game.draw_text('KAIQUE SOUSA FARIAS', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('WEVERTON DE MELLO MACHADO', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('PEDRO DE OLIVEIRA MORAES', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('ANDREI DE SOUZA GOMES', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.blit_screen()