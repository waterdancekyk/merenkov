from datetime import datetime
from time import sleep

# Исправляем функцию, чтобы вычислять время внутри неё
def time_now(msg):
    dt = datetime.now()  # Берем текущее время при каждом вызове функции
    print(msg, dt)

# Пример вызова функции
time_now('ВРЕМЯ МОСКОВСКОЕ: ')
sleep(1)  # Задержка на 1 секунду
time_now('Секунды тикают, USERNAME: ')
sleep(1)  # Задержка на 1 секунду
time_now('Зачем я пошел на ИСП???? ')
