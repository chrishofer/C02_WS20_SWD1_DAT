class Verwaltungsstrafe:
    __strafen_zaehler = 1

    def __init__(self, vorname, nachname, kennzeichen):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__kennzeichen = kennzeichen
        self.__strafnummer = Verwaltungsstrafe.__strafen_zaehler
        Verwaltungsstrafe.__strafen_zaehler += 1

        self.__strafe = 0.0
        self.__anzahl = 0

    @property
    def vorname(self):
        return self.__vorname

    @property
    def nachname(self):
        return self.__nachname

    @property
    def kennzeichen(self):
        return self.__kennzeichen

    @property
    def strafnummer(self):
        return self.__strafnummer

    @property
    def strafe(self):
        # hier fehlt noch code
        return self.__strafe

    @property
    def anzahl(self):
        return self.__anzahl

if __name__ == '__main__':
    a = Verwaltungsstrafe("hansi", "hinterseer", "was299")
    b = Verwaltungsstrafe("susi", "musterstudi", "was259")
    print(a.strafnummer)
    print(b.strafnummer)