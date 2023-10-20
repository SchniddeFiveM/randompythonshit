import pygame
import sys

pygame.init()
hintergrund = pygame.image.load("img/background.jpg")
screen = pygame.display.set_mode([500,800])
clock = pygame.time.Clock()
pygame.display.set_caption("Penismann")

x = 100
y = 300

geschwindigkeit = 3
breite = 40
hoehe = 80


go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    gedrueckt = pygame.key.get_pressed()
    if gedrueckt[pygame.K_UP]:
        y -= geschwindigkeit
    if gedrueckt[pygame.K_RIGHT]:
        x += geschwindigkeit
    if gedrueckt[pygame.K_DOWN]:
        y += geschwindigkeit
    if gedrueckt[pygame.K_LEFT]:
        x -= geschwindigkeit

    screen.blit(hintergrund, (0,0))
    pygame.draw.rect(screen, (255,0,255), (x,y,breite,hoehe))
    pygame.display.update()
    clock.tick(165)