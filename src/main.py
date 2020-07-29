#!/usr/bin/env python3
import pygame
from random import randint
from utils import colors
from utils.classes import RectSprite, RoundedRectSprite, CircleSprite, TextElement
from utils.constants import *


def reset_lives():
    return initial_lives


def spawn_enemies(local_enemies, local_number_of_enemies):
    for i in range(1, local_number_of_enemies + 1):
        if i == 1:
            enemy_x = spacer
        else:
            enemy_x = (spacer * 2 + enemy_width) * (i - 1) + spacer

        local_enemy = RectSprite(enemy_width, enemy_height, enemy_x, enemy_y)
        has_collided = False
        # enemy_color = (
        #     (number_of_enemies % 255 * number_of_enemies * 10) % 255,
        #     (number_of_enemies % 255 * number_of_enemies * 10) % 255,
        #     (number_of_enemies % 255 * number_of_enemies * 10) % 255)

        if local_number_of_enemies % 3 == 1:
            enemy_color = YELLOW
        elif local_number_of_enemies % 3 == 2:
            enemy_color = RED
        elif local_number_of_enemies % 3 == 3:
            enemy_color = GREEN
        else:
            enemy_color = PURPLE

        local_enemies.append([local_enemy, enemy_color, has_collided])


# Basic Variables Setup
clock = pygame.time.Clock()
is_running = True
lives = reset_lives()
score = 0
level = 1

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
score_txt = TextElement()

# Enemies
spawn_enemies(enemies)

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
    alive = ball.animation
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
        ball.setXY(screen_width // 2, screen_height // 2)
        ball.speed_x = ball_speed_x
        ball.speed_y = ball_speed_y
        player.move_size = player_speed
        pass

    # Die when player loses all lives
    if lives == 0:
        break

    # Screen Background
    screen.fill(colors.BLACK)

    # Draw Items
    lives_txt.draw("lives: {}".format(lives), colors.WHITE, screen, (50, text_y))
    score_txt.draw("score: {}".format(score), colors.WHITE, screen, (screen_width // 2, text_y))
    player.draw(screen, player_color)
    ball.draw(screen, ball_color)
    for enemy in enemies:
        if enemy[0].rect.colliderect(ball.rect):
            enemy[2] = True
            ball.speed_y *= -1
            ball.speed_x *= 1.2
            ball.speed_y *= 1.2
            player.move_size *= 1.1
            score += 10 * level
        if not enemy[2]:
            enemy[0].y += 0.5
            enemy[0].rect.y += 0.5
            enemy[0].draw(screen, enemy[1])
        else:
            enemies.remove(enemy)

    if len(enemies) == 0:
        lives = reset_lives()
        number_of_enemies = random_enemy_number()
        spawn_enemies(enemies, randint(4, 12))
        level += 1

    # Display everything on the screen
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
