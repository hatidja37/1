def get_matrix(n,m,value):
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)

result2 = get_matrix(3, 5, 42)

result3 = get_matrix(4, 2, 13)

print(result1)

print(result2)

print(result3)

#В вашем выводе возникают пустые списки в начале некоторых строк. Это может указывать на проблему с созданием матриц.
# Проблема может заключаться в том, что в некоторых случаях конструкция range не охватывает все необходимые элементы. В результате этого пустые списки появляются там, где не должно быть значений. Исправить это можно, добавив проверку на полное прохождение диапазонов в циклах.


# Исправленная версия
def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result1 = get_matrix(2, 2, 10)

result2 = get_matrix(3, 5, 42)

result3 = get_matrix(4, 2, 13)

print(result1)

print(result2)

print(result3)


