def calculate_value(word):
    # Определяем стоимость каждой буквы
    letter_values = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10,
    }

    # Цены для цифр и спецзнаков
    special_value = 69

    total_value = 0

    for char in word:
        if char.upper() in letter_values:  # Проверка, если символ русская буква
            total_value += letter_values[char.upper()]
        elif char.isdigit() or not char.isalnum():  # Если это цифра или спецзнак
            total_value += special_value

    return total_value

# Основная программа
def main():
    user_input = input("Введите слово: ")
    value = calculate_value(user_input)
    print(f"Стоимость слова '{user_input}': {value} рублей")

if __name__ == "__main__":
    main()
