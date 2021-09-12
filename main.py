from game import Game #Pegando o arquivo game e importando a classe Game

g = Game() #facilitar toda a bagaça!

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

pygame.quit()