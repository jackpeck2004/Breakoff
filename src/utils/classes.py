import pygame
from .constants import screen_width, screen_height


class MasterSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def collision(self):
        if self.x + self.rect.width // 2 >= screen_width or self.x - self.rect.width // 2 <= 0:
            self.speed_x *= -1
        if self.y + self.rect.height // 2 >= screen_height or self.y - self.rect.height // 2 <= 0:
            self.speed_y *= -1


class RectSprite(MasterSprite):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)


class CircleSprite(MasterSprite):
    def __init__(self, diameter, x, y, speed_x, speed_y):
        self.diameter = diameter
        self.width = self.diameter
        self.height = self.diameter
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def animation(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, surface, color):
        pygame.draw.circle(surface, color,
                           (self.x, self.y), self.diameter // 2)
