class House:
    houses_history = []
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
        return self.floors

    def __new__(cls, *args, **kwargs):
        cls.houses_history = cls.houses_history + list(args[0:1])
        return super().__new__(cls)
    def __del__(self):
        print(self.name,' снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
