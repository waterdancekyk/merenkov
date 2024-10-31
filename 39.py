class Game:
    def __init__(self):
        self.rooms = {
            "Комната 1": {
                "Loot Bag 1": ["Меч", "Щит", "Зелье"],
                "Loot Bag 2": ["Камень", "Ключ", "Книга"],
                "Loot Bag 3": ["Доспехи", "Лук", "Стрелы"]
            },
            "Комната 2": {
                "Loot Bag 1": ["Яблоко", "Груша", "Виноград"],
                "Loot Bag 2": ["Суп", "Мясо", "Хлеб"],
                "Loot Bag 3": ["Торт", "Мороженое", "Пирог"]
            },
            "Комната 3": {
                "Loot Bag 1": ["Факел", "Карта", "Компас"],
                "Loot Bag 2": ["Спички", "Палатка", "Бутылка"],
                "Loot Bag 3": ["Лопата", "Топор", "Мотыга"]
            },
            "Комната 4": {
                "Loot Bag 1": ["Леденец", "Конфета", "Карамель"],
                "Loot Bag 2": ["Пушка", "Патроны", "Рюкзак"],
                "Loot Bag 3": ["Переключатель", "Провод", "Светильник"]
            },
        }
        self.current_room = "Комната 1"
        self.inventory = []

    def display_rooms(self):
        print("Вы находитесь в:", self.current_room)
        print("Доступные мешки с лутом:")
        for loot_bag, items in self.rooms[self.current_room].items():
            print(f"{loot_bag}: {', '.join(items)}")

    def take_item(self, item):
        for loot_bag, items in self.rooms[self.current_room].items():
            if item in items:
                items.remove(item)
                self.inventory.append(item)
                print(f"Вы взяли: {item}")
                return
        print("Этот предмет не найден в мешках с лутом.")

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.rooms[self.current_room][f"Loot Bag {len(self.rooms[self.current_room])}"].append(item)  # Добавляем в последний мешок
            print(f"Вы оставили: {item}")
        else:
            print("У вас нет такого предмета.")

    def move_to_room(self, room_name):
        if room_name in self.rooms:
            self.current_room = room_name
            print(f"Вы переместились в {self.current_room}.")
        else:
            print("Такой комнаты не существует.")

    def play(self):
        while True:
            self.display_rooms()
            print("Ваш инвентарь:", self.inventory)
            action = input("Выберите действие (взять <предмет>, оставить <предмет>, переместиться <комната>, выйти): ").strip().lower()

            if action.startswith("взять"):
                item = action.split(" ")[1]
                self.take_item(item)
            elif action.startswith("оставить"):
                item = action.split(" ")[1]
                self.drop_item(item)
            elif action.startswith("переместиться"):
                room_name = action.split(" ")[1]
                self.move_to_room(room_name)
            elif action == "выйти":
                print("Вы вышли из игры.")
                break
            else:
                print("Неверная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    game = Game()
    game.play()
