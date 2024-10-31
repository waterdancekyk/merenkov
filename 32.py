import pygame
import random
import math
import time

# Инициализация Pygame
pygame.init()

# Параметры окна
screen = pygame.display.set_mode((800, 800), pygame.FULLSCREEN)
pygame.display.set_caption("Фрактал на весь экран")

# Функция для генерации случайного цвета
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Функция для рисования фрактала (например, фрактальное дерево)
def draw_fractal(surface, x, y, angle, depth, color):
    if depth > 0:
        x_end = x + int(math.cos(math.radians(angle)) * depth * 10.0)
        y_end = y + int(math.sin(math.radians(angle)) * depth * 10.0)

        pygame.draw.line(surface, color, (x, y), (x_end, y_end), depth)
        draw_fractal(surface, x_end, y_end, angle - 20, depth - 1, color)
        draw_fractal(surface, x_end, y_end, angle + 20, depth - 1, color)

# Основной цикл программы
running = True
last_color_change = time.time()
color = random_color()

while running:
    # Закрытие программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Изменение цвета каждые 5 секунд
    if time.time() - last_color_change > 5:
        color = random_color()
        last_color_change = time.time()

    # Заливка экрана чёрным цветом
    screen.fill((0, 0, 0))

    # Рисование фрактала
    draw_fractal(screen, 400, 800, -90, 10, color)

    # Обновление дисплея
    pygame.display.flip()
    pygame.time.delay(50)

# Завершение Pygame
pygame.quit()
