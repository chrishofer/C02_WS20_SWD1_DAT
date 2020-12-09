import abc

# es gibt auch abstractstaticmethod und abstractclassmethod
class Flaeche(abc.ABC):
    @abc.abstractmethod
    def flaeche(self):
        pass

    def print_hello(self):
        print("hello")

class Rechteck(Flaeche):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def flaeche(self):
        return self.a * self.b

class Quadrat(Flaeche):
    def __init__(self, a):
        self.a = a
    def flaeche(self):
        return self.a ** 2


if __name__ == '__main__':

    #f = Flaeche()

    r = Rechteck(4, 10)


    f = Quadrat(4)
    print(f.flaeche())
    f.print_hello()



