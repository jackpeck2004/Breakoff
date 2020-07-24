#!/usr/bin/env python3

import pygame
from utils import colors
from utils.classes import RectSprite, RoundedRectSprite, CircleSprite
from utils.constants import *

# Basic Variables Setup
clock = pygame.time.Clock()
is_running = True

# Initialize Pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakoff')
pygame.init()

# Main Player

player_width, player_height = 300, 30
player_color = colors.BLUE
player = RoundedRectSprite(
    player_width,
    player_height,
    screen_width // 2 - player_width // 2,
    screen_height - player_height - player_height // 3
)

# Ball
ball_diameter = 20
ball = CircleSprite(ball_diameter, screen_width // 2, screen_height // 2, ball_speed_x, ball_speed_y)

# Main game loop
while is_running:

    # Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Sprite Animation
    alive = ball.animation()

    player.setX(ball.speed_x)
    player.animate()

    # Check for collisions

    # Check if ball collides with the player bat
    if player.rect.colliderect(ball.rect):
        ball.speed_y *= -1

    if not alive:
        # is_running = False
        # TODO: add lives functionality
        pass

    # Screen Background
    screen.fill(colors.BLACK)

    # Draw Items
    # draw_rounded_rect(screen, player.rect, player_color,
    #                   player.rect.height // 2 - 2)
    player.draw(screen, player_color)
    ball.draw(screen, colors.WHITE)

    # Display everything on the screen
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
