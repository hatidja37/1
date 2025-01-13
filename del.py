class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls._instance

# Пример использования
class MyClass(Singleton):
    def print_message(self):
        print("Hello, World!")

obj1 = MyClass()
obj2 = MyClass()

assert obj1 is obj2  # Оба объекта ссылаются на один и тот же экземпляр

my_class_instance = MyClass.get_instance()
my_class_instance.print_message()  # Выводит "Hello, World!"