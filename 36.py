def caesar_cipher(text, shift):
    """Шифрует текст с использованием шифра Цезаря."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        elif char.isdigit():  # Обрабатываем цифры
            encrypted_text += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
        else:
            encrypted_text += char  # Оставляем остальные символы без изменений
    return encrypted_text

def vigenere_cipher(text, key):
    """Шифрует текст с использованием шифра Виженера."""
    encrypted_text = ""
    key_length = len(key)
    key_int = [ord(i.lower()) - ord('a') for i in key if i.isalpha()]  # Преобразуем ключ в числа
    key_index = 0

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift = key_int[key_index % key_length]
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
            key_index += 1
        elif char.isdigit():  # Обрабатываем цифры
            shift = key_int[key_index % key_length] % 10
            encrypted_text += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
            key_index += 1
        else:
            encrypted_text += char  # Оставляем остальные символы без изменений

    return encrypted_text

def main():
    print("Выберите тип шифрования:")
    print("1. Шифр Цезаря")
    print("2. Шифр Виженера")
    choice = input("Введите 1 или 2: ")

    message = input("Введите сообщение для шифрования: ")

    if choice == '1':
        shift = int(input("Введите код Цезаря (целое число): "))
        encrypted_message = caesar_cipher(message, shift)
        print(f"Зашифрованное сообщение (шифр Цезаря): {encrypted_message}")
    elif choice == '2':
        key = input("Введите ключевое слово для шифра Виженера: ")
        encrypted_message = vigenere_cipher(message, key)
        print(f"Зашифрованное сообщение (шифр Виженера): {encrypted_message}")
    else:
        print("Ошибка: Неверный выбор шифра.")

if __name__ == "__main__":
    main()
