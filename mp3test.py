import pygame.mixer

pygame.mixer.init()
pygame.mixer.music.load("mp3/kusodokata.mp3")
pygame.mixer.music.play(1)

print("ctlr+c is stop")
while True:
    x = 1

pygame.mixer.music.stop()
