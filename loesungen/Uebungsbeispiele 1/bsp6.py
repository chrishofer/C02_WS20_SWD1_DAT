# laut http://www.geldmarie.at/steuern/lohnsteuer.html

def berechne_lohnsteuer(einkommen : float) -> float:
    tarife = [[1000000, 0.55],[90000, 0.5],[60000, 0.48],[31000, 0.42],[18000, 0.35],[11000, 0.2]]

    steuer = 0
    rest_einkommen = einkommen
    for tar in tarife:
        if rest_einkommen > tar[0]:
            steuer += (rest_einkommen - tar[0]) * tar[1]
            rest_einkommen = tar[0]

    return steuer


def berechne_lohnsteuer_ohne_schleife(einkommen : float) -> float:



    steuer = 0
    rest_einkommen = einkommen
    if rest_einkommen > 1000000:
        steuer += (rest_einkommen - 1000000) * 0.55
        rest_einkommen = 1000000
    if rest_einkommen > 90000:
        steuer += (rest_einkommen - 90000) * 0.5
        rest_einkommen = 90000
    if rest_einkommen > 60000:
        steuer += (rest_einkommen - 60000) * 0.48
        rest_einkommen = 60000
    if rest_einkommen > 31000:
        steuer += (rest_einkommen - 31000) * 0.42
        rest_einkommen = 31000
    if rest_einkommen > 18000:
        steuer += (rest_einkommen - 18000) * 0.35
        rest_einkommen = 18000
    if rest_einkommen > 11000:
        steuer += (rest_einkommen - 11000) * 0.2

    return steuer


if __name__ == '__main__':
    print(berechne_lohnsteuer(11000))
    print(berechne_lohnsteuer(11001))
    print(berechne_lohnsteuer(18000))
    print(berechne_lohnsteuer(18001))
    print(berechne_lohnsteuer(31001))
    print(berechne_lohnsteuer_ohne_schleife(31001))
    pass