# def test_function(a):
#     print(a)
#     def inner_function(x):
#         b = x+1
#         print(b)
#         print("Я в области видимости функции test_function")
#
# inner_function(2)
# test_function(5)
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# ==> NameError: name 'inner_function' is not defined [ имя функции находится в локальном пространстве имен, поэтому не доступно в глобальном пространстве имен вне функции test_function]
#  Внутренние функции имеют ограниченную область видимости и доступны только внутри внешней функции, в которой они определены.



def test_function(a):
    print(a)
    def inner_function(x):
        b = x+1
        print(b)
        print("Я в области видимости функции test_function")

    inner_function(2)
test_function(5)

