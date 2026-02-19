import math

def statistika(rezim, cisla):
    """
    rezim: "soucet" | "pocet" | "max" | "min" | "prumer"    toto je řetězec
    cisla: list[int] nebo list[float]                       toto je seznam čísel

    Vrat:
      - "soucet": soucet vsech cisel v seznamu
      - "pocet": pocet prvku v seznamu
      - "max": nejvetsi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "min": nejmensi hodnota v seznamu (pokud je seznam prazdny, vrat None)
      - "prumer": aritmeticky prumer (pokud je seznam prazdny, vrat None)

    Nepouzivej vestavene funkce sum(), max(), min().
    Pouzij cyklus a podminky.
    """
    if rezim == "soucet":         # funkce soucet
        celkem = 0                # vytvoreni promenne celkem
        for cislo in cisla:     
            celkem += cislo       # projede seznam a pricte vsechny cisla do celkem
        return celkem             # vrati hodnotu celkem
    
    elif rezim == "pocet":        # funkce pocet
        pocet = 0                 # vytvoreni promenne pocet
        for i in cisla:         
            pocet += 1            # projede seznam a za kazde cislo zvysi pocet o 1 (mozna lze pouzit len)
        return pocet              # vrati hodnotu pocet

    elif rezim == "max":          # funkce max
        if not cisla:               # pokud je seznam prazdny, vrat None (zabrani chybe)
            return None
        nejvyssi = cisla[0]         # nastavime prvni cislo v seznamu jako nejvyssi
        for cislo in cisla:         # projede seznam a porovna kazde cislo s nejvyssim
            if cislo > nejvyssi:
                nejvyssi = cislo    # if cislo vetsi nez nejvyssi, nastav nejvyssi na cislo
        return nejvyssi             # vrati hodnotu nejvyssi
    
    elif rezim == "min":            # funkce min
        if not cisla:               # pokud je seznam prazdny, vrat None (zabrani chybe)
            return None             
        nejmensi = cisla[0]         # nastavime prvni cislo v seznamu jako nejmensi
        for cislo in cisla:         # projede seznam a porovna kazde cislo s nejmensim
            if cislo < nejmensi:
                nejmensi = cislo    # if cislo mensi nez nejmensi, nastav nejmensi na cislo
        return nejmensi             # vrati hodnotu nejmensi
    
    elif rezim == "prumer":         # funkce prumer
        if not cisla:               # pokud je seznam prazdny, crat None (zabrana chyby)
            return None
        celkem = 0                  # vytvoreni promenne celkem a pocet
        pocet = 0
        for cislo in cisla:         # stejne jako soucet a pocet
            celkem += cislo
            pocet += 1 
        mezi = celkem / pocet       # vypocita prumer
        return mezi                 # vrati hodnotu prumer
        
    else:               # pokud neni zadany spravny rezim, vrat None (osetreni chyb)
        return None


def test_statistika():
    assert statistika("soucet", [1, 2, 3, 4]) == 10
    assert statistika("soucet", [-1, -2, -3]) == -6
    assert statistika("soucet", []) == 0
    assert statistika("pocet", [1, 2, 3]) == 3
    assert statistika("pocet", []) == 0
    assert statistika("max", [1, 9, 3]) == 9
    assert statistika("max", [-10, -2, -30]) == -2
    assert statistika("max", []) is None
    assert statistika("min", [1, 9, 3]) == 1
    assert statistika("min", [-10, -2, -30]) == -30
    assert statistika("min", []) is None
    assert math.isclose(statistika("prumer", [2, 4, 6]), 4.0)
    assert math.isclose(statistika("prumer", [1, 2]), 1.5)
    assert statistika("prumer", []) is None
    assert statistika("neco", [1, 2, 3]) is None


if __name__ == "__main__":                       # Tento kód se spustí jen pokud se soubor spouští přímo
    print(statistika("soucet", [1, 2, 3]))     # 6
    print(statistika("pocet", [1, 2, 3]))     # 3
    print(statistika("max", [1, 9, 3]))       # 9
    print(statistika("min", [1, 9, 3]))       # 1
    print(statistika("prumer", [2, 4, 6]))    # 4.0