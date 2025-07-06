import pygame
import os
from engine.global_variables import *

class Image():
    def __init__(self, way: str, size: list, coordinates: list):
        self.size = size
        self.coordinates = coordinates
        self.image = pygame.transform.scale(
            pygame.image.load(way),
            self.size
        )
    def draw(self, surface: pygame.surface):
        surface.blit(
            self.image,
            self.coordinates
        )
    def change(self, new_way: str):
        self.image = pygame.transform.scale(
            pygame.image.load(new_way),
            self.size
        )

class VerticalBar():
    def __init__(self, size: list, percentage: int, coordinates: list):
        self.size = size
        self.percentage = percentage
        self.coordinates = coordinates
    def draw(self, surface: pygame.surface):
        pygame.draw.rect(
            surface,
            (0, 0, 0),
            (
                self.coordinates[0],
                self.coordinates[1],
                self.size[0],
                self.size[1]
            )
        )
        pygame.draw.rect(
            surface,
            (255 - 2.55 * self.percentage, 0 + 2.55 * self.percentage, 0),
            (
                self.coordinates[0],
                self.coordinates[1] + self.size[1] - int(self.size[1] * self.percentage / 100),
                self.size[0],
                int(self.size[1] * self.percentage / 100)
            )
        )

class MultilineText():
    def __init__(self, text: str):
        self.lines = text.split("\n")

    def draw(self, surface: pygame.surface, coordinates: list):
        [x, y] = coordinates

        for text in self.lines:
            surface.blit(FONT.render(text, True, CONFIG_SCREEN["font"]["color"]), [x, y])
            y += CONFIG_SCREEN["font"]["size"] + CONFIG_SCREEN["font"]["line_spacing"]