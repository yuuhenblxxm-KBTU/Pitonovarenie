import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

CELL_SIZE = 20
SNAKE_SIZE = CELL_SIZE
APPLE_SIZE = CELL_SIZE

snake_x = WIDTH // 2
snake_y = HEIGHT // 2

snake_dx = CELL_SIZE
snake_dy = 0

SNAKE_SPEED = 10

score = 0
speed_increase = 0.8

font = pygame.font.Font(None, 36)

class Apple:
    def __init__(self, x, y, color, score):
        self.x = x
        self.y = y
        self.color = color
        self.score = score

def draw_score(score):
    score_text = font.render(f"Счет: {score}", True, WHITE)
    WIN.blit(score_text, (10, 10))

def draw_snake(snake_list, snake_color):
    for segment in snake_list:
        pygame.draw.rect(WIN, snake_color, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_apple(apple):
    pygame.draw.rect(WIN, apple.color, (apple.x, apple.y, APPLE_SIZE, APPLE_SIZE))

snake_list = []
snake_length = 1

apples = []
apples.append(Apple(random.randint(0, (WIDTH - APPLE_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (HEIGHT - APPLE_SIZE) // CELL_SIZE) * CELL_SIZE,
                    RED, 1))
apples.append(Apple(random.randint(0, (WIDTH - APPLE_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (HEIGHT - APPLE_SIZE) // CELL_SIZE) * CELL_SIZE,
                    GOLD, 3))

clock = pygame.time.Clock()
running = True

while running:
    WIN.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dx == 0:  # Prevent moving directly opposite
        snake_dx = -CELL_SIZE
        snake_dy = 0
    elif keys[pygame.K_RIGHT] and snake_dx == 0:
        snake_dx = CELL_SIZE
        snake_dy = 0
    elif keys[pygame.K_UP] and snake_dy == 0:
        snake_dy = -CELL_SIZE
        snake_dx = 0
    elif keys[pygame.K_DOWN] and snake_dy == 0:
        snake_dy = CELL_SIZE
        snake_dx = 0

    snake_x += snake_dx
    snake_y += snake_dy

    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        running = False

    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for apple in apples:
        if snake_x == apple.x and snake_y == apple.y:
            apple.x = random.randint(0, (WIDTH - APPLE_SIZE) // CELL_SIZE) * CELL_SIZE
            apple.y = random.randint(0, (HEIGHT - APPLE_SIZE) // CELL_SIZE) * CELL_SIZE
            score += apple.score
            SNAKE_SPEED += int(SNAKE_SPEED * speed_increase)
            clock.tick(SNAKE_SPEED)

    for apple in apples:
        draw_apple(apple)

    draw_snake(snake_list, WHITE)
    draw_score(score)

    pygame.display.update()
    clock.tick(SNAKE_SPEED)

pygame.quit()