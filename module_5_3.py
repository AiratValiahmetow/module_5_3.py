class House:
    def __init__(self, name, number_of_floors,):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        for k in (range(new_floor)):
            k += 1
            if new_floor > self.number_of_floors or new_floor < 1:
                 print("Такого этажа не существует")
                 break
            else:
                 print(k)

    def __len__(self):
            return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors} '

    def __eq__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
            if isinstance(value, int):
                self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
            return self.__add__(value)

    def __iadd__(self, value):
            if isinstance(value, int):
                self.number_of_floors += value
            return self











h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#__str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)