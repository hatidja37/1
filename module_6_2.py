class ColorVariants:
    """Класс, представляющий возможные варианты цвета."""
    VAR_COLORS = ["White", "Red", "Blue", "Green", "Black"]


class Vehicle:

    def __init__(self, owner: str, _model: str, _engine_power: int, _color: str):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color
        self.color_variants = ColorVariants.VAR_COLORS

    def get_model(self):
        return self._model

    def get_horsepower(self):
        return self._engine_power

    def get_color(self):
        return self._color

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in map(str.lower, ColorVariants.VAR_COLORS):
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    def __init__(self, owner: str, _model: str, _engine_power: int, _color: str):
        super().__init__(owner, _model, _engine_power, _color)
        self.__PASSENGERS_LIMIT = 5



sedan = Sedan("Иван Иванов", "Toyota Camry", 150, "Silver")

sedan.print_info()      # Напечатает всю информацию об автомобиле
sedan.set_color("red")  # Попытается установить новый цвет автомобиля
sedan.print_info()
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()