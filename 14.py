def add_task(schedule, new_start, new_end):
    # Добавляем новую задачу в расписание
    schedule.append((new_start, new_end))
    
    # Сортируем расписание по времени старта
    schedule.sort(key=lambda x: x[0])
    
    # Обновляем интервалы занятости
    merged_schedule = []
    current_start, current_end = schedule[0]
    
    for start, end in schedule[1:]:
        if start <= current_end:  # Если интервалы пересекаются
            current_end = max(current_end, end)  # Объединяем их
        else:
            merged_schedule.append((current_start, current_end))
            current_start, current_end = start, end
    
    # Добавляем последний интервал
    merged_schedule.append((current_start, current_end))
    
    return merged_schedule

# Изначальное расписание
schedule = [(8, 15), (18, 22), (23, 24)]  # 23 до 24 = 23 до 7 следующего дня

# Пример добавления новой задачи
new_task_start = 17
new_task_end = 20

# Обновляем расписание
updated_schedule = add_task(schedule, new_task_start, new_task_end)

# Выводим обновленное расписание
print("Обновленное расписание:")
for start, end in updated_schedule:
    print(f"С {start} до {end}")
