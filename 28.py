import random

class ConstructorGame:
    def __init__(self):
        self.superclass = "SuperClass"
        self.classes = [f"Class{i+1}" for i in range(8)]
        self.methods = [f"method{i+1}" for i in range(6)]
        self.chosen_classes = []
        self.chosen_methods = []
        self.program_template = ""

    def choose_program_type(self):
        print("Привет! Давайте создадим программу.")
        print("Выберите тип программы:")
        types = ["1. Игра", "2. Учётная система", "3. Школьный модуль"]
        for t in types:
            print(t)
        choice = input("Введите номер типа программы: ")
        return choice

    def choose_classes_methods(self):
        num_classes = int(input("Сколько классов вы хотите использовать? (от 1 до 8): "))
        num_methods = int(input("Сколько методов использовать в каждом классе? (от 1 до 6): "))

        # Выбираем случайные классы и методы
        self.chosen_classes = random.sample(self.classes, num_classes)
        self.chosen_methods = random.sample(self.methods, num_methods)
        
        print(f"Вы выбрали {num_classes} классов и {num_methods} методов.")

    def create_template(self, program_type):
        if program_type == '1':
            self.program_template += "Программа: Игра\n"
        elif program_type == '2':
            self.program_template += "Программа: Учётная система\n"
        else:
            self.program_template += "Программа: Школьный модуль\n"
        
        self.program_template += f"\nclass {self.superclass}:\n"
        self.program_template += "    def __init__(self):\n        pass\n\n"
        
        for cls in self.chosen_classes:
            self.program_template += f"class {cls}({self.superclass}):\n"
            self.program_template += "    def __init__(self):\n        super().__init__()\n\n"
            
            for method in self.chosen_methods:
                self.program_template += f"    def {method}(self):\n"
                self.program_template += "        # Реализовать логику метода\n"
                self.program_template += "        pass\n\n"
                
    def show_template(self):
        print("\nВаша программа:")
        print(self.program_template)
    
    def play(self):
        program_type = self.choose_program_type()
        self.choose_classes_methods()
        self.create_template(program_type)
        self.show_template()
        print("\nИгра окончена. Вы создали базовый шаблон кода. Удачи в программировании!")
        
# Запуск игры
game = ConstructorGame()
game.play()
