from dataclasses import dataclass

@dataclass
class WeeklySmartphoneSales:
    smartphone: str
    week: int
    numbers_sold: int = 0


def plus_one(x):
    return x + 1

def fakultaet(n):
    if n == 1:
        print("yayy bei 1 ein Ende ist in Sicht")
        return 1
    else:
        print(f"rufe gleich {n-1} fakultaet auf")
        return n * fakultaet(n - 1)

if __name__ == '__main__':
    iphone_w40 = WeeklySmartphoneSales("iPhone 11", 40)

    iphone_w40.numbers_sold = 100000
    print(iphone_w40)


    print(fakultaet(5))



    #list comprehension
    l2 = [i ** 2 for i in range(10)]
    print(l2)

    # list comprehension mit bedingung
    # möcht nur für geradezahlige i einen Eintrag
    l3 = [i ** 2 for i in range(10) if (i % 2) == 0]
    print(l3)

    # liste mit listen generien -> quasi so wie wenn wir
    # zwei verschatelte for schleifen hätten
    ll = [[i*j for j in range(10)] for i in range(10)]
    print(ll)

    print(plus_one(2))
    # mir muss bewusst sein, dass eine hier definierte funktion
    # auch nur hier verwendbar ist
    plus_one_second_edition = lambda x: x + 1
    print(plus_one_second_edition(4))

    # anonyme funktionen definierne (die funktion hat keinen namen)
    print((lambda x, y: x + y)(2, 4))
