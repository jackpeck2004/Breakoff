#!/usr/bin/env python3

import pygame

from utils import colors, classes

from utils.rounded_rect import draw_rounded_rect


# Basic Variables Setup

WIDTH, HEIGHT = 1080, 720
isRunning = True

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakoff')
pygame.init()

# Main Player

PLAYER_WIDTH, PLAYER_HEIGHT = 300, 30
PLAYER_COLOR = colors.BLUE
player = classes.RectSprite(
    PLAYER_WIDTH, PLAYER_HEIGHT, WIDTH//2-PLAYER_WIDTH//2, HEIGHT-PLAYER_HEIGHT-PLAYER_HEIGHT//3)

while isRunning:

    # Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # Screen Background
    screen.fill(colors.BLACK)

    # Draw Items
    # pygame.draw.rect(screen, colors.RED, rect)
    # player.draw(screen, colors.BLUE)
    draw_rounded_rect(screen, player.rect, PLAYER_COLOR,
                      player.rect.height//2-2)

    # Display everything on the screen
    pygame.display.flip()
