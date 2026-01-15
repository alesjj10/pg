# funkce zkontroluje, zda je cislo sude nebo liche
# vypise:
# - "Cislo x je sude"
# - "Cislo x je liche"
def sudy_nebo_lichy(cislo):
    if cislo % 2 != 0:
        print(f"Cislo {cislo} je liche")
    else:
        print(f"Cislo {cislo} je sude")


if __name__ == "__main__":

    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)