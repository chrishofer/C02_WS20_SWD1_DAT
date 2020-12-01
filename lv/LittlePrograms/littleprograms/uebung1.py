
class Hund: # Name in großge. CamelCase

    species = 'Canis lupus familiaris' # Klassenattri.

    def __init__(self, name, age): # Zum Initialisieren
        self.name = name # Instanzattribut
        self.age = age


if __name__ == '__main__':

    rex = Hund("Kommissar Rex", 14)
    lassie = Hund("Lassie", 10)

    print(rex.age) # Zugriff auf eine Objekt bzw. Instanzvariable
    print(lassie.age)
    print(lassie.species) # geht theoretisch auch (aber bitte nicht schreibend darauf zugreifen)
    # lassie.species = "Abenteuerhündin" # bitte nicht machen - weil jetzt haben wir ein neues instanzattribut erzeugt
    # idealerweise immer über klassenvar zugreifen
    print(Hund.species) # Zugriff auf eine Klassenvar (gibt es nur einmal)
    print(lassie.species)
    print(dir(lassie)) # Variante um schön anzusehen
    print(lassie.__dict__) # immer wenn ich mit . zugreife schaut python im __dict__ ob es das kennt - falls nicht wird im __dict__ der Klasse nach
