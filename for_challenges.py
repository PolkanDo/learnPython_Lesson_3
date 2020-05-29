# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f"\t- {name}")


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    name_len = len(name)
    print(f"\t- {name}, len of name: {name_len};")


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    if is_male[name]:
        print(f"\t- {name} is male;")
    else:
        print(f"\t- {name} is female;")


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
num_groups = len(groups)
if num_groups == 1:
    print(f"Всего {num_groups} группa:")
elif num_groups < 5:
    print(f"Всего {num_groups} группы:")
else:
    print(f"Всего {num_groups} групп:")
for group in groups:
    num_people = len(group)
    if num_people == 1:
        print(f"\t - В группе {num_people} человек.")
    elif num_people < 5:
        print(f"\t - В группе {num_people} человека.")
    else:
        print(f"\t - В группе {num_people} людей.")

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
for group in groups:
    char_list = ', '.join(group)
    group_index = groups.index(group) + 1
    print(f"Группа {group_index}: {char_list}")
