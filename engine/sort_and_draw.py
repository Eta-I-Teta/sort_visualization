from engine.drawing import *
import time

def bubble_sort_and_draw(surface: pygame.surface, arr: list, stopped_point: int):
    if stopped_point == None:
        return 0
    if stopped_point == len(arr) - 1:
        draw_array(surface, arr, [stopped_point, stopped_point + 1])
        return 0
    else:
        if arr[stopped_point] > arr[stopped_point + 1]:
            arr[stopped_point], arr[stopped_point + 1] = arr[stopped_point + 1], arr[stopped_point]
        draw_array(surface, arr, [stopped_point, stopped_point + 1])
        return stopped_point + 1
    
def shaker_sort_and_draw(surface: pygame.surface, arr: list, additional_info: list):
    return None