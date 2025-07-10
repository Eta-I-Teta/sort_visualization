import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

from engine.pygame_GUI import *
from engine.global_variables import *
from engine.sort_and_draw import *

# Настройки окна
screen = pygame.display.set_mode((CONFIG_SCREEN["width"], CONFIG_SCREEN["height"]))
pygame.display.set_caption(CONFIG_SCREEN["window_name"])

additional_info = None

delay = 0

scenes = [
    Scene(
        "Сортировка пузырьком", 
        "Принцип работы:\n" \
        "Проходит по массиву, сравнивая соседние элементы\n" \
        "и меняя их местами, если они стоят в неправильном порядке.\n" \
        "Процесс повторяется, пока массив не будет полностью отсортирован.\n", 
        bubble_sort_and_draw,
    )
]
selected_scene = 0
sorting = False

# Частота кадров
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sorting = False

            if (event.key == pygame.K_RETURN) and (not sorting):
                arr = []
                for i in range(50): arr.append(i + 1)
                random.shuffle(arr)
                sorting = True
                additional_info = None

            if (event.key == pygame.K_t):
                if CONFIG_SCREEN["bg_color"] == COLOR["white"]:
                    CONFIG_SCREEN["bg_color"] = COLOR["black"]
                    CONFIG_SCREEN["text_color"] = COLOR["white"]
                else:
                    CONFIG_SCREEN["bg_color"] = COLOR["white"]
                    CONFIG_SCREEN["text_color"] = COLOR["black"]

            if (event.key == pygame.K_d) and (not sorting):
                if (selected_scene != len(scenes) - 1):
                    selected_scene += 1
                else:
                    selected_scene = 0

            if (event.key == pygame.K_a) and (not sorting):
                if (selected_scene != 0):
                    selected_scene -= 1
                else:
                    selected_scene = len(scenes) - 1
            
            if event.key == pygame.K_w:
                delay = min(1.5, round(delay + 0.1, 1))
            if event.key == pygame.K_s:
                delay = max(0, round(delay - 0.1, 1))
    
    # Обновление игрового состояния
    # (здесь будет ваша игровая логика)
    
    # Отрисовка
    screen.fill(CONFIG_SCREEN["bg_color"])

    MultilineText(
        f"Задержка: {delay} с", 
        [15, CONFIG_SCREEN["height"] - 16 - 15], 
        font_size = 16, 
        color = CONFIG_SCREEN["text_color"],
        font_family = CONFIG_SCREEN["font_family"]
    ).draw(screen)

    if not sorting:
        MultilineText(
            scenes[selected_scene].name, 
            [15, 15], 
            font_size = 30, 
            color = CONFIG_SCREEN["text_color"],
            font_family = CONFIG_SCREEN["font_family"]
        ).draw(screen)
        MultilineText(
            scenes[selected_scene].description, 
            [15, 15 + 50 + 5], 
            font_size = 20, 
            color = CONFIG_SCREEN["text_color"], 
            line_spacing = 0,
            font_family = CONFIG_SCREEN["font_family"]
        ).draw(screen)
    else:
        if arr == sorted(arr):
            draw_array(screen, arr)
        else:
            additional_info = scenes[selected_scene].sort(screen, arr, additional_info, delay)
    
    pygame.display.flip()
    clock.tick(CONFIG_SCREEN["FPS"])

# Завершение работы
pygame.quit()
sys.exit()