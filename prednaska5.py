class ChybaDeleniNulou(Exception):
    pass

def vydel(citatel, jmenovatel):
    if jmenovatel == 0:
        raise ChybaDeleniNulou("Nulou nelze dělit")
    return citatel / jmenovatel
    

if __name__ == "__main__":

    try:

        cislo1 = None
        while cislo1 is None:
            try:
                cislo1 = int(input("zadej citatel: "))
            except Exception:
                print('zadej validni cislo')


        cislo2 = int(input("zadej jmenovatel: "))

        vysledek = vydel(cislo1, cislo2)

        print(vysledek)

    except ChybaDeleniNulou as e:

        print('pokusili jste se dělit nulou')

    except Exception as e:

        print('V tomto programu nastala chyba: {e}')