class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
    def go_to(self, new_floor):
        a = 1
        if new_floor > self.floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            while a <= new_floor:
                print(a)
                a = a+1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(8)
h2.go_to(10)
