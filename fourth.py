def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    start = figurka["pozice"]
    radek, sloupec = start
    cil_r, cil_s = cilova_pozice

    # Ověření, že pozice je na šachovnici
    if not (1 <= cil_r <= 8 and 1 <= cil_s <= 8):
        return False

    #  Ověření, že cílové pole není obsazené
    if cilova_pozice in obsazene_pozice:
        return False

    # Logika pro jednotlivé figury
    def cesta_volna(cesta):
        return all(p not in obsazene_pozice for p in cesta)

    # Pohyb pěšce
    if typ == "pěšec":
        if sloupec == cil_s:
            if cil_r - radek == 1 and (cil_r, cil_s) not in obsazene_pozice:
                return True
            if radek == 2 and cil_r - radek == 2:
                mezi = (radek + 1, sloupec)
                if mezi not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
                    return True
        return False

    # Pohyb jezdce
    if typ == "jezdec":
        dr = abs(cil_r - radek)
        ds = abs(cil_s - sloupec)
        return (dr, ds) in [(1, 2), (2, 1)]

    # Pohyb věže
    if typ == "věž":
        if radek == cil_r:
            směr = 1 if cil_s > sloupec else -1
            cesta = [(radek, s) for s in range(sloupec + směr, cil_s, směr)]
            return cesta_volna(cesta)
        elif sloupec == cil_s:
            směr = 1 if cil_r > radek else -1
            cesta = [(r, sloupec) for r in range(radek + směr, cil_r, směr)]
            return cesta_volna(cesta)
        return False

    # Pohyb střelce
    if typ == "střelec":
        dr = cil_r - radek
        ds = cil_s - sloupec
        if abs(dr) != abs(ds):
            return False
        směr_r = 1 if dr > 0 else -1
        směr_s = 1 if ds > 0 else -1
        cesta = [(radek + i * směr_r, sloupec + i * směr_s) for i in range(1, abs(dr))]
        return cesta_volna(cesta)

    # Pohyb dámy
    if typ == "dáma":
        # kombinace věže a střelce
        dr = cil_r - radek
        ds = cil_s - sloupec
        if radek == cil_r or sloupec == cil_s:
            # pohyb věže 
            return je_tah_mozny({"typ": "věž", "pozice": start}, cilova_pozice, obsazene_pozice)
        elif abs(dr) == abs(ds):
            # pohyb střelce
            return je_tah_mozny({"typ": "střelec", "pozice": start}, cilova_pozice, obsazene_pozice)
        else:
            return False

    # Pohyb krále
    if typ == "král":
        return abs(cil_r - radek) <= 1 and abs(cil_s - sloupec) <= 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False -> True protože je pěšák na jeho startovací pozici na druhé řadě
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False
    print( )
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False
    print( )
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
