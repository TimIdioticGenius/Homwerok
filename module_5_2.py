class House:
    def __len__(self):
        return self.floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей:{self.floors}"
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

print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))