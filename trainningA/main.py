import pygame
from guy import Guy
from enemy import Enemy


pygame.init()  # inicializando o pygame
display = pygame.display.set_mode([850, 600])  # criar uma janela [x,y] tamanho da janela
pygame.display.set_caption("MyGame")  # legenda na janela


# Objects
objectGroup = pygame.sprite.Group()

guy = Guy(objectGroup)
personEnemy = Enemy(objectGroup)
personEnemy.rect.center = [200, 400]
personEnemy2 = Enemy(objectGroup)

gameLoop = True
if __name__ == "__main__":
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False


        # Object Update:
        objectGroup.update()


        # Draw:
        display.fill([56, 56, 56])  # preencher cor na tela
        objectGroup.draw(display)

        pygame.display.update()  # atualização da janela
