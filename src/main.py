#!/usr/bin/env python3

import pygame
from utils import colors, classes
from utils.rounded_rect import draw_rounded_rect


def main():
    # Basic Variables Setup
    WIDTH, HEIGHT = 1080, 720
    clock = pygame.time.Clock()
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

    # Ball
    BALL_DIAMETER = 50
    ball = classes.CircleSprite(BALL_DIAMETER, WIDTH//2, HEIGHT//2)

    while isRunning:

        # Handle Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        # Sprite Animation
        # ball.bounceOffBorderLeft(WIDTH, HEIGHT)
        # ball.setXSpeed(10)
        # ball.moveXBySpeed()

        # Screen Background
        screen.fill(colors.BLACK)

        # Draw Items
        draw_rounded_rect(screen, player.rect, PLAYER_COLOR,
                          player.rect.height//2-2)
        ball.draw(screen, colors.WHITE)

        # Display everything on the screen
        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
