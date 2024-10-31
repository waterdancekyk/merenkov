def encrypt_letter(letter):
    """Шифрует одну букву с помощью заданного алгоритма."""
    if letter.isalpha():
        # Преобразуем букву в число (A=1, B=2, ..., Z=26)
        num = ord(letter.upper()) - ord('A') + 1
        # Умножаем число само на себя 3 раза
        encrypted = num ** 3
        return encrypted
    else:
        raise ValueError("Только буквы разрешены.")

def decrypt_number(encrypted_num):
    """Расшифровывает зашифрованное число."""
    # Сначала умножаем на 7
    multiplied = encrypted_num * 7
    # Теперь извлекаем корень третьей степени, чтобы вернуть обратно
    decrypted_num = int(round(multiplied ** (1/3)))
    return decrypted_num

def letter_from_number(num):
    """Преобразует число обратно в букву."""
    return chr(num + ord('A') - 1)

def encrypt_message(message):
    """Шифрует сообщение."""
    encrypted_message = []
    for letter in message:
        try:
            encrypted_letter = encrypt_letter(letter)
            encrypted_message.append(encrypted_letter)
        except ValueError as e:
            print(e)
    return encrypted_message

def decrypt_message(encrypted_message):
    """Расшифровывает зашифрованное сообщение."""
    decrypted_message = ""
    for encrypted_num in encrypted_message:
        decrypted_num = decrypt_number(encrypted_num)
        decrypted_message += letter_from_number(decrypted_num)
    return decrypted_message

def main():
    print("Введите сообщение для шифрования (только буквы A-Z):")
    message = input().strip()
    
    # Шифруем сообщение
    encrypted_message = encrypt_message(message)
    print("Зашифрованное сообщение:", encrypted_message)

    # Расшифровываем сообщение
    decrypted_message = decrypt_message(encrypted_message)
    print("Расшифрованное сообщение:", decrypted_message)

if __name__ == "__main__":
    main()
