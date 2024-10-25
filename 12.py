# Класс Студент
class Student:
    def __init__(self, name, missed_classes):
        self.name = name
        self.missed_classes = missed_classes  # Количество пропущенных занятий
    
    def calculate_penalty(self):
        """Метод для расчета штрафа за пропуски занятий"""
        penalty = self.missed_classes * 100  # Штраф за каждое пропущенное занятие 100 единиц
        return penalty

# Класс Работник
class Worker:
    def __init__(self, base_salary):
        self.base_salary = base_salary  # Базовая зарплата
    
    def calculate_salary(self):
        """Метод для расчета базовой зарплаты"""
        return self.base_salary

# Класс Работающий_студент, наследует от Студента и Работника
class WorkingStudent(Student, Worker):
    def __init__(self, name, missed_classes, base_salary):
        # Инициализируем родительские классы
        Student.__init__(self, name, missed_classes)
        Worker.__init__(self, base_salary)
    
    def calculate_final_salary(self):
        """Метод для расчета финальной зарплаты с учетом штрафов"""
        base_salary = self.calculate_salary()  # Базовая зарплата
        penalty = self.calculate_penalty()  # Штраф за пропуски
        final_salary = base_salary - penalty  # Финальная зарплата
        return final_salary if final_salary > 0 else 0  # Зарплата не может быть отрицательной

# Пример использования программы
def main():
    # Ввод данных от пользователя
    name = input("Введите имя студента: ")
    missed_classes = int(input("Введите количество пропущенных занятий: "))
    base_salary = float(input("Введите базовую зарплату: "))

    # Создаем объект Работающего студента
    working_student = WorkingStudent(name, missed_classes, base_salary)

    # Рассчитываем финальную зарплату
    final_salary = working_student.calculate_final_salary()

    # Выводим результат
    print(f"Студент {working_student.name} пропустил {working_student.missed_classes} занятий.")
    print(f"Финальная зарплата с учетом пропусков: {final_salary:.2f}")

# Запуск программы
if __name__ == "__main__":
    main()
