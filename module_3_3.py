def print_params(a=1, b='строка', c=True):
    print(a, b, c)
# 1
print_params()
print_params(b=1,c=0)
print_params(b=25)
print_params(c = [1,2,3])
print()
# 2
values_list=['пример', False, {1,3,5}]
values_dict={"a":3, "b":(4,5,6), "c":[10,20]}
print_params(*values_list)
print_params(**values_dict)
print()
# 3
values_list_2=[[3,7,9], {1,3,5}]
print_params(*values_list_2, 42)


