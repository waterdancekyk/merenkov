def invert_number_string_method(number):
    """Инвертирует число с использованием строкового метода"""
    return int(str(number)[::-1])  # Переворот строки и преобразование обратно в целое число

def invert_number_arithmetic_method(number):
    """Инвертирует число с использованием арифметического метода"""
    inverted = 0
    while number > 0:
        inverted = inverted * 10 + number % 10  # Добавление последней цифры
        number //= 10  # Удаление последней цифры
    return inverted

def main():
    while True:
        user_input = input("Введите целое число: ")

        # Фильтрация ввода
        if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
            print("Ошибка: введите целое число без специальных символов и букв.")
            continue

        number = int(user_input)
        
        # Выбор способа инверсии
        print("Выберите способ инверсии:")
        print("1. Строковой метод")
        print("2. Арифметический метод")
        choice = input("Введите 1 или 2: ")

        if choice == '1':
            inverted_number = invert_number_string_method(abs(number))  # Используем модуль для инверсии
            if number < 0:
                inverted_number = -inverted_number  # Если число отрицательное, восстанавливаем знак
            print(f"Инвертированное число (строковой метод): {inverted_number}")
        elif choice == '2':
            inverted_number = invert_number_arithmetic_method(abs(number))  # Используем модуль для инверсии
            if number < 0:
                inverted_number = -inverted_number  # Если число отрицательное, восстанавливаем знак
            print(f"Инвертированное число (арифметический метод): {inverted_number}")
        else:
            print("Ошибка: выберите 1 или 2.")

        # Выход из программы
        if input("Хотите продолжить? (да/нет): ").lower() != 'да':
            break

# Запускаем основную функцию
if __name__ == "__main__":
    main()
