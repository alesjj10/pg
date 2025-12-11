def vrat_3_hodnoty():
    return 3, 6, 9

if __name__ == "__main__":

    student = {
        "name": "Alice",
        "age": 25
    }




    if "age" in student:
        print(student["age"])
    else:
        print("none")



    """
    prvni, druhy, treti = vrat_3_hodnoty()
    print(prvni)
    print(druhy)
    print(treti)


    fronta = [] # FIFO
    fronta.append(10)
    fronta.append(5)
    fronta.append(1)
    fronta.append(20)

    print(fronta.pop(0))

    fronta.append(3)

    print(fronta.pop(0))
    print(fronta.pop(0))    
    print(fronta.pop(0))
    print(fronta.pop(0))

    print('---')

"""