class Hund: # Name in großge. CamelCase

    species = 'Canis lupus familiaris' # Klassenattri.
    zaehler = 0 # soll mitzählen wie viele objekte gerade leben

    @classmethod
    def get_anzahl_hunde(cls):
            return cls.zaehler

    def __init__(self, name: str, age: str): # Zum Initialisieren
        self.__name = name # Achtung da nur getter existiert müssen wir direkt auf __ zugreifen
        self.age = age
        self._gefuettert = False        # protect Attribut
        self.__gassi_gegangen = True   # private Attribut
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

if __name__ == '__main__':

    rex = Hund("Kommissar Rex", 14)
    lassie = Hund("Lassie", 10)

    rex.gib_laut()
    # es gibt eigentlich keine zugriffeinschränkungen
    print(rex._gefuettert) # auch nicht machen da protected
    #print(rex.__gassi_gegangen) # geht nicht wegen name mangeling
    print(dir(rex))
    print(rex._Hund__gassi_gegangen) # es funktioniert - aber bitte nicht machen

    print(rex.age)
    # weil es getter kann ich lesen aber nicht zuweisen
    print(rex.name)
    ##rex.name = "Scooby Doo"  # geht nicht

