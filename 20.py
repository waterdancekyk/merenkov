import numpy as np
import matplotlib.pyplot as plt

def draw_circle(ax, center, radius, pepperoni_count):
    """Рисует круг с заданным центром, радиусом и количеством пепперони."""
    circle = plt.Circle(center, radius, color='orange', alpha=0.5)
    ax.add_artist(circle)
    # Отображаем количество пепперони внутри круга
    ax.text(center[0], center[1], str(pepperoni_count), ha='center', va='center', fontsize=12)

def pizza_fractal(ax, center, radius, depth, pepperoni_count):
    """Рекурсивная функция для рисования пиццы-фрактала."""
    if depth == 0:
        return
    draw_circle(ax, center, radius, pepperoni_count)  # Рисуем текущий кусок пиццы
    new_radius = radius / 2  # Новый радиус будет в 2 раза меньше
    new_pepperoni_count = pepperoni_count // 4  # Пепперони делится на 4

    # Рисуем 4 новых круга в каждой четверти
    pizza_fractal(ax, (center[0] - new_radius, center[1] - new_radius), new_radius, depth - 1, new_pepperoni_count)  # Нижний левый
    pizza_fractal(ax, (center[0] + new_radius, center[1] - new_radius), new_radius, depth - 1, new_pepperoni_count)  # Нижний правый
    pizza_fractal(ax, (center[0] - new_radius, center[1] + new_radius), new_radius, depth - 1, new_pepperoni_count)  # Верхний левый
    pizza_fractal(ax, (center[0] + new_radius, center[1] + new_radius), new_radius, depth - 1, new_pepperoni_count)  # Верхний правый

def main():
    radius = 100  # Радиус пиццы
    depth = 4  # Глубина рекурсии
    initial_pepperoni = 100  # Начальное количество пепперони

    fig, ax = plt.subplots()
    ax.set_xlim(-radius*1.5, radius*1.5)
    ax.set_ylim(-radius*1.5, radius*1.5)
    ax.set_aspect('equal')
    plt.axis('off')  # Отключаем оси

    # Рисуем фрактал пиццы
    pizza_fractal(ax, (0, 0), radius, depth, initial_pepperoni)

    # Расчет количества людей, которых можно накормить
    total_people = initial_pepperoni
    for i in range(depth):
        total_people //= 4  # На каждом уровне пепперони делится на 4
        print(f"Уровень {i+1}: {total_people} пепперони")

    plt.title("Пицца-фрактал")
    plt.show()

# Запускаем программу
if __name__ == "__main__":
    main()
