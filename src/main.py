#!/usr/bin/env python3

import pygame
from utils import colors, classes
from utils.rounded_rect import draw_rounded_rect


def main():
    # Basic Variables Setup
    screen_width, screen_height = 1080, 720
    clock = pygame.time.Clock()
    is_running = True

    # Initialize Pygame
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Breakoff')
    pygame.init()

    # Main Player

    player_width, player_height = 300, 30
    player_color = colors.BLUE
    player = classes.RectSprite(
        player_width,
        player_height,
        screen_width // 2 - player_width // 2,
        screen_height - player_height - player_height//3
    )

    # Ball
    ball_diameter = 50
    ball_speed_x = 10
    ball_speed_y = 10
    ball = classes.CircleSprite(ball_diameter, screen_width//2, screen_height//2)

    def ball_animation():
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        if ball.x >= screen_width or ball.x <= 0:
            ball.x *= -1
            print(ball.x)
        if ball.y >= screen_height or ball.y <= 0:
            ball.y *= -1
            print(ball.y)

    while is_running:

        # Handle Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # Sprite Animation
        ball_animation()

        # Screen Background
        screen.fill(colors.BLACK)

        # Draw Items
        draw_rounded_rect(screen, player.rect, player_color,
                          player.rect.height//2-2)
        ball.draw(screen, colors.WHITE)

        # Display everything on the screen
        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
