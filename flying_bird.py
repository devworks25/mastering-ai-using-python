import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Bird")

clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
GREEN = (50, 180, 70)
YELLOW = (255, 220, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Bird
bird_x = 150
bird_y = 300
bird_size = 30
bird_velocity = 0

GRAVITY = 0.5
JUMP = -9

# Pipes
pipe_width = 70
pipe_gap = 170
pipe_speed = 4

pipes = []

def create_pipe():
    gap_y = random.randint(150, 400)

    top_pipe = pygame.Rect(
        WIDTH,
        0,
        pipe_width,
        gap_y - pipe_gap // 2
    )

    bottom_pipe = pygame.Rect(
        WIDTH,
        gap_y + pipe_gap // 2,
        pipe_width,
        HEIGHT
    )

    return top_pipe, bottom_pipe


# Create first pipes
for x in [500, 800, 1100]:
    top, bottom = create_pipe()
    top.x = x
    bottom.x = x
    pipes.append((top, bottom))


score = 0
font = pygame.font.Font(None, 50)

game_over = False

while True:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = JUMP

            if event.key == pygame.K_SPACE and game_over:
                # Restart game
                bird_y = 300
                bird_velocity = 0
                score = 0
                pipes.clear()

                for x in [500, 800, 1100]:
                    top, bottom = create_pipe()
                    top.x = x
                    bottom.x = x
                    pipes.append((top, bottom))

                game_over = False

    if not game_over:

        # Bird physics
        bird_velocity += GRAVITY
        bird_y += bird_velocity

        bird_rect = pygame.Rect(
            bird_x,
            int(bird_y),
            bird_size,
            bird_size
        )

        # Move pipes
        for top, bottom in pipes:
            top.x -= pipe_speed
            bottom.x -= pipe_speed

        # Add new pipe
        if pipes[-1][0].x < 500:
            top, bottom = create_pipe()
            pipes.append((top, bottom))

        # Remove old pipes
        if pipes[0][0].x < -pipe_width:
            pipes.pop(0)
            score += 1

        # Collision with pipes
        for top, bottom in pipes:
            if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
                game_over = True

        # Collision with ground/sky
        if bird_y <= 0 or bird_y + bird_size >= HEIGHT:
            game_over = True

    # Draw background
    screen.fill(SKY)

    # Draw pipes
    for top, bottom in pipes:
        pygame.draw.rect(screen, GREEN, top)
        pygame.draw.rect(screen, GREEN, bottom)

    # Draw bird
    pygame.draw.circle(
        screen,
        YELLOW,
        (bird_x + bird_size // 2, int(bird_y) + bird_size // 2),
        bird_size // 2
    )

    # Bird eye
    pygame.draw.circle(
        screen,
        BLACK,
        (bird_x + 20, int(bird_y) + 9),
        4
    )

    # Score
    score_text = font.render(str(score), True, WHITE)
    screen.blit(score_text, (WIDTH // 2, 30))

    # Game over
    if game_over:
        game_over_text = font.render(
            "GAME OVER",
            True,
            BLACK
        )
        restart_text = font.render(
            "Press SPACE to restart",
            True,
            BLACK
        )

        screen.blit(
            game_over_text,
            (WIDTH // 2 - 120, HEIGHT // 2 - 50)
        )

        screen.blit(
            restart_text,
            (WIDTH // 2 - 180, HEIGHT // 2 + 10)
        )

    pygame.display.update()
    clock.tick(60)