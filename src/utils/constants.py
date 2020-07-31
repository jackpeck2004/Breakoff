from .colors import *
from random import randint

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720
# SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080

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
# number_of_enemies = 12
enemies = []
enemy_speed = 1

# Text
text_y = 20

counter: int = 0
limit: int = 10
