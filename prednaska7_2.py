class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    
    def prirad_ucet(self, ucet):
        self.ucet = ucet


class Ucet:
    def __init__(self, majitel):
        self.majitel = majitel
        self.__zustatek = 0

    def zustatek(self):
        return self.__zustatek

    def vloz(self, castka):
        if castka <= 0:
            raise Exception("Zaporna castka")
        self.__zustatek += castka

    def vyber(self, castka):
        if castka <= 0:
            raise Exception("Zaporna castka")


    def __str__(self):
        return f'Ucet({self.majitel.jmeno}): {self.zustatek()}'

class Banka:
    def __init__(self, nazev):
        self.nazev = nazev
        self.ucty = []

    def zaloz_ucet(self, osoba):
        novy_ucet = Ucet(osoba)
        osoba.prirad_ucet(novy_ucet)
        self.ucty.append(novy_ucet)

   
if __name__ == "__main__":
    osoba1 = Osoba("Alice")
    osoba2 = Osoba("Bob")

    print(osoba1.jmeno, osoba1.ucet)

    banka1 = Banka("KB")

    banka1.zaloz_ucet(osoba1)
    banka1.zaloz_ucet(osoba2)

    print(osoba1.jmeno, osoba1.ucet)
    print(banka1.nazev, banka1.ucty)