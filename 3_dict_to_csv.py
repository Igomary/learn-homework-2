"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people =   [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Сергй', 'age': 15, 'job': 'Музыкант'}
    ]

    with open('people_dict.csv', 'w') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for each in people:
            writer.writerow(each)

if __name__ == "__main__":
    main()
