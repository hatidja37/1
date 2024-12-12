number = int(input('введите число от 3 до 20:'))
# print(number, '-')
keys= []
for i in range(1, 21):
    for j in range(1, 21):
        if number % (i + j) == 0:
            while i != j:
                # value = f'{i}{j}'  # Преобразуем пару чисел в строку без пробела
                # keys.append(value)
                keys.append((i, j))
                break
#             else:
#                 continue
#         else:
#             continue
# # print(keys)
# # result=keys
# # print(*result)


def get_unique_results(pairs):
    seen = set() # для хранения всех пар, которые уже были просмотрены
    unique_pairs = []

    for pair in pairs:
        if pair not in seen:
            unique_pairs.append(pair)
            seen.add(pair)
            seen.add((pair[1], pair[0])) # добавление зеркального отображения пары в множество seen

    return unique_pairs

unique_pairs = get_unique_results(keys)
# Метод join объединяет элементы списка в строку без пробелов и запятых
result = ''.join([f"{x}{y}" for x, y in unique_pairs])

print(number, '-', result)

