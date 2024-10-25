def draw_triangle(rows):
    """Рисует один треугольник с указанным количеством строк."""
    triangle = []
    for i in range(rows):
        # Создаем каждую строку с центровкой
        line = ' ' * (rows - i - 1) + '*' * (2 * i + 1)
        triangle.append(line)
    return triangle

def draw_triforce(symbols_per_triangle):
    """Рисует трифорс, состоящий из 3 треугольников."""
    # Вычисляем количество строк в одном треугольнике
    rows = symbols_per_triangle // 2  # Должно быть четным для симметрии
    
    if symbols_per_triangle % 2 != 0 or rows < 1:
        print("Невозможно построить трифорс с данным количеством символов.")
        return

    # Рисуем три треугольника
    top_triangle = draw_triangle(rows)
    bottom_triangle = draw_triangle(rows)
    
    # Соединяем верхний и нижний треугольники
    triforce = []
    for i in range(rows):
        # Создаем строку для верхнего треугольника
        triforce.append(top_triangle[i] + ' ' + top_triangle[i])
    for i in range(rows):
        # Создаем строку для нижнего треугольника
        triforce.append(' ' * (rows - 1) + bottom_triangle[i])
    
    # Выводим трифорс
    for line in triforce:
        print(line)

def main():
    while True:
        user_input = input("Введите количество символов в одном треугольнике: ")
        try:
            symbols_per_triangle = int(user_input)
            draw_triforce(symbols_per_triangle)
        except ValueError:
            print("Ошибка: введите целое число.")
        
        # Запрос на продолжение
        if input("Хотите продолжить? (да/нет): ").lower() != 'да':
            break

# Запускаем основную функцию
if __name__ == "__main__":
    main()
