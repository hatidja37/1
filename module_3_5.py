def get_multiplied_digits(number):
    str_number=str(number)
    first=int(str_number[0])
    if number ==0:
        return 0
    else:
        if len(str_number)>1:
            result = first * get_multiplied_digits(int(str_number[1:]))
            return result
        if len(str_number) <= 1:
            return first
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)

# вывод:
# 24
# 0

# def get_multiplied_digits(number):
#     str_number=str(number)
#     first=int(str_number[0])
#     if number ==0:
#         return 1
#     else:
#         if len(str_number)>1:
#             result = first * get_multiplied_digits(int(str_number[1:]))
#             return result
#         if len(str_number) <= 1:
#             return first
# result = get_multiplied_digits(40203)
# print(result)
# result2 = get_multiplied_digits(402030)
# print(result2)
#
#  вывод:
#  24
#  24
