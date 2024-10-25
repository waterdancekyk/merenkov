import math

def calculate_expression(expression):
    try:
        # Проверка на наличие функций, таких как sin, cos и log
        if 'sin(' in expression:
            # Извлечение аргумента
            angle = float(expression.split('sin(')[1].split(')')[0])
            if angle > 2:
                raise ValueError("Синус не может быть больше 2.")
            result = math.sin(angle)
        elif 'cos(' in expression:
            # Извлечение аргумента
            angle = float(expression.split('cos(')[1].split(')')[0])
            if angle > 2:
                raise ValueError("Косинус не может быть больше 2.")
            result = math.cos(angle)
        elif 'log(' in expression:
            # Извлечение аргумента
            value = float(expression.split('log(')[1].split(')')[0])
            if value <= 0:
                raise ValueError("Аргумент логарифма должен быть положительным.")
            result = math.log(value)
        else:
            # Вычисление математического выражения с помощью eval
            result = eval(expression)
        
        return result
    
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль!"
    except Exception as e:
        return f"Произошла ошибка: {e}"

def main():
    expression = input("Введите математическое выражение: ")
    result = calculate_expression(expression)
    print(f"Результат: {result}")

# Запускаем программу
if __name__ == "__main__":
    main()
