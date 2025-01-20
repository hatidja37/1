import random
class Animal:
    # Атрибуты класса
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        # Индивидуальные атрибуты объекта
        self._cords = [0, 0, 0]
        self.speed = speed


    def move(self, x, y, z):
        dz = self._cords[2] + self.speed * z
        if dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += self.speed * x
            self._cords[1] += self.speed * y
            self._cords[2] = dz

    def get_cords(self):
        print(f"X:{self._cords[0]},Y:{self._cords[1]},Z:{self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER<5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound is not None:
            print(f"Sound: {self.sound}")
        else:
            print("I don't have a sound.")

class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):

        how_many_eggs=random.randint(1, 4)
        print(f"Here are(is) {how_many_eggs} eggs for you")

class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):

        self.dz = abs(self._cords[2])
        self.speed = self.speed * 0.5
        # Уменьшение координаты z на значение self.dz. Это заставляет объект погружаться вниз.
        self._cords[2] -= self.dz

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)


class Duckbill(PoisonousAnimal,  AquaticAnimal, Bird):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound="Click-click-click"


# Создание экземпляра класса Duckbill
db = Duckbill(10)

# Тестирование
# print(Duckbill.mro())
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()




# Вывод на консоль:
#
# True
#
# True
#
# Click-click-click
#
# Be careful, i'm attacking you 0_0
#
# X: 10 Y: 20 Z: 30
#
# X: 10 Y: 20 Z: 0
#
# Here are(is) 3 eggs for you # Число может быть другим (1-4)
