import inspect

def inspect_function(func):
    # Получаем имя функции
    func_name = func.__name__
    
    # Получаем информацию о сигнатуре функции
    func_signature = inspect.signature(func)
    
    print(f"Название функции: {func_name}")
    
    # Перебираем параметры функции
    for param_name, param in func_signature.parameters.items():
        # Определяем тип параметра (позиционный, ключевой и т.д.)
        if param.default == inspect.Parameter.empty:
            if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
                param_type = "позиционный или ключевой (обязательный)"
            elif param.kind == inspect.Parameter.VAR_POSITIONAL:
                param_type = "*аргументы (кортеж)"
            elif param.kind == inspect.Parameter.VAR_KEYWORD:
                param_type = "**ключевые аргументы (словарь)"
        else:
            if param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
                param_type = "позиционный или ключевой (с дефолтным значением)"
        
        # Выводим информацию о параметре
        print(f"Параметр: {param_name}, Тип: {param_type}")

# Пример функции для анализа
def sample_function(a, b, *args, c=10, **kwargs):
    pass

# Вызываем inspect_function для анализа sample_function
inspect_function(sample_function)
