class Motor:
    def __init__(self):
        # das ist für andere teile des autos interessant
        # diese möchten darauf zugreifen können
        # deswegen machen wir es public
        # (es war einmal public - jetzt private mit getter)
        self.__umdrehungen_pro_minute = 0
        # es geht um daten die zuvor public waren
        # jetzt möchte ich zugriff darauf nur über meine methoden erlauben
        # -> property mit einer private oder protected variable dahinter (üblich private)
        self.geschwindigkeit = 20


        # es sollte keinen anderen teil des autos interessierne
        # wie viel benzin/diesel eingespritzt wird
        # -> private
        self.__einspritz_menge = 0

        # protected: immer dann wenn nur wir als klasse und unsere subklassen
        # darauf zugreifen sollen
        self._motor_modus = "sport"

    @property
    def geschwindigkeit(self):
        # theoretisch müsste ich hier noch datan transofmrieren
        # zb geburtsdatum in ein alter umwandeln falls das zweitere gefragt wäre
        print("getter Zugriff")
        return self.__geschwindigkeit

    @geschwindigkeit.setter
    def geschwindigkeit(self, value):
        print("setter Zugriff")
        if value >= 0 and value <= 250:
            self.__geschwindigkeit = value

    @property
    def umdrehungen_pro_minute(self):
        return self.__umdrehungen_pro_minute

    def __interne_fkt(self):
        print("hallo")

if __name__ == '__main__':
    m = Motor()

    print(m.umdrehungen_pro_minute)
    #m.umdrehungen_pro_minute = 1000
    print(m.umdrehungen_pro_minute)
    # python bennenten den namen um
    # achtung: sollte man nicht machen
    print(m._Motor__einspritz_menge)
    # protected keine umbenennung - trotzdem nicht machen
    print(m._motor_modus)

    print(m.geschwindigkeit)


    m._Motor__interne_fkt()