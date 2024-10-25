#цикл while
while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: введите два целых числа!")


if a % 2 == 0:
    print(f"Первое число {a} - четное")
else:
    print(f"Первое число {a} - нечетное")

if b % 2 == 0:
    print(f"Второе число {b} - четное")
else:
    print(f"Второе число {b} - нечетное")


print(f"Последовательность Фибоначчи начинается с {a} и {b}:")
count = 0 
max_count = 10

while count < max_count:
    print(a, end=" ")

    a, b = b, a + b
    count += 1
