def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    teens = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    cislo = int(cislo)


    # 0–9
    if cislo < 10:
        return jednotky[cislo]
    # 10–19
    elif cislo < 20:
        return teens[cislo - 10]
    # 20–99
    elif cislo < 100:
        d = cislo // 10
        j = cislo % 10
        if j == 0:
            return desitky[d]
        else:
            return desitky[d] + " " + jednotky[j]
    # 100
    elif cislo == 100:
        return "sto"
    else:
        return "mimo rozsah"

# Příklady
print(cislo_text(0))    # nula
print(cislo_text(15))   # patnáct
print(cislo_text(25))   # dvacet pět
print(cislo_text(100))  # sto
