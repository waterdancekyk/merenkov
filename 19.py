import numpy as np
import matplotlib.pyplot as plt

def create_sierpinski_carpet(matrix, x, y, size, depth):
    if depth == 0:  # Базовый случай: ничего не делать, если достигли глубины
        return
    new_size = size // 3  # Новый размер для деления
    matrix[y + new_size:y + 2 * new_size, x + new_size:x + 2 * new_size] = 0  # Заменяем центральную часть на 0
    # Рекурсивные вызовы для 8 оставшихся частей
    for i in range(3):
        for j in range(3):
            if (i, j) != (1, 1):  # Пропускаем центральную часть
                create_sierpinski_carpet(matrix, x + j * new_size, y + i * new_size, new_size, depth - 1)

def main(size, depth):
    matrix = np.ones((size, size))  # Создаем начальную матрицу
    create_sierpinski_carpet(matrix, 0, 0, size, depth)  # Рекурсивно создаем фрактал
    plt.imshow(matrix, cmap='binary')  # Визуализируем результат
    plt.axis('off')  # Отключаем оси
    plt.show()  # Показываем график

# Запускаем программу
n = 729  # Размер матрицы (должен быть 3^k)
depth = 5  # Глубина рекурсии
main(n, depth)
