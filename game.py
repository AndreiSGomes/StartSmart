import pygame #Biblioteca pygame
from menu import * #pegando o arquivo Menu / o uso de "*" aparentemente é para incluir tudo
from pygame.locals import* #
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
#INICIO
            # # #  CONFIGURAÇÕES DE TELA ------------------------------------------------------------------
            larguraTela, alturaTela = 1000, 500
            metadeLargura = larguraTela / 2
            metadeAltura = alturaTela / 2
            areaTela = larguraTela * alturaTela
            tela = pygame.display.set_mode((larguraTela, alturaTela))
            bg = pygame.image.load("Cenario/cenario.gif")
            background = pygame.transform.scale(bg, (larguraTela, alturaTela))
            pygame.display.set_caption("War C-19")

            pygame.init()
            CLOCK = pygame.time.Clock()
            FPS = 45
            BLACK = (0, 0, 0)

            # # # MUSICA -----------------------------------------------------------------------------------
            pygame.mixer.music.load('Musicas/start.wav')
            pygame.mixer.music.play(-1)

            # # # PERSONAGEM ---------------------------------------------------------------------------------
            scale_hero=[100,100] 
            left = [pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Tras1.png')),(scale_hero)),
                    pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Tras2.png')),(scale_hero)),
                    pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Tras3.png')),(scale_hero)),
                    pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Tras4.png')),(scale_hero))
                    ]
            right = [pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Frente1.png')),(scale_hero)),
                     pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Frente2.png')),(scale_hero)),
                     pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Frente3.png')),(scale_hero)),
                     pygame.transform.scale(pygame.image.load(os.path.join('Personagens', 'Frente4.png')),(scale_hero))
                     ]
            bullet_img = pygame.transform.scale(pygame.image.load(os.path.join('Bullets', 'bullet.png')), (10, 10))
            x = 100
            y = 395
            radius = 80
            vel = 5
            move_left = False
            move_right = False
            stepIndex = 0

            class Hero:
                def __init__(self, x, y):
                    # walk
                    self.x = x
                    self.y = y
                    self.velx = 6
                    self.vely = 15
                    self.face_right = True
                    self.face_left = False
                    self.stepIndex = 0
                    # Jump
                    self.jump = False
                    # Bullet
                    self.bullets = []
                    self.cool_down_count = 0
                    # Health
                    self.hitbox = (self.x, self.y, 64, 64)
                    self.health = 40
                    self.lives = 1
                    self.alive = True

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
                    self.hitbox = (self.x, self.y, 78, 90)
                    pygame.draw.rect(tela, (255, 0, 0), (self.x + 30, self.y - 10, 40, 10))
                    if self.health >= 0:
                        pygame.draw.rect(tela, (0, 255, 0), (self.x + 30, self.y - 10, self.health, 10))
                    if self.stepIndex >= 16:
                        self.stepIndex = 0
                    if self.face_left:
                        tela.blit(left[self.stepIndex // 4], (self.x, self.y))
                        self.stepIndex += 1
                    if self.face_right:
                        tela.blit(right[self.stepIndex // 4], (self.x, self.y))
                        self.stepIndex += 1

                def jump_motion(self, userInput):
                    if userInput[pygame.K_SPACE] and self.jump is False:
                        jumpvar = pygame.mixer.Sound('Musicas/jump.wav')
                        jumpvar.play()
                        self.jump = True
                    if self.jump:
                        self.y -= self.vely * 2
                        self.vely -= 1
                    if self.vely < -15:
                        self.jump = False
                        self.vely = 15

                def direction(self):
                    if self.face_right:
                        return 1
                    if self.face_left:
                        return -1

                def cooldown(self):
                    if self.cool_down_count >= 20:
                        self.cool_down_count = 0
                    elif self.cool_down_count > 0:
                        self.cool_down_count += 1

                def shoot(self):
                    self.hit()
                    self.cooldown()
                    if (userInput[pygame.K_f] and self.cool_down_count == 0):
                        shootvar=pygame.mixer.Sound('Musicas/shot.wav')
                        shootvar.play()
                        bullet = Bullet(self.x, self.y, self.direction())
                        self.bullets.append(bullet)
                        self.cool_down_count = 1
                    for bullet in self.bullets:
                        bullet.move()
                        if bullet.off_screen():
                            self.bullets.remove(bullet)

                def hit(self):
                    for enemy in enemies:
                        for bullet in self.bullets:
                            if enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[
                                1] < bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
                                enemy.health -= 25
                                player.bullets.remove(bullet)

            class Bullet:
                def __init__(self, x, y, direction):
                    self.x = x + 70
                    self.y = y + 30
                    self.direction = direction

                def draw_bullet(self):
                    tela.blit(bullet_img, (self.x, self.y))

                def move(self):
                    if self.direction == 1:
                        self.x += 15
                    if self.direction == -1:
                        self.x -= 15

                def off_screen(self):
                    return not (self.x >= 0 and self.x <= larguraTela)

            # INIMIGO ----------------------------------------------------------------------------------------
            scale_enimy=[100,100]
            left_enemy = [pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'T1.png')),(scale_enimy)),
                          pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'T2.png')),(scale_enimy)),
                          pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'T3.png')),(scale_enimy)),
                          pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'T4.png')),(scale_enimy))
                          ]
            right_enemy = [pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'F1.png')),(scale_enimy)),
                           pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'F2.png')),(scale_enimy)),
                           pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'F3.png')),(scale_enimy)),
                           pygame.transform.scale(pygame.image.load(os.path.join('Inimigos', 'F4.png')),(scale_enimy))
                           ]

            class Enemy:
                def __init__(self, x, y, direction):
                    self.x = x
                    self.y = y
                    self.direction = direction
                    self.stepIndex = 0
                    # Health
                    self.hitbox = (self.x, self.y, 64, 64)
                    self.health = 40

                def step(self):
                    if self.stepIndex >= 32:
                        self.stepIndex = 0

                def draw(self, tela):
                    self.hitbox = (self.x, self.y, 78, 90)
                    pygame.draw.rect(tela, (255, 0, 0), (self.x + 20, self.y - 10, 40, 10))
                    if self.health >= 0:
                        pygame.draw.rect(tela, (0, 255, 0), (self.x + 20, self.y - 10, self.health, 10))
                    self.step()
                    if self.direction == left:
                        tela.blit(left_enemy[self.stepIndex // 8], (self.x, self.y))
                    if self.direction == right:
                        tela.blit(right_enemy[self.stepIndex // 8], (self.x, self.y))
                    self.stepIndex += 1

                def move(self):
                    self.hit()
                    if self.direction == left:
                        self.x -= 10
                    if self.direction == right:
                        self.x += 9

                def hit(self):
                    if player.hitbox[0] < enemy.x + 32 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < enemy.y + 32 < player.hitbox[1] + player.hitbox[3]:
                        if player.health > 0:
                            player.health -= 1
                            if player.health == 0 and player.lives > 0:
                                player.lives -= 1
                                player.health = 40
                            elif player.health == 0 and player.lives == 0:
                                player.alive = False

                def off_screen(self):
                    return not (self.x >= -80 and self.x <= larguraTela + 30)

            # # # FUNÇÃO TELA ------------------------------------------------------------------------------
            def draw_game():
                tela.fill(BLACK)
                tela.blit(background, (0, 0))
                # Draw Player
                player.draw(tela)
                # Draw Bullets
                for bullet in player.bullets:
                    bullet.draw_bullet()
                # Draw Enemies
                for enemy in enemies:
                    enemy.draw(tela)
                # Player Health
                if player.alive == False:
                    tela.fill((0, 0, 0))
                    font = pygame.font.Font('fonte/PressStart2P-vaV7.ttf', 32)
                    text = font.render('GAME OVER! precione R', True, (138, 47, 47))
                    textRect = text.get_rect()
                    textRect.center = (metadeLargura, metadeAltura)
                    tela.blit(text, textRect)
                    if userInput[pygame.K_r]:
                        player.alive = True
                        player.lives = 1
                        player.health = 40
                font = pygame.font.Font('fonte/PressStart2P-vaV7.ttf', 27)
                text = font.render('Curados: ' + str(kills) + '  Vidas: ' + str(player.lives), True, (189, 178, 209))
                tela.blit(text, (230, 20))

                pygame.display.update()
                CLOCK.tick(FPS)

            player = Hero(250, 410)
            enemies = []
            kills = 0

            # # # LOOP ------------------------------------------------------------------------
            run = True
            while run:

                # # # FECHAR TELA ------------------------------------------------------------
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                # Input
                userInput = pygame.key.get_pressed()

                # shoot
                player.shoot()

                # Movement
                player.move_hero(userInput)
                player.jump_motion(userInput)

                # # # CONTROLE INIMIGOS
                if len(enemies) == 0:
                    rand_nr = random.randint(0, 1)
                    if rand_nr == 1:
                        enemy = Enemy(1010, 407, left)
                        enemies.append(enemy)
                    if rand_nr == 0:
                        enemy = Enemy(0, 407, right)
                        enemies.append(enemy)
                for enemy in enemies:
                    enemy.move()
                    if enemy.off_screen() or enemy.health <= 0:
                        enemies.remove(enemy)
                    if enemy.health <= 0:
                        kills += 1


                # Draw game in windows
                draw_game()

    #FIM


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