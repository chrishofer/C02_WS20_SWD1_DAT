import abc

# es gibt auch abstractstaticmethod und abstractclassmethod
class Flaeche(abc.ABC):
    @abc.abstractmethod
    def flaeche(self):
        pass

    def print_hello(self):
        print("hello")

class Quadrat(Flaeche):
    def __init__(self, a):
        self.a = a
    def flaeche(self):
        return self.a ** 2


if __name__ == '__main__':

    #f = Flaeche()
    f = Quadrat(4)
    print(f.flaeche())
    f.print_hello()



