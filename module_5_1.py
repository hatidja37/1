class House:
     def __init__(self, name, number_floor):
         self.name=name
         self.number_floor=number_floor

     def go_to(self,new_floor):

         print(f"Название дома: {self.name}; Kол-во этажей в доме: {self.number_floor}")
         print(f"Какой этаж вызываем: {new_floor}")
         if 1 <= new_floor <= self.number_floor:
             while True:
                 for i in range(1,new_floor+1):
                     print(i)
                 else:
                     break
         else:
             print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(10)

h2.go_to(3)
