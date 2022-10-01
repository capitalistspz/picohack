from typing import Union

import pygame
from pygame import Surface
from pygame.surface import SurfaceType


class drawable_circle:
    def __init__(self, x, y, radius, colour=(255, 255, 255)):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__colour = colour

    def draw(self, screen: Union[Surface, SurfaceType]):
        surface = pygame.Surface()
