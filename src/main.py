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

    ball_speed_x = 5
    ball_speed_y = 7
    ball = classes.CircleSprite(ball_diameter, screen_width//2, screen_height//2)

    def ball_animation(speedX, speedY):
        ball.x += speedX
        ball.y += speedY
        if ball.x >= screen_width or ball.x <= 0:
            speedX *= -1
            print("x:", ball.x)
        if ball.y >= screen_height or ball.y <= 0:
            speedY *= -1
            print("y:", ball.y)

    # Main game loop
    while is_running:

        # Handle Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # Sprite Animation
        ball_animation(ball_speed_x, ball_speed_y)

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
