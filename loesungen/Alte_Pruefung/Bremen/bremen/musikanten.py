import abc, math
from typing import List, Dict

class Instrument:
    def __init__(self, name: str, lautstaerke: float):
        self.name = name
        self.lautstaerke = lautstaerke


class Musikant(abc.ABC):
    @property
    def anzahl_beine(self):
        return self.__anzahl_beine

    @property
    def instrument(self):
        return self.__instrument

    def __init__(self, anzahl_beine: int, instrument: Instrument):
        self.__anzahl_beine = anzahl_beine
        self.__instrument = instrument

    @abc.abstractmethod
    def verscheuche_raeuber(self) -> int:
        pass

    @abc.abstractmethod
    def spiele_musik(self) -> float:
        pass

    def __repr__(self):
        return f'Verscheucht:{self.verscheuche_raeuber()}, Musiziert:{self.spiele_musik()}'


class Esel(Musikant):
    @property
    def tritt_kraft(self):
        return self.__tritt_kraft

    def __init__(self, anzahl_beine: int, instrument: Instrument, tritt_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__tritt_kraft = tritt_kraft

    def __repr__(self):
        return f'Esel {self.tritt_kraft}:' + super().__repr__()

    def verscheuche_raeuber(self) -> int:
        return math.floor(self.tritt_kraft * self.anzahl_beine)

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke


class Hund(Musikant):
    @property
    def bell_lautstaerke(self):
        return self.__bell_lautstaerke

    def __init__(self, anzahl_beine: int, instrument: Instrument, bell_lautstaerke: float):
        super().__init__(anzahl_beine, instrument)
        self.__bell_lautstaerke = bell_lautstaerke

    def __repr__(self):
        return f'Hund {self.bell_lautstaerke}:' + super().__repr__()

    def verscheuche_raeuber(self) -> int:
        if self.bell_lautstaerke > self.instrument.lautstaerke:
            return math.floor(self.bell_lautstaerke)
        else:
            return math.floor(self.instrument.lautstaerke)

    def spiele_musik(self) -> float:
        return (self.instrument.lautstaerke + self.bell_lautstaerke) / 2


class Katze(Musikant):
    @property
    def kratz_kraft(self):
        return self.__kratz_kraft

    def __init__(self, anzahl_beine: int, instrument: Instrument, kratz_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__kratz_kraft = kratz_kraft

    def __repr__(self):
        return f'Katze {self.kratz_kraft}:' + super().__repr__()

    def verscheuche_raeuber(self) -> int:
        verscheucht = self.kratz_kraft
        if self.anzahl_beine == 3:
            verscheucht /= 2
        elif self.anzahl_beine <= 2:
            verscheucht = 1

        return math.floor(verscheucht)

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke


class Hahn(Musikant):
    @property
    def flug_weite(self):
        return self.__flug_weite

    def __init__(self, anzahl_beine: int, instrument: Instrument, flug_weite: int):
        super().__init__(anzahl_beine, instrument)
        self.__flug_weite = flug_weite

    def __repr__(self):
        return f'Hahn {self.flug_weite}:' + super().__repr__()

    def verscheuche_raeuber(self) -> int:
        if self.flug_weite < 2:
            return math.floor(self.instrument.lautstaerke)
        elif self.flug_weite == 2:
            return 6
        elif self.flug_weite == 3:
            return 5
        elif self.flug_weite == 4:
            return 4
        elif self.flug_weite == 5:
            return 3
        elif self.flug_weite == 6:
            return 2
        return 1

    def spiele_musik(self) -> float:
        return (self.instrument.lautstaerke + 2) / self.flug_weite

class Quartett:
    def __init__(self):
        self.__musikanten = []

    def add(self, m: Musikant):
        self.__musikanten.append(m)

    def ist_quartett(self) -> bool:
        if len(self.__musikanten) == 4:
            return True
        return False

    def gemeinsam_raeuber_verscheucht(self) -> int:
        vers = 0

        for m in self.__musikanten:
            vers += m.verscheuche_raeuber()

        return vers

    def durchschnittliche_lautstaerke(self) -> float:
        laut = 0
        for m in self.__musikanten:
            laut += m.spiele_musik()

        laut = laut / len(self.__musikanten)
        return laut

    def get_musikanten_in_lautstaerke_bereich(self, von: float, bis: float) -> List:

        l = []
        for m in self.__musikanten:
            laut = m.spiele_musik()
            if laut >= von and laut <= bis:
                l.append(m)

        return l


    def get_anzahl_musikante_mit_bein_anzahl(self) -> Dict[int, int]:
        sol = {}

        for m in self.__musikanten:

            anz = sol.get(m.anzahl_beine, 0) + 1
            sol[m.anzahl_beine] = anz

        return sol

if __name__ == '__main__':
    # too lazy for more :)
    e = Esel(4, Instrument("Trompete", 15), 10)
    h = Hund(4, Instrument("Trompete", 15), 10)
    k = Katze(4, Instrument("Trompete", 15), 10)
    ha = Hahn(2, Instrument("Trompete", 15), 10)

    q = Quartett()
    q.add(e)
    q.add(h)
    q.add(k)
    q.add(ha)

    print(q.ist_quartett())
    print(q.gemeinsam_raeuber_verscheucht())
    print(q.durchschnittliche_lautstaerke())
    print(q.get_musikanten_in_lautstaerke_bereich(10, 14))
    print(q.get_anzahl_musikante_mit_bein_anzahl())

