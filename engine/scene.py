import pygame

class Scene():
    def __init__(self, name: str, description: str, sort):
        self.name = name
        self.description = description
        self.sort = sort