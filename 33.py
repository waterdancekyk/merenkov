import numpy as np

class TransportProblem:
    def __init__(self, supply, demand, costs):
        self.supply = supply          # Список поставок от каждого источника
        self.demand = demand          # Список потребностей для каждого пункта назначения
        self.costs = costs            # Матрица затрат на перевозку
        self.n_sources = len(supply)  # Количество источников
        self.n_destinations = len(demand)  # Количество пунктов назначения
        self.solution = np.zeros((self.n_sources, self.n_destinations))  # Решение задачи

    def solve(self):
        # Начальное распределение (метод северо-западного угла)
        supply = self.supply.copy()
        demand = self.demand.copy()

        for i in range(self.n_sources):
            for j in range(self.n_destinations):
                if supply[i] > 0 and demand[j] > 0:
                    # Определяем количество товаров для перевозки
                    quantity = min(supply[i], demand[j])
                    self.solution[i][j] = quantity  # Заполняем решение
                    supply[i] -= quantity  # Уменьшаем поставку
                    demand[j] -= quantity  # Уменьшаем потребность

        return self.solution

    def total_cost(self):
        # Подсчет общей стоимости доставки
        total = 0
        for i in range(self.n_sources):
            for j in range(self.n_destinations):
                total += self.solution[i][j] * self.costs[i][j]
        return total

# Пример данных для задачи
supply = [20, 30, 25]  # Поставки от 3 источников
demand = [10, 25, 40]  # Потребности для 3 пунктов назначения
costs = [[8, 6, 10],    # Затраты от 1 источника к пунктам назначения
         [9, 12, 13],   # Затраты от 2 источника к пунктам назначения
         [14, 9, 16]]   # Затраты от 3 источника к пунктам назначения

# Создание и решение задачи
problem = TransportProblem(supply, demand, costs)
solution = problem.solve()

# Вывод результатов
print("Оптимальное распределение:")
print(solution)
print("Общая стоимость доставки:", problem.total_cost())
