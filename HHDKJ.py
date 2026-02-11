import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 30

# Player properties
player_size = 50
player_color = (255, 0, 0)
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Draw everything
    screen.fill((0, 0, 0))  # Black background
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Update display and tick clock
    pygame.display.flip()
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()