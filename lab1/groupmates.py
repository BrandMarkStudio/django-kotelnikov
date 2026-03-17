import django
groupmates = [
    {"name": "Аня", "group": "2251", "age": 20, "marks": [5, 4, 5]},
    {"name": "Иван", "group": "2251", "age": 21, "marks": [4, 4, 5]},
    {"name": "Виктор", "group": "2251", "age": 20, "marks": [5, 4, 3]},
    {"name": "Даниил", "group": "2251", "age": 21, "marks": [3, 4, 5]},
]

# Функция фильтрации студентов по средней оценке
def filter_students_by_average(students, min_average):
    """
    Фильтрует студентов по средней оценке.
    
    :param students: список словарей с информацией о студентах
    :param min_average: минимальная средняя оценка для фильтрации
    :return: список студентов, у которых средний балл выше min_average
    """
    filtered_students = []  # Пустой список для студентов, прошедших фильтр
    
    for student in students:
        marks = student.get("marks", [])
        if not marks:
            continue  # если оценок нет, пропускаем
        average = sum(marks) / len(marks)
        if average > min_average:
            filtered_students.append(student)
    
    return filtered_students

# Функция вывода студентов в виде таблицы
def print_students(students):
    """
    Выводит список студентов в виде таблицы.
    """
    print(f"{'Имя студента':15} {'Группа':8} {'Возраст':8} {'Оценки':20} {'Средний балл':15}")
    for student in students:
        avg = sum(student['marks']) / len(student['marks']) if student['marks'] else 0
        marks_str = ", ".join(str(m) for m in student['marks'])
        print(f"{student['name']:15} {student['group']:8} {student['age']:8} {marks_str:20} {avg:15.2f}")
    print("\n")

# Пример использования
min_avg = 4.0  # Порог фильтрации
top_students = filter_students_by_average(groupmates, min_avg)
print_students(top_students)