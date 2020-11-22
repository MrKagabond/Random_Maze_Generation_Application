import pygame


class Tile:
    def __init__(self, x: int, y: int, w: int, h: int, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen

    def draw(self, x: int, y: int, w: int, h: int, colour):
        pygame.draw.rect(self.screen, colour, pygame.Rect(x, y, w, h))
        pygame.display.update()
