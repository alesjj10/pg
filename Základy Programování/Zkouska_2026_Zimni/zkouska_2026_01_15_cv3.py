from abc import ABC, abstractmethod
# ABC = Abstract Base Class

class Zamestnanec(ABC):                         # abstraktni trida, nelze vytvorit instanci, základ pro dědičnost
    def __init__(self, jmeno, zakladni_mzda):   # konstruktor tridy, parametry jmeno a zakladni_mzda
        self.jmeno = jmeno
        self.zakladni_mzda = zakladni_mzda
        self.pocet_odpracovanych_let = 0    # inicializace pocet_odpracovanych_let na 0
                                            # bude se menit metodou pridej_rok
    def pridej_rok(self):
        self.pocet_odpracovanych_let += 1

    def odeber_rok(self):                       # neni v zadani ale proc ne
        if self.pocet_odpracovanych_let > 0:
            self.pocet_odpracovanych_let -= 1

    @abstractmethod                      # abstraktni metoda, musi byt implementovana v podtridach ktere dedi ze zamestnanec  
    def vypocitej_mzdu(self):
        # Zakladni mzda + 1000 Kc za kazdy odpracovany rok
        bonus = 1000 * self.pocet_odpracovanych_let         # vypocet bonusu za odpracovane roky
        return self.zakladni_mzda + bonus

    def __str__(self):                  # metoda pro stringovou reprezentaci objektu vraci citelny popis zamestnance
        return f"Zamestnanec {self.jmeno}, odpracovanych let {self.pocet_odpracovanych_let}, zakladni mzda {self.zakladni_mzda} Kc"


# Vytvorte tridu Programator, ktera dedi od Zamestnanec
# Programator dostava 10% navíc proti mzdě vypočítané metodou vypocitej_mzdu ve tride Zamestnanec
class Programator(Zamestnanec):                 # dedi od Zamestnanec
    def vypocitej_mzdu(self):               # prepise metodu vypocitej_mzdu povinne!
        zakladni_mzda = super().vypocitej_mzdu()    # vola metodu rodicovske tridy
        return int(zakladni_mzda * 1.1)         # pricte 10% k vypoctene mzde


# Vytvorte tridu Manazer, ktera dedi od Zamestnanec
# konstruktor tridy Manazer prijima navic parametr pocet_podrizenych
# Manazer dostava 1000 Kc navíc za každého podřízeného zaměstnance nad rámec mzdy
# vypočítané metodou vypocitej_mzdu ve tride Zamestnanec
class Manazer(Zamestnanec):                # dedi od Zamestnanec                    
    def __init__(self, jmeno, zakladni_mzda, pocet_podrizenych):    # konstruktor prijima navic pocet_podrizenych
        super().__init__(jmeno, zakladni_mzda)                  # vola konstruktor rodicovske tridy
        self.pocet_podrizenych = pocet_podrizenych        # inicializace pocet_podrizenych

    def vypocitej_mzdu(self):                   
        zakladni_mzda = super().vypocitej_mzdu()        
        bonus_za_podrizene = self.pocet_podrizenych * 1000      # vypocet bonusu za podrizene
        return zakladni_mzda + bonus_za_podrizene               # pricte bonus k vypoctene mzde


if __name__ == "__main__":
    p1 = Programator("Alice", 40000)
    m1 = Manazer("Bob", 50000, 5)

    zamestnanci = [p1, m1]

    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)
    # ocekavany vystup:
    # Zamestnanec Alice, odpracovanych let 0, zakladni mzda 40000 Kc
    # Mzda: 44000 Kc
    # --------------------
    # Zamestnanec Bob, odpracovanych let 0, zakladni mzda 50000 Kc
    # Mzda: 55000 Kc
    
    # Pridame 2 roky praxe
    for zamestnanec in zamestnanci:
        zamestnanec.pridej_rok()
        zamestnanec.pridej_rok()

    print("Po pripocteni odpracovanych let:")
    for zamestnanec in zamestnanci:
        print(zamestnanec)
        print(f'Mzda: {zamestnanec.vypocitej_mzdu()} Kc')
        print('-' * 20)
    # ocekavany vystup:
    # Zamestnanec Alice, odpracovanych let 2, zakladni mzda 40000 Kc
    # Mzda: 46200 Kc
    # --------------------
    # Zamestnanec Bob, odpracovanych let 2, zakladni mzda 50000 Kc
    # Mzda: 57000 Kc