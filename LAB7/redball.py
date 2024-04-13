import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))

RED = (255, 0, 0)
center = (200, 150)
radius = 25
thickness = 0
center_x, center_y = 400 // 2, 300 // 2

x, y = center_x, center_y

clock = pygame.time.Clock()
running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and y > 50:
                y -= 20
            elif event.key == pygame.K_s and y < 250:
                y += 20
            elif event.key == pygame.K_a and x > 50:
                x -= 20
            elif event.key == pygame.K_d and x < 350:
                x += 20
        
    screen.fill((255, 255, 255))
        
    pygame.draw.circle(screen, RED, (x, y), radius, thickness)
        
    pygame.display.flip()
    clock.tick(60)