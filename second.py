def cislo_text(cislo):   
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    nact = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    
    cislo = int(cislo)

    # pro cisla od 0 do 9 
    if cislo < 10:
        return jednotky[cislo]
    
    elif cislo < 20:
        return nact[cislo]
    



if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)



    

    