class Game:
    def __init__(self):
        self.projects = {
            "Парковка": {
                "classes": ["Vehicle", "Car", "Truck", "Bus", "ParkingLot"],
                "functions": ["park_vehicle", "calculate_fee"]
            },
            "Магазин": {
                "classes": ["Product", "Cart", "Customer", "Order"],
                "functions": ["add_to_cart", "checkout"]
            },
            "Игровая площадка": {
                "classes": ["Game", "Player", "Scoreboard"],
                "functions": ["start_game", "end_game"]
            }
        }

    def choose_project(self):
        print("Выберите проект:", ", ".join(self.projects.keys()))
        project = input("Введите название проекта: ")
        return self.projects.get(project, None)

    def build_program(self, project):
        print("Выберите классы:", ", ".join(project['classes']))
        classes = input("Введите выбранные классы через запятую: ").split(',')
        
        print("Выберите функции:", ", ".join(project['functions']))
        functions = input("Введите выбранные функции через запятую: ").split(',')

        return classes, functions

    def run(self):
        project = self.choose_project()
        if project:
            classes, functions = self.build_program(project)
            print("Вы собрали программу с классами:", classes, "и функциями:", functions)
        else:
            print("Неверный выбор проекта.")

# Запуск игры
game = Game()
game.run()
