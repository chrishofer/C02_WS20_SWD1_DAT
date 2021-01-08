import abc

# TODO:
#
# Blatt 5 Beispiel 2
#     get_salary_by_department() -> dict[str, float]
#
# Prüfungsablauf

# in anderen statischen programmiersprachen
class Things():
    def __init__(self):
        self.var = 12 # public variable
        self._prot_var = 22 # protectd variables
        self.__priv_var = 33 # privat und namge gemangled
    def make_noise(self):
        pass
    def __repr__(self):
        return f'Things var={self.var} _prot_var={self._prot_var} __priv_var={self.__priv_var}'
    def __str__(self):
        return f'Things({self.var})'

# und alle müssten davon erben und dann könnten wir über
# eine liste von Things iterieren

class Dog(Things):
    def __init__(self):
        super().__init__()
        self._prot_var
        self.__priv_var = 55

    def make_noise(self):
        print("wuff wuff")

class Human:
    def make_noise(self):
        print("Hello")
    def make_hello(self):
        print("Hello")


class Car:
    def make_noise(self):
        print("brumm brumm")


# Abstrakte Klassen ermöglichen uns ein gemeinsames Interface oder Schnittstelle zu definieren
# gibt vor welche Methoden/Eigenschaften alle davon abgeleiteten Kindklassen haben müssen
# wir können keine instanzen von abstrakten klassen anlegen

class Konto(abc.ABC):
    def __init__(self):
        self.balance = 0

    def set_to_zero(self):
        self.balance = 0

    @abc.abstractmethod
    def calc_interest(self):
        pass

    @abc.abstractmethod
    def deposit(self):
        pass


class SparKonto(Konto):

    def calc_interest(self):
        pass

    def deposit(self):
        pass

# Beispiel für property
# var1 ein property mit get/set
# var 2 nur ein get property
class PropTest():
    @property
    def var1(self): # lesender zugriff (getter) auf var1
        return self.__var1

    @var1.setter
    def var1(self, value): # schreibender zugriff (setter) auf var1
        # ich möchte nur positive werte zuweisen - sonst auf 0 zuweisen
        if value < 0:
            self.__var1 = 0
        else:
            self.__var1 = value

    @property
    def var2(self): # nur lesen von außen zugreifen
        return self.__var2

    def __init__(self, var1, var2):
        self.var1 = var1 # hier kann ich schon mit . und ohne __ zugreifen
        self.__var2 = var2 # wenn property nur getter dann müssen wir in klasse auch direkt auf die private var zugreifen
    def print_var(self):
        print(f'{self.var1} {self.var2}')

if __name__ == '__main__':
    pt = PropTest(-20, 10)
    pt.print_var()


    # k = Konto() # geht nicht
    #s = SparKonto()
    d = Dog()
    h = Human()
    c = Car()
    l = [d, h, c]
    # jetzt machen wir party und jeder macht ein geraeusch
    d.make_noise()
    h.make_noise()
    c.make_noise()

    for objekt in l:
        objekt.make_noise()


    d = {'Steffi': 100}
    print(d.get('Steffi'))
    print(d.get('Hansi', 0)) # wenn kein Hansi key dann liefer zweiten Parameter retour, dict wird nicht verändert
    print(d)

    print(d.setdefault("Steffi", 0))
    print(d.setdefault("Hansi", 0)) # unterschied - trägt wert auch gleich in dict ein
    print(d)

