def print_matrix(matrix):
    """Выводит матрицу в удобном формате."""
    for row in matrix:
        print(" ".join(map(str, row)))
    print()  # Печатаем пустую строку для разделения

def add_matrices(mat1, mat2):
    """Складывает две матрицы."""
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

def multiply_matrix_by_scalar(matrix, scalar):
    """Умножает матрицу на скаляр."""
    return [[element * scalar for element in row] for row in matrix]

def transpose_matrix(matrix):
    """Транспонирует матрицу."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def input_matrix(rows, cols):
    """Считывает матрицу с клавиатуры."""
    matrix = []
    print(f"Введите элементы матрицы {rows}x{cols}:")
    for i in range(rows):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Ошибка: введите {cols} элементов.")
            row = list(map(float, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение двух матриц")
        print("2. Умножение матрицы на скаляр")
        print("3. Транспонирование матрицы")
        print("4. Выход")

        choice = input("Введите номер операции: ")

        if choice == '1':
            rows = int(input("Введите количество строк для матриц: "))
            cols = int(input("Введите количество столбцов для матриц: "))
            print("Ввод первой матрицы:")
            matrix1 = input_matrix(rows, cols)
            print("Ввод второй матрицы:")
            matrix2 = input_matrix(rows, cols)

            result = add_matrices(matrix1, matrix2)
            print("Результат сложения:")
            print_matrix(result)

        elif choice == '2':
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            matrix = input_matrix(rows, cols)
            scalar = float(input("Введите скаляр (число): "))

            result = multiply_matrix_by_scalar(matrix, scalar)
            print("Результат умножения матрицы на скаляр:")
            print_matrix(result)

        elif choice == '3':
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            matrix = input_matrix(rows, cols)

            result = transpose_matrix(matrix)
            print("Результат транспонирования:")
            print_matrix(result)

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Ошибка: неверный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
