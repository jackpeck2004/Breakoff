import pygame


class MasterSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y


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
    def __init__(self, diameter, x, y):
        self.diameter = diameter
        self.width = self.diameter
        self.height = self.diameter
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface, color):
        pygame.draw.circle(surface, color,
                           (self.x, self.y), self.diameter//2)
