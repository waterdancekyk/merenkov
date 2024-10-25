import os
import time
import re
import threading

# Путь к папке на рабочем столе
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_name = "Супер_папка"
folder_path = os.path.join(desktop_path, folder_name)

def create_folder():
    """Создает папку на рабочем столе"""
    os.makedirs(folder_path, exist_ok=True)
    print(f"Папка '{folder_name}' создана на рабочем столе.")

def is_valid_message(message):
    """Проверяет, содержит ли сообщение специальные символы"""
    return bool(re.match(r'^[\w\s\d]+$', message))

def create_files(message, base_filename):
    """Создает 10 файлов с заданным текстом"""
    for i in range(10):
        filename = f"{base_filename}_{i+1}.txt"
        with open(os.path.join(folder_path, filename), 'w', encoding='utf-8') as f:
            f.write(message)
    print("Файлы успешно созданы.")

def delete_files():
    """Удаляет все файлы в папке"""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Все файлы удалены.")

def prompt_delete_files():
    """Запрашивает у пользователя, хочет ли он удалить файлы"""
    user_input = input("Хотите удалить все файлы? (да/нет): ")
    if user_input.lower() == 'да':
        delete_files()
    else:
        print("Файлы не удалены. Программа завершена.")

def timer():
    """Запускает таймер на 1 минуту"""
    time.sleep(60)
    print("Время вышло. Программа завершена.")
    exit()

def main():
    # Создаем папку
    create_folder()
    
    # Получаем текст и имя файла от пользователя
    message = input("Введите сообщение для файлов (без специальных символов): ")
    if not is_valid_message(message):
        print("Ошибка: сообщение содержит специальные символы.")
        return

    base_filename = input("Введите начальное название файла: ")
    
    # Создаем файлы
    create_files(message, base_filename)

    # Запускаем таймер в отдельном потоке
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

    # Запрашиваем на удаление
    prompt_delete_files()

# Запускаем основную функцию
if __name__ == "__main__":
    main()
