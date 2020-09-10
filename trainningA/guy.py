import pygame

class Guy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/jogadorTeste.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self, *args):
        #LOGICA!
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 1
        elif keys[pygame.K_DOWN]:
            self.rect.y += 1
        elif keys[pygame.K_UP]:
            self.rect.y -= 1

