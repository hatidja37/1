def deep_sum(data):
    total = 0
    if isinstance(data, (int, float)):
        return data
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            total += len(key) + deep_sum(value)
    elif isinstance(data, (list, tuple, set)):
        for element in data:
            total += deep_sum(element)
    return total


data_structure = ([
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
])

print(deep_sum(data_structure))


# data_structure = [
#
#   [1, 2, 3],
#
#   {'a': 4, 'b': 5},
#
#   (6, {'cube': 7, 'drum': 8}),
#
#   "Hello",
#
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
#
# ]
#
#
#
# def summa(*args):
#     # Базовый случай
#     if not args:
#         return 0
#
#     s = 0
#
#     for arg in args:
#         if isinstance(arg, set):
#             s += sum(set(arg))
#         elif isinstance(arg, list):
#             s += sum(arg)
#         elif isinstance(arg, dict):
#             total = 0
#             for key, value in arg.items():
#                 total += len(key)+value
#             s += total
#         elif isinstance(arg, str):
#             s += len(arg)
#         elif isinstance(arg, tuple):
#             s += sum(arg)
#         else:
#             s += arg
#
#     return s
#
# def sum_list_elements(lst):
#     total = 0
#     for item in lst:
#         if isinstance(item, list):
#             total += sum_list_elements(item)
#         else:
#             total += item
#     return total
#
#
# data_structure = [[1, 2], {'a': 3}, "abc", (4, 5)]
# print(summa(data_structure))





# НАДО: найти сумму всех чисел и сумм длин всех строк
# обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
#  -нельзя использовать индексацию и обращение по ключам
#
# Что должно быть подсчитано:
#
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
#
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
#
# Выходные данные (консоль):
# 99
#
# Примечания (рекомендации):

# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.