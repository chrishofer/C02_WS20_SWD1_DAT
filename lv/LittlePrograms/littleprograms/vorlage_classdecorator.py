class Test_meta(type):
    def __init__(cls, *args, **kwargs):
        print("einmal init")
        cls.zaehler = 0
    @property
    def zaehler(cls):
        print("getter")
        return cls.__zaehler

    @zaehler.setter
    def zaehler(cls, value):
        print("setter")
        cls.__zaehler = value


class Test(metaclass=Test_meta):
    zaehler2 = 77
    def __init__(self):
        Test.zaehler += 1

class TestRead_meta(type):
    def __init__(cls, *args, **kwargs):
        print("Read einmal init")
        cls.__zaehler = 0
    @property
    def zaehler(cls):
        print("Read getter")
        return cls.__zaehler


class TestRead(metaclass=TestRead_meta):
    zaehler3 = 99
    def __init__(self):
        TestRead._TestRead_meta__zaehler += 1


if __name__ == '__main__':

    print(Test.zaehler)
    t = Test()
    print(Test.zaehler)

    Test.zaehler = 2
    # print(t.zaehler) # Kein Zugriff über ein Klassenobjekt während klassische Klassenvar schon geht
    print(t.zaehler2)

    print("---------------")
    print(TestRead.zaehler)
    tr = TestRead()

    # TestRead.zaehler = 12 # kann nicht setzen
    #print(tr.zaehler) # Kein Zugriff
    print(tr.zaehler3)
    print(TestRead.zaehler)