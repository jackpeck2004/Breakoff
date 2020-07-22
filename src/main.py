#!/usr/bin/env python3

import pygame

# Basic Variables Setup

WIDTH, HEIGHT = 1920, 1080
isRunning = True

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakoff')
pygame.init()

while isRunning:

    # Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False