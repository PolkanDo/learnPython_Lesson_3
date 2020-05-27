import csv

people =[
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Толя', 'age': 30, 'job': 'Pilot'}
    ]

with open('users.csv', 'w', encoding='utf-8', newline="") as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in people:
        writer.writerow(user)