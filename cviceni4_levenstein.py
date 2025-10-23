
def levensteinova_vzdalenost_while(dotaz1, dotaz2):
    delka = max(len(dotaz1), len(dotaz2))  
    i = 0
    levenstein = 0
    while i < delka:
        if i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                levenstein += 1
        else:
            levenstein += 1
        i += 1
    return levenstein


def levensteinova_vzdalenost_for(dotaz1, dotaz2):
    delka = min(len(dotaz1), len(dotaz2)) 
    levenstein = 0
    for i in range(delka):
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein

if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print("for cyklus")
    print(levensteinova_vzdalenost_for(query1, query2))
    print(levensteinova_vzdalenost_for(query2, query3))
    print(levensteinova_vzdalenost_for(query1, query3))
    print(levensteinova_vzdalenost_for(query1, query4))
    print("while cyklus")
    print(levensteinova_vzdalenost_while(query1, query2))
    print(levensteinova_vzdalenost_while(query2, query3))
    print(levensteinova_vzdalenost_while(query1, query3))
    print(levensteinova_vzdalenost_while(query1, query4))