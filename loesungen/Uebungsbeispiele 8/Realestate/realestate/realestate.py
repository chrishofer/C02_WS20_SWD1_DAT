import abc
from typing import List, Dict


class RealEstate(abc.ABC):
    def __init__(self, square_meter: float):
        self.square_meter = square_meter

    @property
    def square_meter(self):
        return self.__square_meter

    @square_meter.setter
    def square_meter(self, value):
        self.__square_meter = value

    @property
    def category(self) -> int:
        return int(self.square_meter / 10)

    @abc.abstractmethod
    def calc_lease(self) -> float:
        pass

    def __repr__(self):
        return f'RealEstate {self.square_meter}'


class Office(RealEstate):
    def __init__(self, square_meter: float, people: int):
        super().__init__(square_meter)
        self.__people = people

    def __repr__(self):
        return f'Office {self.square_meter} für {self.__people} Personen'


    def calc_lease(self) -> float:
        if self.__people < 50:
            return self.square_meter * 8
        elif self.people < 100:
            return self.square_meter * 8.2 + 90
        elif self.people >= 100:
            return self.square_meter * 8.5 + self.__people


class Flat(RealEstate):
    def __init__(self, square_meter: float, count_room: int, type: str):
        super().__init__(square_meter)
        self.__count_room = count_room
        self.__type = type

    def __repr__(self):
        return f'Flat {self.square_meter} mit {self.__count_room} Räumen vom Typ {self.__type}'

    def calc_lease(self) -> float:
        if self.__type == "Low":
            return self.square_meter * 7
        elif self.__type == "Standard":
            return self.square_meter * 7.5 + self.__count_room * 10
        elif self.__type == "High":
            return self.square_meter * 8 + self.__count_room * 12
        return -1

class House(RealEstate):
    def __init__(self, square_meter: float, garden: bool):
        super().__init__(square_meter)
        self.__garden = garden

    def __repr__(self):
        return f'House {self.square_meter} Garten {self.__garden} '

    def calc_lease(self) -> float:
        if self.__garden:
            l = self.square_meter * 10 + 200
        else:
            l = self.square_meter * 15

        if l < 1000:
            return 1000
        return l

class Accounting():
    def __init__(self):
        self.__real_estates = []

    def add(self, re: RealEstate):
        self.__real_estates.append(re)

    def print_all(self):
        for e in self.__real_estates:
            print(e)

    def get_overall_lease(self) -> float:
        s = 0
        for e in self.__real_estates:
            s += e.calc_lease()

        return s

    def get_real_estate_in_category(self) -> Dict[int, int]:
        erg = {}
        for e in self.__real_estates:
            cat = e.category

            erg[cat] = 1 + erg.get(cat, 0)

        return erg

if __name__ == '__main__':
    a = Accounting()

    a.add(House(30, True))
    a.add(House(60, True))
    a.add(Flat(60, 3, "Standard"))
    a.add(Office(100, 10))
    a.print_all()
    print(a.get_real_estate_in_category())