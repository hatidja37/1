class House:
    def __init__(self, name, number_floor):
        self.name = name
        self._number_floor = number_floor

    # def go_to(self, new_floor):
    #
    #     # print(f"Название дома: {self.name}; Kол-во этажей в доме: {self._number_floor}")
    #     print(f"Какой этаж вызываем: {new_floor}")
    #     if 1 <= new_floor <= self._number_floor:
    #         while True:
    #             for i in range(1, new_floor + 1):
    #                 print(i)
    #             else:
    #                 break
    #     else:
    #         print('Такого этажа не существует')
    # def __len__(self):
    #     return self._number_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self._number_floor}"

    # if isinstance(other, int) and isinstance(other, House):

# 1. __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
    def __eq__(self, other):
        if isinstance(other, House): # isinstance(other, House) - other указывает на объект типа House.
            return self._number_floor == other._number_floor
        else:
            print(f'ведите "other" правильного формата')

# 2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения.
    def __lt__(self, other):
        if  isinstance(other, House):
            return self._number_floor < other._number_floor
    def __le__(self, other):
        if isinstance(other, House):
            return self._number_floor <= other._number_floor
    def __gt__(self, other):
        if isinstance(other, House):
            return self._number_floor > other._number_floor
    def __ge__(self, other):
        if isinstance(other, House):
            return self._number_floor >= other._number_floor
    def __ne__(self, other):
        if isinstance(other, House):
            return self._number_floor != other._number_floor

# 3. __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
    def __add__(self, value):
        if isinstance(value, int): # isinstance(other, int) - other указывает на объект типа int.
            self._number_floor+=value
            return self

# 4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
    def __radd__(self, value):
        if isinstance(value, int):
            self._number_floor+=value
            return self
    def __iadd__(self, value):
        if isinstance(value, int):
            self._number_floor+=value
            return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__