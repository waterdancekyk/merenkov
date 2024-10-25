class Triangle:
    def __init__(self, a, b, c):
        # Проверка: все ли значения целые числа
        if not all(isinstance(x, int) for x in [a, b, c]):
            raise ValueError("Нужно вводить только целые числа!")
        
        # Проверка: все ли числа положительные
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Отрицательные числа нельзя!")
        
        self.a = a
        self.b = b
        self.c = c
    
    def eto_treygolnik(self):
        # Проверка условия существования треугольника
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Треугольник строится."
        else:
            return "Треугольник не построится."

# Функция для ввода от пользователя
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Отрицательные числа нельзя! Попробуйте снова.")
            else:
                return value
        except ValueError:
            print("Нужно вводить только целые числа! Попробуйте снова.")

# Основной код
def main():
    print("Введите длины сторон треугольника.")
    
    a = get_positive_integer("Введите сторону a: ")
    b = get_positive_integer("Введите сторону b: ")
    c = get_positive_integer("Введите сторону c: ")

    # Создание экземпляра класса Triangle
    try:
        triangle = Triangle(a, b, c)
        # Выводим результат
        print(triangle.eto_treygolnik())
    except ValueError as e:
        print(e)

# Запуск программы
if __name__ == "__main__":
    main()
