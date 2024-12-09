first=int(input('введите первое число:'))
second=int(input('введите второе число:'))
third=int(input('введите третье число:'))

if first==second and first==third:
    print(3)
else:
    if first==second:
        print(2)
    elif second==third:
        print(2)
    elif first==third:
        print(2)
    else: print(0)

# Улучшенный вариант:

# Ввод данных и приведение к целым числам
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
# Создадим множество из введённых чисел
numbers = {first, second, third}
# Определим количество уникальных чисел
unique_value = len(numbers)
# Выведем результат:
if unique_value == 1:
    print(3)
elif unique_value == 2:
    print(2)
else:
    print(0)

# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0
#
