present_students = [1, 2, 3, 4, 5]
sleeping_students = [2, 4, 6]

# Находим студентов, которые присутствуют и спят на лекции
actually_sleeping = [student for student in sleeping_students if student in present_students]

print("Студенты, которые спят на лекции:", actually_sleeping)
