def my_decorator(func):          # Dekorator
    def text_around(para):
        print(f'Davor {func.__name__}')
        func(para) # Funktion wird aufgerufen
        print(f'Danach {func.__name__}')
    return text_around

# das ist die kurzversion der zuweisung hallo = my_decorator(hallo)
@my_decorator
def hallo(txt):			# zu dekorierendes Objekt
    print(f'Hallo {txt}')

if __name__ == '__main__':
    hallo("DAT")
    y = hallo
    y("DAT erneut")

    # wenn ich absofort hallo aufrufe, dass noch etwas anderes gemacht wird
    # und zwar das was in meinem decorator passiert
    #x = my_decorator(hallo)
    #x("DAT 2")
    #hallo = my_decorator(hallo)
    #hallo("DAT")