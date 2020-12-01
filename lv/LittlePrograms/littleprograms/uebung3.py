class Hund: # Name in großge. CamelCase

    species = 'Canis lupus familiaris' # Klassenattri.
    zaehler = 0 # soll mitzählen wie viele objekte gerade leben

    @classmethod
    def get_anzahl_hunde(cls):
            return cls.zaehler

    def __init__(self, name: str, age: str): # Zum Initialisieren
        self.name = name # Instanzattribut
        self.age = age
        Hund.zaehler += 1

    def __del__(self):
        Hund.zaehler -= 1

    def gib_laut(self):
        print(f'{self.name} bellt')

    def __repr__(self):
        return f'Hund(name={self.name},age={self.age})'

    def __str__(self):
        return f'{self.name} ist ein Hund und ist {self.age} Jahre alt'

if __name__ == '__main__':

    rex = Hund("Kommissar Rex", 14)
    lassie = Hund("Lassie", 10)

    lassie.gib_laut()
    print(lassie.__str__())
    print(lassie.__repr__())
    print(lassie) # print verwendet __str__ Funktion so vorhanden, sonst __repr__
    # lassie.gib_laut() wird intern eigentlich
    Hund.gib_laut(lassie) # kein Mensch schreibt es so

    # for element in [rex, lassie]:
    #     print(element)


    print(Hund.get_anzahl_hunde())

    del lassie # ich brauch es nicht mehr

    print(Hund.get_anzahl_hunde())
