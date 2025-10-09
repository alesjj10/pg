def vrat_treti(seznam):
    if len(seznam) >= 3:
        return seznam[2]
    else:
        return None

def prumer(cisla):
    return sum(cisla) / len(cisla)



def naformatuj_text(student):
    return f"Jméno: {student['jmeno']} {student['prijmeni']}, Věk: {student['vek']}, Průměrná známka: {round(prumer(student['znamky']), 2)}"




if __name__ == "__main__":
    # vytvoreni noveho seznamu
    seznam = [12, 50, 1, 3, 5]
    # 3. prvek vinasobime 3
    seznam[3] *= 3
    # nakonec seynam pridame hodnotu 100
    seznam.append(100)
    # seznam srovnáme sestupně
    seznam.sort()
    seznam.reverse()

    #seznam2 = [1,2,3]
    #print(prumer(seznam2))
   
    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,1,3,1,2,1]
    }
    student["vek"] += 1
    print(naformatuj_text(student))
