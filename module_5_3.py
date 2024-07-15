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
    def __eq__(self, other):
        return self.floors == other
    def __lt__(self, other):
        return self.floors < other.floors
    def __le__(self, other):
        return self.floors <= other.floors
    def __gt__(self, other):
        return self.floors > other.floors
    def __ge__(self, other):
        return self.floors >= other.floors
    def __ne__(self, other):
        return self.floors != other.floors
    def __add__(self, other):
        return self.floors + other


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1.floors == h2.floors)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2.floors
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)