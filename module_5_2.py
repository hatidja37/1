class House:
    def __init__(self, name, number_floor):
        self.name = name
        self._number_floor = number_floor

    def go_to(self, new_floor):

        # print(f"Название дома: {self.name}; Kол-во этажей в доме: {self._number_floor}")
        print(f"Какой этаж вызываем: {new_floor}")
        if 1 <= new_floor <= self._number_floor:
            while True:
                for i in range(1, new_floor + 1):
                    print(i)
                else:
                    break
        else:
            print('Такого этажа не существует')
    def __len__(self):
        return self._number_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self._number_floor}"

#
# h1 = House('ЖК Горский', 18)
#
# h2 = House('Домик в деревне', 2)
h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)
# h1.go_to(10)
#
# h2.go_to(3)
print(h1)

print(h2)
print(len(h1))

print(len(h2))