from .constants import *
from .classes import RectSprite
from .colors import *


def reset_lives():
    return initial_lives


def spawn_enemies():
    for i in range(1, number_of_enemies + 1):
        if i == 1:
            enemy_x = spacer
        else:
            enemy_x = (spacer * 2 + enemy_width) * (i - 1) + spacer

        rect = RectSprite(enemy_width, enemy_height, enemy_x, enemy_y)
        has_collided = False
        # enemy_color = (
        #     (number_of_enemies % 255 * number_of_enemies * 10) % 255,
        #     (number_of_enemies % 255 * number_of_enemies * 10) % 255,
        #     (number_of_enemies % 255 * number_of_enemies * 10) % 255)

        if number_of_enemies % 3 == 1:
            enemy_color = YELLOW
        elif number_of_enemies % 3 == 2:
            enemy_color = RED
        elif number_of_enemies % 3 == 3:
            enemy_color = GREEN
        else:
            enemy_color = PURPLE

        enemies.append([rect, enemy_color, has_collided])
