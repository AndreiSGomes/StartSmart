import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

	
# define display surface			
W, H = 1080, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("War C-19")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
COLOR = (97, 31, 184)

bg = pygame.image.load("scenery/scenery_test.png").convert()
bg = pygame.transform.scale(bg, (W, H))
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 3
stagePosX = 0

startScrollingPosX = HW

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius #posição do personagem na tela (eixo X)
playerPosY = 547  #posição do personagem na tela (eixo y)
playerVelocityX = 0 #velocidade do personagem


# main loop
while True:
	events()

	k = pygame.key.get_pressed()
	if k[K_RIGHT]:
		playerVelocityX = 1
	elif k[K_LEFT]:
		playerVelocityX = -1
	else:
		playerVelocityX = 0

	playerPosX += playerVelocityX
	if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
	if playerPosX < circleRadius: playerPosX = circleRadius
	if playerPosX < startScrollingPosX: circlePosX = playerPosX
	elif playerPosX > stageWidth - startScrollingPosX: circlePosX = playerPosX - stageWidth + W
	else:
		circlePosX = startScrollingPosX
		stagePosX += -playerVelocityX

	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))

	pygame.draw.circle(DS, COLOR, (int(circlePosX), playerPosY - 25), circleRadius, 0)

	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)