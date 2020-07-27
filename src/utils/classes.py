import pygame
import pygame.gfxdraw
from .constants import screen_width, screen_height


class MasterSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, *groups):
        super().__init__(*groups)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def getRect(self):
        return self.rect

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, value: int):
        self.x = value
        self.rect.x = self.x

    def setY(self, value: int):
        self.y = value
        self.rect.y = self.y

    def setXY(self, x: int, y: int):
        self.setX(x)
        self.setY(y)


class RectSprite(MasterSprite):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.change_x = 0
        self.change_y = 0

    def move(self, mod):
        move_size = 10
        # self.setX(self.x + mod*move_size)
        self.change_x = mod * move_size

    def animate(self):
        # Update Position based on move
        self.setX(self.getX() + self.change_x)

        # Make sure the player stays in side the viewport even when it collides
        if self.getRect().right >= screen_width:
            self.setX(screen_width - self.width)
        if self.getRect().left <= 0:
            self.setX(0)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)


class RoundedRectSprite(RectSprite):
    def draw(self, surface, color):
        rect = self.rect
        corner_radius = self.rect.height // 2 - 2
        if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
            raise ValueError(
                f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

        # need to use anti aliasing circle drawing routines to smooth the corners
        pygame.gfxdraw.aacircle(surface, rect.left + corner_radius,
                                rect.top + corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1,
                                rect.top + corner_radius, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.left + corner_radius,
                                rect.bottom - corner_radius - 1, corner_radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1,
                                rect.bottom - corner_radius - 1, corner_radius, color)

        pygame.gfxdraw.filled_circle(
            surface, rect.left + corner_radius, rect.top + corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(
            surface, rect.right - corner_radius - 1, rect.top + corner_radius, corner_radius, color)
        pygame.gfxdraw.filled_circle(
            surface, rect.left + corner_radius, rect.bottom - corner_radius - 1, corner_radius, color)
        pygame.gfxdraw.filled_circle(
            surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1, corner_radius, color)

        rect_tmp = pygame.Rect(rect)

        rect_tmp.width -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)

        rect_tmp.width = rect.width
        rect_tmp.height -= 2 * corner_radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)


class CircleSprite(MasterSprite):
    def __init__(self, diameter: int, x: int, y: int, speed_x: int, speed_y: int):
        self.diameter = diameter
        super().__init__(self.diameter, self.diameter, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, surface, color):
        pygame.draw.circle(surface, color,
                           (self.x, self.y), self.diameter // 2)

    def animation(self) -> bool:
        # self.x += self.speed_x
        # self.y += self.speed_y
        self.setXY(self.x + self.speed_x, self.y + self.speed_y)

        # Check if the ball bounces off the sides
        if self.x + self.rect.width // 2 >= screen_width or self.x - self.rect.width // 2 <= 0:
            self.speed_x *= -1

        # Check if the ball bounces off the top
        if self.y - self.rect.height // 2 <= 0:
            self.speed_y *= -1

        if self.y + self.rect.width // 2 >= screen_height:
            return False

        return True

class TextElement:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = ""
        self.textRect = 0

    def draw(self, content: str, color: tuple, screen, location=(screen_width // 2, screen_height // 2)):
        self.text = self.font.render(content, True, color)
        self.textRect = self.text.get_rect()
        self.textRect.center = location
        screen.blit(self.text, self.textRect)
