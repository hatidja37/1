def get_multiplied_digits(number):
    str_number=str(number)     # Преобразуем число в строку для удобной работы с цифрами
    first=int(str_number[0])   # Берем первую цифру числа
    if len(str_number) ==2 and int(str_number[1]) %10 == 0:   #Базовый случай: если длина строки равна 2 и без остатка делится на 10, возвращаем первую цифру
        return first
    else:
        if len(str_number)>1:
            result = first * get_multiplied_digits(int(str_number[1:]))    # Возвращаем произведение первой цифры и результата рекурсии
            return result
        if len(str_number) <= 1:
            return first
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)




# Я бы начал с описания рекурсивного случая, а всё, что в него не входит - оставил на базовый.
#
# Собственно в рекурсивном случае я бы указал, что если длина строки больше 1 - то считаем рекурсивный случай.
#
# А в базовом может быть:
# if first != 0:
#    return first

# def get_multiplied_digits(number):
#     str_number=str(number)     # Преобразуем число в строку для удобной работы с цифрами
#     first=int(str_number[0])   # Берем первую цифру числа
#     if len(str_number)>1:
#         result = first * get_multiplied_digits(int(str_number[1:]))    # Возвращаем произведение первой цифры и результата рекурсии
#         return result
#     if len(str_number) <= 1:
#         return first
#     else:
#         first != 0:  # Базовый случай: если первая цифра не ноль
#         return first
# result = get_multiplied_digits(40203)
# print(result)
# result2 = get_multiplied_digits(402030)
# print(result2)

def get_multiplied_digits(number):
    str_number=str(number)     # Преобразуем число в строку для удобной работы с цифрами
    first=int(str_number[0])   # Берем первую цифру числа
    if first != 0:  # Базовый случай: если первая цифра не ноль
        return first
    else:
        if len(str_number)>1:
            result = first * get_multiplied_digits(int(str_number[1:]))    # Возвращаем произведение первой цифры и результата рекурсии
            return result
        if len(str_number) <= 1:
            return first
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)