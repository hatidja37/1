class House:
    houses_history = []

    def __new__(cls, name, number_floor):
        instance = super().__new__(cls)
        cls.houses_history.append(name)
        return instance

    def __init__(self, name, number_floor):
        self.name = name
        self._number_floor = number_floor

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

del h2

del h3

print(House.houses_history)

