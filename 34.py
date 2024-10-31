import random
import string

# Функция шифрования (шифр Цезаря)
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Генерация лицензионного ключа
def generate_license_key():
    joke = "shot_in_foot"  # Шутка
    encrypted_joke = caesar_cipher(joke, 3)  # Зашифровка шутки

    # Генерация случайных частей ключа
    part1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part2 = encrypted_joke[:4] + random.choice(string.ascii_uppercase)  # Вставка части шутки
    part3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    # Форматирование ключа
    license_key = f"{part1}-{part2}-{part3}"

    # Добавление контрольной суммы
    checksum = sum(ord(c) for c in license_key) % 10
    license_key += str(checksum)

    return license_key

# Проверка лицензионного ключа
def check_license_key(key):
    # Проверка контрольной суммы
    if not key[:-1].replace("-", "").isalnum() or len(key) != 15:
        return False

    expected_checksum = sum(ord(c) for c in key[:-1]) % 10
    if int(key[-1]) != expected_checksum:
        return False

    # Расшифровка шутки
    encrypted_joke = key[5:9]  # Часть шутки из ключа
    decrypted_joke = caesar_cipher(encrypted_joke, -3)  # Расшифровка шутки

    if decrypted_joke == "shot":  # Проверка на правильность шутки
        print("Шутка: Выстрел в ногу!")
        return True
    return False

# Основная программа
def main():
    license_key = generate_license_key()
    print(f"Сгенерированный лицензионный ключ: {license_key}")

    # Проверка ключа (можно вводить ключ вручную)
    user_input = input("Введите лицензионный ключ для проверки: ")
    if check_license_key(user_input):
        print("Ключ верный! 🎉")
        # Здесь можно добавить вывод изображения слоника
    else:
        print("Неверный ключ. Попробуйте снова.")

if __name__ == "__main__":
    main()
