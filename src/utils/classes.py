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

    def draw(self, screen, color):
        self.color = color
        self.screen = screen
        pygame.draw.rect(self.screen, self.color, self.rect)