def cislo_text(cislo):   
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    nact = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    
    cislo = int(cislo)

    
    if cislo < 10:          # pro cisla od 0 do 9 
        return jednotky[cislo]
    
    elif cislo < 20:        # pro cisla od 10 do 19
        return nact[cislo - 10]
    
    elif cislo < 100:       # pro cisla od 20 do 99
        a = cislo // 10     # rozklad na desitkz   
        b = cislo % 10      # rozklad na jednotky
        if b == 0:          # pokud je jednotka 0, vypise se jen desitka
            return desitky[a]
        else:               # jinak se vypisi desitka a jednotka
            return desitky[a] + " " + jednotky[b]
    # pro cislo 100
    elif cislo == 100:
        return "sto"
    else:
        return "mimo rozsah"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)



    

    