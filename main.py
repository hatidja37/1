print('Hi, PyCharm')
x = 43
y = 32
print(x * y)
print("End line")



# if '@' in sender and ('.com' in sender or '.ru' in sender or '.net' in sender):
#     return True
# Ну я бы вот скорее поступил вот так, явно проверяя каждый элемент.

# Можно попробовать через any(), которое проверяет наличие любого из элементов, внутри составив цикл.
# **
# if '@' in sender and any(ext in sender for ext in ['.com', '.ru', '.net']):
#     return True
# return False