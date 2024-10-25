from datetime import datetime

def get_weekday(date):
    """Возвращает день недели для данной даты в виде строки."""
    return date.strftime("%A")

def main():
    # Запрашиваем даты у пользователя
    while True:
        try:
            date_input_1 = input("Введите первую дату (в формате ГГГГ-ММ-ДД): ")
            date_input_2 = input("Введите вторую дату (в формате ГГГГ-ММ-ДД): ")

            # Преобразуем ввод в объекты datetime
            date_1 = datetime.strptime(date_input_1, "%Y-%m-%d")
            date_2 = datetime.strptime(date_input_2, "%Y-%m-%d")
            break  # Выходим из цикла, если ввод успешен

        except ValueError:
            print("Ошибка: Введите дату в правильном формате (ГГГГ-ММ-ДД). Попробуйте снова.")

    # Создаем список с кортежами (дата, день недели)
    dates_with_weekdays = [
        (date_1, get_weekday(date_1)),
        (date_2, get_weekday(date_2)),
    ]

    # Сортируем по дням недели в алфавитном порядке
    sorted_dates = sorted(dates_with_weekdays, key=lambda x: x[1])

    # Выводим отсортированные даты и дни недели
    print("\nОтсортированные даты по дням недели:")
    for date, weekday in sorted_dates:
        print(f"{date.strftime('%Y-%m-%d')} - {weekday}")

# Запускаем программу
if __name__ == "__main__":
    main()
