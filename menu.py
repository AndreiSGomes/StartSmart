#Bibliotecas importadas
import os
import pygame
import pygame_menu

pygame.init() # Iniciar o programa
os.environ['SDL_VIDEO_CENTERED'] = '1' # Centralizador de Janela
surface = pygame.display.set_mode((800, 400)) #Tamanho da Janela
pygame.display.set_caption('WAR C-19') #Nome do jogo na janela



def start_the_game():
    print('Jogo Iniciado')
    


menu = pygame_menu.Menu(height=400,
                        width=800,
                        theme=pygame_menu.themes.THEME_GREEN,
                        onclose=pygame_menu.events.EXIT,
                        title='Vamos acabar com o COVID!')

menu.add_text_input('Nome: ', default='StartSmart') #Nome de Usuário
menu.add_button('Iniciar', start_the_game) # Iniciar o jogo
menu.add_button('Sair', pygame_menu.events.EXIT) # Botão de sair com o ESC e o Botão de fechar da interface do jogo.

if __name__ == '__main__':
    menu.mainloop(surface)