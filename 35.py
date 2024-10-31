def caesar_cipher(text, shift):
    """Шифрует или расшифровывает текст с использованием шифра Цезаря."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Оставляем остальные символы без изменений
    return encrypted_text

def is_encrypted(text):
    """Определяет, является ли текст зашифрованным."""
    return any(not char.isalpha() and not char.isspace() for char in text)

def main():
    message = input("Введите сообщение: ")
    shift = int(input("Введите код Цезаря (целое число): "))

    # Шифруем сообщение
    encrypted_message = caesar_cipher(message, shift)
    print(f"Зашифрованное сообщение: {encrypted_message}")

    # Проверяем, является ли зашифрованным
    if is_encrypted(encrypted_message):
        print("Это зашифрованное сообщение.")
    else:
        print("Это обычный текст.")

    # Расшифровка сообщения
    decrypt_shift = -shift  # Для расшифровки используем отрицательное значение сдвига
    decrypted_message = caesar_cipher(encrypted_message, decrypt_shift)
    print(f"Расшифрованное сообщение: {decrypted_message}")

if __name__ == "__main__":
    main()
