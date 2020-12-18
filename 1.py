import os
import sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


clock = pygame.time.Clock()
running = True
b = pygame.Color((0, 0, 0))

all_sprites = pygame.sprite.Group()

s = pygame.sprite.Sprite()
s.image = pygame.image.load('cursed_cursor.png')
s.rect = s.image.get_rect()
all_sprites.add(s)
s.rect.x, s.rect.y = (0, 0)
screen.blit(s.image, s.rect)
pos = (0, 0)
pygame.mouse.set_visible(False)

while running:
    screen.fill(b)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            s.rect.x, s.rect.y = event.pos
            
    screen.blit(s.image, s.rect)
    clock.tick(60)
    pygame.display.flip()
    screen.fill(b)
pygame.quit()
