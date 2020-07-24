import pygame
from .constants import screen_width, screen_height


class MasterSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def getRect(self):
        return self.rect

    def setX(self, value: int):
        self.x += value
        self.rect.x = self.x

    def setY(self, value: int):
        self.y += value
        self.rect.y = self.y

    def setXY(self, x:int, y: int):
        self.setX(x)
        self.setY(y)



class RectSprite(MasterSprite):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)

    def animate(self):
        if self.getRect().right >= screen_width:
            self.getRect().x = screen_width
            print("collided")

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)


class CircleSprite(MasterSprite):
    def __init__(self, diameter: int, x: int, y: int, speed_x: int, speed_y: int):
        self.diameter = diameter
        super().__init__(self.diameter, self.diameter, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, surface, color):
        pygame.draw.circle(surface, color,
                           (self.x, self.y), self.diameter // 2)

    def animation(self):
        # self.x += self.speed_x
        # self.y += self.speed_y
        self.setXY(self.speed_x, self.speed_y)

        # Check if the ball bounces off the sides
        if self.x + self.rect.width // 2 >= screen_width or self.x - self.rect.width // 2 <= 0:
            self.speed_x *= -1

        # Check if the ball bounces off the top
        if self.y - self.rect.height // 2 <= 0:
            self.speed_y *= -1

        if self.y + self.rect.width // 2 >= screen_height:
            return False

        return True
