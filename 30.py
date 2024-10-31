students = [
    {"name": "Alice", "grades": [80, 85, 90]},
    {"name": "Bob", "grades": [70, 75, 78]},
    {"name": "Charlie", "grades": [90, 92, 85]}
]

def average(grades):
    return sum(grades) / len(grades)

def best_student(students):
    best = None
    max_average = -float("inf")  # Устанавливаем начальное значение на минус бесконечность
    for student in students:
        avg = average(student["grades"])
        if avg > max_average:
            best = student
            max_average = avg
    return best

def print_results(students):
    for student in students:
        print(f"Student: {student['name']}, Average grade: {average(student['grades'])}")
    best = best_student(students)
    if best:
        print(f"Best student: {best['name']}, Average grade: {average(best['grades'])}")

# Основная программа
def main():
    print_results(students)

# Запуск основной функции
if __name__ == "__main__":
    main()
