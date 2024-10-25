import random

# Вводим размер матрицы
while True:
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))
        break
    except ValueError:
        print("Ошибка: введите целые числа для строк и столбцов!")

# Создаем матрицу с случайными числами
matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

# Вывод исходной матрицы
print("\nИсходная матрица:")
for row in matrix:
    print(row)

# Предлагаем пользователю выбрать действие
while True:
    print("\nВыберите действие:")
    print("1 - Транспонировать матрицу")
    print("2 - Отсортировать строки по возрастанию")
    print("3 - Отсортировать столбцы по возрастанию")
    print("4 - Отсортировать строки по убыванию")
    print("5 - Отсортировать столбцы по убыванию")
    print("0 - Выход")

    try:
        choice = int(input("Ваш выбор: "))
    except ValueError:
        print("Ошибка: введите число от 0 до 5.")
        continue

    if choice == 0:
        print("Выход.")
        break

    elif choice == 1:
        # Транспонирование матрицы
        transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
        print("\nТранспонированная матрица:")
        for row in transposed_matrix:
            print(row)

    elif choice == 2:
        # Сортировка строк по возрастанию
        for i in range(rows):
            matrix[i].sort()
        print("\nМатрица с отсортированными строками по возрастанию:")
        for row in matrix:
            print(row)

    elif choice == 3:
        # Сортировка столбцов по возрастанию
        for j in range(cols):
            column = [matrix[i][j] for i in range(rows)]
            column.sort()
            for i in range(rows):
                matrix[i][j] = column[i]
        print("\nМатрица с отсортированными столбцами по возрастанию:")
        for row in matrix:
            print(row)

    elif choice == 4:
        # Сортировка строк по убыванию
        for i in range(rows):
            matrix[i].sort(reverse=True)
        print("\nМатрица с отсортированными строками по убыванию:")
        for row in matrix:
            print(row)

    elif choice == 5:
        # Сортировка столбцов по убыванию
        for j in range(cols):
            column = [matrix[i][j] for i in range(rows)]
            column.sort(reverse=True)
            for i in range(rows):
                matrix[i][j] = column[i]
        print("\nМатрица с отсортированными столбцами по убыванию:")
        for row in matrix:
            print(row)

    else:
        print("Неверный выбор. Попробуйте снова.")
