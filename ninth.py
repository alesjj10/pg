def dev_to_bin(cislo):
    cislo = int(cislo)

    # ošetření pr 0
    if cislo == 0:
        return "0"

    vysledek = ""
    while cislo > 0:
        vysledek = str(cislo % 2) + vysledek
        cislo //= 2

    return vysledek


def test_bin_to_dec():
    assert dev_to_bin("0") == "0"
    assert dev_to_bin(1) == "1"
    assert dev_to_bin("100") == "1100100"
    assert dev_to_bin(101) == "1100101"
    assert dev_to_bin(127) == "1111111"
    assert dev_to_bin("128") == "10000000"
