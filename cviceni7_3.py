class Chybna_suma(Exception):
    pass


class Bankovni_ucet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0


    def __str__(self):
        return f'Ucet {self.jmeno} ma zustatek: {self.__zustatek} kc'


    def vloz(self, suma):
        if suma <= 0:
            raise Chybna_suma("nulova nebo zaporna castka")
        self.__zustatek += suma

    def vyber(self, suma):
        if suma <= 0:
            raise Chybna_suma("nulova nebo zaporna castka")
        if suma > suma.__zustatek:
            raise Chybna_suma("Nedostatecny zustatek")
        self.__zustatek -= suma




if __name__ == "__main__":

    try:
        ucet = Bankovni_ucet("Alice")
        print(ucet)
        ucet.vloz(100)
        print(ucet)
        ucet.vyber(100)
        print(ucet)
    except Chybna_suma as e:
        print(e)