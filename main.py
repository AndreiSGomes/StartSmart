import math, random, sys, os
import pygame



# # #  CONFIGURAÇÕES DE TELA ------------------------------------------------------------------
larguraTela, alturaTela = 1000, 500
metadeLargura = larguraTela / 2
metadeAltura = alturaTela / 2
areaTela = larguraTela * alturaTela
tela = pygame.display.set_mode((larguraTela, alturaTela))
bg = pygame.image.load("Cenario/cenario.png").convert()
background = pygame.transform.scale(bg, (larguraTela, alturaTela))
pygame.display.set_caption("War C-19")

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)


# # # TEMPORIZADOR ----------------------------------------------------------------------------
timer = 0
tempo_segundo = 0

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (66, 50)


# # # PERSONAGEM ---------------------------------------------------------------------------------
left = [pygame.image.load(os.path.join('Personagens', 'Tras1.png')),
        pygame.image.load(os.path.join('Personagens', 'Tras2.png')),
        pygame.image.load(os.path.join('Personagens', 'Tras3.png')),
        pygame.image.load(os.path.join('Personagens', 'Tras4.png'))
        ]
right = [pygame.image.load(os.path.join('Personagens', 'Frente1.png')),
         pygame.image.load(os.path.join('Personagens', 'Frente2.png')),
         pygame.image.load(os.path.join('Personagens', 'Frente3.png')),
         pygame.image.load(os.path.join('Personagens', 'Frente4.png'))
         ]

x = 100
y = 395
radius = 80
vel = 5
move_left = False
move_right = False
stepIndex = 0

class Hero:
    def __init__(self, x, y):
        #walk
        self.x = x
        self.y = y
        self.velx = 5
        self.vely = 15
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        # Jump
        self.jump = False

    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= larguraTela - radius:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw(self, tela):
        if self.stepIndex >= 16:
            self.stepIndex = 0
        if self.face_left:
            tela.blit(left[self.stepIndex//4], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            tela.blit(right[self.stepIndex//4], (self.x, self.y))
            self.stepIndex += 1

    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*2
            self.vely -= 1
        if self.vely < -15:
            self.jump = False
            self.vely = 15

# INIMIGO ----------------------------------------------------------------------------------------
left_enemy = [pygame.image.load(os.path.join('Inimigos', 'T1.png')),
              pygame.image.load(os.path.join('Inimigos', 'T2.png')),
              pygame.image.load(os.path.join('Inimigos', 'T3.png')),
              pygame.image.load(os.path.join('Inimigos', 'T4.png'))
              ]
right_enemy = [pygame.image.load(os.path.join('Inimigos', 'F1.png')),
               pygame.image.load(os.path.join('Inimigos', 'F2.png')),
               pygame.image.load(os.path.join('Inimigos', 'F3.png')),
               pygame.image.load(os.path.join('Inimigos', 'F4.png'))
               ]



class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.stepIndex = 0

    def step(self):
        if self.stepIndex >= 32:
            self.stepIndex = 0

    def draw(self, tela):
        self.step()
        if self.direction == left:
            tela.blit(left_enemy[self.stepIndex//8], (self.x, self.y))
        if self.direction == right:
            tela.blit(right_enemy[self.stepIndex // 8], (self.x, self.y))
        self.stepIndex += 1

    def move(self):
        if self.direction == left:
            self.x -= 2
        if self.direction == right:
            self.x += 2

    def off_screen(self):
        return not(self.x >= -80 and self.x <= larguraTela + 30)



# # # FUNÇÃO TELA ------------------------------------------------------------------------------
def draw_game():
    tela.fill(BLACK)
    tela.blit(background, (0, 0))
    player.draw(tela)
    for enemy in enemies:
        enemy.draw(tela)
    # TEMPORIZADOR
    tela.blit(texto, pos_texto)
    #ATUALIZAÇÃO DA TELA
    pygame.display.update()
    CLOCK.tick(FPS)

# INSTÂNCIA INIMIGO/PERSONAGEM
player = Hero(250, 410)
enemies = []


# # # MUSICA -----------------------------------------------------------------------------------
pygame.mixer.music.load('Musicas/Wandering-the-Streets_Looping.mp3')
pygame.mixer.music.play()
pygame.event.wait()



# # # LOOP ------------------------------------------------------------------------
run = True
while run:

    # # # FECHAR TELA ------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Input
    userInput = pygame.key.get_pressed()

    # Movement
    player.move_hero(userInput)
    player.jump_motion(userInput)

    # Draw game in windows
    draw_game()

# # # CONTROLE INIMIGOS
    if len(enemies) == 0:
        rand_nr = random.randint(0, 1)
        if rand_nr == 1:
            enemy = Enemy(1010, 407, left)
            enemies.append(enemy)
        if rand_nr == 0:
            enemy = Enemy(-10, 407, right)
            enemies.append(enemy)
    for enemy in enemies:
        enemy.move()
        if enemy.off_screen():
            enemies.remove(enemy)

# # # TEMPORIZADOR
    if (timer <20): #tempo
        timer += 1
    else: #tempo
        tempo_segundo +=1 #tempo
        texto = font.render("Tempo: " +str(tempo_segundo), True, (255, 0, 255), (1, 1,500))   #tempo

        timer = 0 #tempo



