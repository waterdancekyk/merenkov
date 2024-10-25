def happy_three_args(*, var1=None, var2=None, var3=None):
    # Проверяем, что ни один из параметров не равен None
    if var1 is not None and var2 is not None and var3 is not None:
        print(f"Переданы в функцию аргументы: var1 = {var1}, var2 = {var2}, var3 = {var3}")
    else:
        # Создаем список для аргументов, которые не равны None
        passed_args = []
        if var1 is not None:
            passed_args.append(f"var1 = {var1}")
        if var2 is not None:
            passed_args.append(f"var2 = {var2}")
        if var3 is not None:
            passed_args.append(f"var3 = {var3}")
        
        # Формируем итоговое сообщение с переданными аргументами
        if passed_args:
            print("Переданы в функцию аргументы: " + ", ".join(passed_args))
        else:
            print("Ни один аргумент не был передан.")

# Пример вызова функции
happy_three_args(var1=2, var3=10)
