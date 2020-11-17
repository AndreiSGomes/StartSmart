import pygame

pygame.init()

w = 1152
h = 648
win = pygame.display.set_mode((w, h))
game = True

lr = [[118, 597], []]

itens = pygame.image.load("character/Frame Character 1 - No Mask.png")
#janela, imagem, posição(frente, altura) TELA (500,150) Comprimento
def maske_blit(win, img, wx, wy, x, y, w, h):
    surf = pygame.Surface((w, h)).convert()
    surf.blit(img, (0, 0), (wx, wy, w, h))
    alpha = surf.get_at((0, 0)) 
    surf.set_colorkey(alpha)
    win.blit(surf, (x, y))


while game:

    maske_blit(win, itens, 118, 42, 500, 150, 259, 411)

    pygame.display.flip()

    win.fill((255, 255, 255))


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False 
