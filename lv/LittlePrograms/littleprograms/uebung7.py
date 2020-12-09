class Hund:  # Name in großge. CamelCase

    species = 'Canis lupus familiaris'  # Klassenattri.
    zaehler = 0  # soll mitzählen wie viele objekte gerade leben

    @classmethod
    def get_anzahl_hunde(cls):
        return cls.zaehler

    def __init__(self, name: str, age: str):  # Zum Initialisieren
        self.__name = name  # Achtung da nur getter existiert müssen wir direkt auf __ zugreifen
        self.age = age
        self._gefuettert = False  # protect Attribut
        self.__gassi_gegangen = True  # private Attribut
        Hund.zaehler += 1

    @property
    def age(self):
        print("age getter aufgerufen")
        return self.__alter

    @age.setter
    def age(self, value):
        print("age setter aufgerufen")
        self.__alter = value

    @property
    def name(self):
        return self.__name

    def __del__(self):
        Hund.zaehler -= 1

    def gib_laut(self):
        print(f'{self.name} bellt')

        if self.__gassi_gegangen:
            print("Wedelt mit Schwanz weil sich Hund freut")

    def __repr__(self):
        return f'Hund(name={self.name},age={self.age})'

    def __str__(self):
        return f'{self.name} ist ein Hund und ist {self.age} Jahre alt'

class Corgi(Hund):
    # es wird standardmäßig nur ein init aufgerufen
    # wenn wir hier keines hätte dann das von den eltern

    def __init__(self, name, age, iq):
        # wir müssen explizit init unserer eltern aufrufen
        super().__init__(name, age)
        # Hund.__init__(self, name, age) # das wäre alternativ möglich
        self.iq = iq

    def gib_laut(self):
        print(f'{self.name} bellt ganz intelligent')
        # wenn ich die implementation der basisklasse brauchen würde
        # dann könnte ich super verwenden
        #super().gib_laut()


class Mensch:
    def gib_laut(self):
        print("Mensch macht wuff wuff")

if __name__ == '__main__':
    #ächeddar = Corgi("cheddar", 14)
    cheddar = Corgi("Cheddar", 14, 100)
    #m = Mensch()
    print(cheddar.name)
    cheddar.gib_laut()

    if type(cheddar) == Corgi:
        print("ja ist er")

    if type(cheddar) == Hund:
        print("wird niemand am bildschirm sehen")

    if isinstance(cheddar, Hund):
        print("weil in einem corgi ein hund ist (weil elternklasse)")
    #l = [cheddar, m]
    # duck typing
    #for laut_geber in l:
    #    laut_geber.gib_laut()


