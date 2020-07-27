from .colors import *
from random import randint


def random_enemy_number():
    return randint(3, 12)


# Game constants
screen_width, screen_height = 1080, 720
# screen_width, screen_height = 1920, 1080

# Ball Constants
ball_speed_x = 5
ball_speed_y = 5
ball_diameter = 20
ball_color = WHITE

# Player constants
player_width, player_height = 300, 30
player_color = BLUE
initial_lives = 3
player_speed = 10

# Enemy Constants
spacer = 10
enemy_height = 30
enemy_y = 100
number_of_enemies = random_enemy_number()
# number_of_enemies = 12
enemy_width = (screen_width - spacer * number_of_enemies * 2) / number_of_enemies
enemies = []

# Text
text_y = 20
