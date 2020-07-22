#!/usr/bin/env python3

import pygame

from utils import colors


# Basic Variables Setup

WIDTH, HEIGHT = 1920, 1080
isRunning = True

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakoff')
pygame.init()

rect = pygame.Rect(WIDTH // 2 -50, HEIGHT // 2 -50, 100, 100)

while isRunning:

    # Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # Screen Background
    screen.fill(colors.WHITE)

    # Draw Items
    pygame.draw.rect(screen, colors.RED, rect)

    # Display everything on the screen
    pygame.display.flip()
