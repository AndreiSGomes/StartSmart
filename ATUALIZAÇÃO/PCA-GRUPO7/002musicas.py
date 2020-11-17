pygame.mixer.init()
pygame.mixer.music.load('de021.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass