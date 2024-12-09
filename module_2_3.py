# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# variable=0
# while variable < len(my_list):
#     value = my_list[variable]
#     if value > 0:
#         my_list_new =[]
#         my_list_new.append(value)
#         variable = variable+1
#         print(my_list_new)
#     elif my_list[variable] == 0:
#         variable = variable + 1
#         continue
#     else:
#         break

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
variable=0
while variable < len(my_list):
    value = my_list[variable]
    if value > 0:
        print(my_list[variable])
        variable = variable + 1
    elif my_list[variable] == 0:
        variable = variable + 1
        continue
    else:
        break




# Вывод на консоль:
#
# 42
# 69
# 322
# 13
# 99