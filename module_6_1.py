# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if food.edible:
            # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
            print(f"{self.name} съел {food.name}")
            self.fed = True
        # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    def __init__(self, name, alive=True, fed=False):
        super().__init__(name, alive, fed)

class Predator (Animal):
    def __init__(self, name, alive = True, fed = False):
        super().__init__(name, alive, fed)
class Flower (Plant):
    def __init__(self, name, edible=False):
        super().__init__(name, edible)

class Fruit (Plant):
    def __init__(self, name, edible=True):
        super().__init__(name, edible)


a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')


print(a1.name)

print(p1.name)

print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)


