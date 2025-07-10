from engine.pygame_GUI import *
from engine.scene import *
from engine.global_variables import *

def draw_array(surface: pygame.surface, arr: list, selected: list = []):
    lenght = len(arr)
    size = min(
        CONFIG_SCREEN["width"] * 0.8 / lenght,
        CONFIG_SCREEN["height"] * 0.8 / lenght
    )
    x = (CONFIG_SCREEN["width"] - lenght * size) / 2
    for index in range(len(arr)):
        y = ((CONFIG_SCREEN["height"] - lenght * size) / 2) + ((lenght - 1) * size)
        color = COLOR["blue"] if index in selected else COLOR["green"]
        for floor in range(arr[index]):
            Rect(color, [size] * 2, [x, y]).draw(surface)
            y -= size
        x += size

def draw_scene(surface: pygame.surface, scene: Scene):
    MultilineText(scene.name, [15, 15], font_size = 35, color = CONFIG_SCREEN["text_color"]).draw(surface)
    MultilineText(scene.description, [15, 15 + 50 + 5], font_size = 30, color = CONFIG_SCREEN["text_color"], line_spacing = 0).draw(surface)