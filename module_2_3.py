my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
variable=0
final_list=[]
while variable < len(my_list):
    value = my_list[variable]
    if value > 0:
        final_list.append(my_list[variable])
        # print(my_list[variable])
        variable = variable + 1
    elif my_list[variable] == 0:
        variable = variable + 1
        continue
    else:
        break

print(final_list)
