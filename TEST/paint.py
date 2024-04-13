import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PENCIL_SIZE = 3
MARKER_SIZE = 10

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Game")
clock = pygame.time.Clock()

# Variables
drawing = False
brush_size = PENCIL_SIZE
drawing_color = BLACK

def draw_brush(pos):
    if drawing:
        pygame.draw.circle(screen, drawing_color, pos, brush_size)

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                if brush_size == PENCIL_SIZE:
                    brush_size = MARKER_SIZE
                else:
                    brush_size = PENCIL_SIZE
            elif event.key == pygame.K_c:
                screen.fill(WHITE)
    
    draw_brush(pygame.mouse.get_pos())
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()