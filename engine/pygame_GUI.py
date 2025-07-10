import pygame
import os

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
    def __init__(
            self, 
            text: str, 
            coordinates: tuple[int, int],
            font_size: int = 16,
            color: tuple[int, int, int] = [255] * 3,
            font_family: str = None,
            line_spacing: int = 5
        ):
        self.text = text
        self.coordinates = coordinates
        self.font_size = font_size
        self.color = color,
        self.font_family = font_family
        self.line_spacing = line_spacing

    def draw(self, surface: pygame.surface):
        [x, y] = self.coordinates
        if type(self.font_family) is bool:
            font = pygame.font.SysFont('Arial', self.font_size)
        else:
            font = pygame.font.Font(self.font_family, self.font_size)

        for line in self.text.split("\n"):
            surface.blit(font.render(line, True, self.color), [x, y])
            y += self.font_size + self.line_spacing

class Rect():
    def __init__(
            self, 
            color: tuple[int, int, int], 
            size: tuple[int, int], 
            coordinates: tuple[int, int],
            border_radius: int = -1,
            border_width: int = 0
        ):
        self.color = color
        self.size = size
        self.coordinates = coordinates
        self.border_radius = border_radius
        self.border_width = border_width
    def draw(self, surface: pygame.surface):
        pygame.draw.rect(
            surface,
            self.color,
            [
                self.coordinates[0],
                self.coordinates[1],
                self.size[0],
                self.size[1]
            ],
            self.border_width,
            self.border_radius
        )