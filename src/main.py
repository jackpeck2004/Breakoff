#!/usr/bin/env python3

import pygame
from utils import colors
from utils.classes import RectSprite, RoundedRectSprite, CircleSprite, TextElement
from utils.constants import *

# Basic Variables Setup
clock = pygame.time.Clock()
is_running = True
lives = 3

# Initialize Pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakoff')
pygame.init()

# Main Player
player = RoundedRectSprite(
    player_width,
    player_height,
    screen_width // 2 - player_width // 2,
    screen_height - player_height - player_height // 3
)

# Ball
ball = CircleSprite(ball_diameter, screen_width // 2, screen_height // 2, ball_speed_x, ball_speed_y)

# Text
lives_txt = TextElement()


# Main game loop
while is_running:

    # Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move(1)
            if event.key == pygame.K_LEFT:
                player.move(-1)
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.move(0)


    # Sprite Animation
    alive = ball.animation()
    player.animate()

    # Check for collisions
    # Check if ball collides with the player bat
    if player.rect.colliderect(ball.rect):
        ball.speed_y *= -1

    # When the player loses a life
    if not alive:
        # is_running = False
        lives -= 1
        alive = True
        ball.setXY(screen_width//2, screen_height//2)
        print(lives)
        pass

    # Die when player loses all lives
    if lives == 0:
        break

    # Screen Background
    screen.fill(colors.BLACK)

    # Draw Items
    lives_txt.draw("lives: {}".format(lives), colors.WHITE, screen, (50, 20))
    player.draw(screen, player_color)
    ball.draw(screen, ball_color)

    # Display everything on the screen
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
