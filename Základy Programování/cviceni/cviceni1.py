
def cislo_mensi_nez_3(tri):
    if tri > 3:
        print(f"hodnota {tri} je vesti nez 3")
    elif tri < 3:
        print(f"hodnota {tri} je mensi nez 3")
    else: 
        print(f"hodnota {tri} je rovna 3")

if __name__ == "__main__":

    cislo = input("Zadej cislo: ")
    cislo = int(cislo)
    print(f"Zadane cislo je: {cislo}")

    cislo_mensi_nez_3(1)
    cislo_mensi_nez_3(cislo)

