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