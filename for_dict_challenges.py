import collections

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

c = collections.Counter()
names = [student['first_name'] for student in students]
names = list(names)
for name in names:
    c[name] += 1
for name in set(names):
    print(f"{name}: {c[name]}")
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
c = collections.Counter()
names = [student['first_name'] for student in students]
names = list(names)
for name in names:
    c[name] += 1
a = dict(c.most_common(1))
for name in a.keys():
    print(f"Самое часто встречающееся имя в классе: {name}")

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
for students in school_students:
    class_number = school_students.index(students)+1
    c = collections.Counter()
    names = [student['first_name'] for student in students]
    names = list(names)
    for name in names:
        c[name] += 1
    a = dict(c.most_common(1))
    for name in a.keys():
        print(f"Самое часто встречающееся имя в классе {class_number}: {name}")
    
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


def get_gender(is_male, names):
    male = 0
    female = 0
    for name in names:
        if is_male[name]:
            male += 1
        else:
            female += 1
    return male, female


for class_info in school:
    for key, value in class_info.items():
        if key == 'students':
            names = [student['first_name'] for student in value]
            names = list(names)
            gender_nums = get_gender(is_male, names)
            print(f"В классе {class_info['class']}: {gender_nums[1]} девочек и {gender_nums[0]} мальчиков.")

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


def max_val(dictionary):
    m_val = max(dictionary.values())
    final_list = [k for k, v in dictionary.items() if v == m_val]
    return final_list[0]


boys = {}
girls = {}

for class_info in school:
    for key, value in class_info.items():
        if key == 'students':
            names = [student['first_name'] for student in value]
            names = list(names)
            gender_nums = get_gender(is_male, names)
            boys[class_info['class']] = gender_nums[0]
            girls[class_info['class']] = gender_nums[1]

print(f"Больше всего мальчиков в классе {max_val(boys)}")
print(f"Больше всего мальчиков в классе {max_val(girls)}")

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a