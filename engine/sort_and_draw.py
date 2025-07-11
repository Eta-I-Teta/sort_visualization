from engine.drawing import *
import time

def bubble_sort_and_draw(surface: pygame.surface, arr: list, additional_info, delay: int):
    if additional_info == None:
        draw_array(surface, arr)
        time.sleep(delay)
        return {
            "stopped_point": 0,
            "right_border": len(arr) - 1
        }
    
    stopped_point = additional_info["stopped_point"]
    right_border = additional_info["right_border"]

    if stopped_point != right_border:
        if arr[stopped_point] > arr[stopped_point + 1]:
            arr[stopped_point], arr[stopped_point + 1] = arr[stopped_point + 1], arr[stopped_point]
        draw_array(surface, arr, [stopped_point, stopped_point + 1])
        time.sleep(delay)
        return {
            "stopped_point": stopped_point + 1,
            "right_border": right_border
        }
    else:
        draw_array(surface, arr)
        time.sleep(delay)
        return {
            "stopped_point": 0,
            "right_border": right_border - 1
        }

def comb_sort_and_draw(surface: pygame.surface, arr: list, additional_info, delay: int):
    if additional_info == None:
        draw_array(surface, arr)
        return {
            "stopped_point": 0,
            "step": int(len(arr) // 1.247)
        }
    
    stopped_point = additional_info["stopped_point"]
    step = additional_info["step"]

    if stopped_point + step > len(arr) - 1:
        draw_array(surface, arr)
        return {
            "stopped_point": 0,
            "step": int(step // 1.247)
        }
    else:
        if arr[stopped_point] > arr[stopped_point + step]:
            arr[stopped_point], arr[stopped_point + step] = arr[stopped_point + step], arr[stopped_point]
        draw_array(surface, arr, [stopped_point, stopped_point + step])
        time.sleep(delay)
        return {
            "stopped_point": stopped_point + 1,
            "step": step
        }

def insertion_sort_and_draw(surface: pygame.surface, arr: list, additional_info, delay: int):
    if additional_info == None:
        draw_array(surface, arr)
        return {
            "stopped_point": 0,
            "right_border": 0
        }
    
    stopped_point = additional_info["stopped_point"]
    right_border = additional_info["right_border"]

    if right_border == len(arr) - 1:
        return {
            "stopped_point": 0,
            "right_border": 0
        }
    else:
        if stopped_point != -1:
            if arr[right_border + 1] > arr[stopped_point]:
                move_element(arr, right_border + 1, stopped_point + 1)
                draw_array(surface, arr, [stopped_point, right_border + 1])
                time.sleep(delay)
                return {
                    "stopped_point": right_border + 1,
                    "right_border": right_border + 1
                }
            else:
                draw_array(surface, arr, [stopped_point, right_border + 1])
                time.sleep(delay)
                return {
                    "stopped_point": stopped_point - 1,
                    "right_border": right_border
                }
        else:
            move_element(arr, right_border + 1, 0)
            draw_array(surface, arr, [stopped_point, right_border + 1])
            time.sleep(delay)
            return {
                "stopped_point": right_border + 1,
                "right_border": right_border + 1
            }