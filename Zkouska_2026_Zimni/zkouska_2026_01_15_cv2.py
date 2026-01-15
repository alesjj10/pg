import sys

def spocitej_statistiku(text):
    
#   nejlehci zpusob !!pro kratší text!! (projede text min 5krat)
#    pocet_radku = len(text.splitlines())
#    pocet_slov = len(text.split())
#    pocet_znaku = len(text)

    pocet_radku = 0         # inicializace promennych
    pocet_slov = 0
    pocet_znaku = 0

    radky = text.splitlines()   # rozdeli text na radky
    pocet_radku = len(radky)    # spocita pocet radku

    for s in radky:             # projede kazdy radek a spocita slova
        slova = s.split()       # rozdeli radek na slova (split ignoruji mezery navic)
        pocet_slov += len(slova)    # pricte pocet slov v radku do celkoveho poctu slov

    pocet_znaku = len(text)     # spocita pocet znaku v textu (vcetne mezer a znaku novy radek \n)


    return pocet_radku, pocet_slov, pocet_znaku     # vcrati n-tici (tuple) s vysledky


def test_spocitej_statistiku():                                                 # testovaci funkce
    assert spocitej_statistiku("Ahoj svet\nToto je test.") == (2, 5, 23)        # testuje radky, slova, znaky
    assert spocitej_statistiku("") == (0, 0, 0)                                 # prazdny text    
    assert spocitej_statistiku("Jediny radek bez novych radku") == (1, 5, 29)   # testuje jeden radek
    assert spocitej_statistiku("Prvni radek\nDruhy radek\nTreti radek") == (3, 6, 35)  


if __name__ == "__main__":          # Hlavni část programu
    try:            # Ošetření chyb při práci se soubory (skočí to except při chybě)

        vstupni_soubor = 'data.txt'
        vystupni_soubor = 'statistika.txt'

        # načtěte data ze vstupního souboru (jméno souboru je v proměnné `vstupni_soubor`)    
        
        with open(vstupni_soubor, 'r', encoding='utf-8') as f:  # otevře soubor pro čtení, with zajistí zavření souboru
            obsah = f.read()                # načte celý obsah souboru do proměnné obsah    

    
        pocet_radku, pocet_slov, pocet_znaku = spocitej_statistiku(obsah) # zavolá funkci

        # uložte výsledky do výstupního souboru (jméno souboru je v proměnné `vystupni_soubor`)
        # formát:
        # Pocet radku: X
        # Pocet slov: Y
        # Pocet znaku: Z

        with open(vystupni_soubor, 'w', encoding='utf-8') as f:     # otevře/vytvori soubor pro zápis
            f.write(f"Pocet radku: {pocet_radku}\n")               # zapíše výsledky do souboru
            f.write(f"Pocet slov: {pocet_slov}\n")                 
            f.write(f"Pocet znaku: {pocet_znaku}\n")



        # volitelne info pro uzivatele
        print(f"Pocet radku: {pocet_radku}")                        # info navíc
        print(f"Pocet slov: {pocet_slov}")  
        print(f"Pocet znaku: {pocet_znaku}")
        
        print("Statistika byla ulozena do souboru", vystupni_soubor)

    except FileNotFoundError:                       # osetreni chyby pokud soubor data.txt neexistuje
        print("Vstupni soubor neexistuje")
    except Exception:                                # osetreni ostatnich chyb  
        print("Doslo k chybe pri praci se souborem")