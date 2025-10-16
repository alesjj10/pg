def my_range(start, stop, step=1):
    result = []
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    return result


def for_enumerate(iterable, start=0):
    vysledek = []
    for jmeno in iterable:
        vysledek.append((start, jmeno))
        start += 1
    return vysledek


def while_enumerate(iterable, start=0):
    vysledek = []
    index = 0
    while index < len(iterable):
        vysledek.append((index + start, iterable[index]))
        index += 1
    return vysledek

if __name__ == "__main__":


    """
    standalone kód

    text = "acdef"
    seznam = ["a", "b", "c", "d", "e", "f"]


    index = 0
    for znak in text:
        if index % 2 == 0:
            print(znak)
        index += 1


    index = 0
    while index < len(text):
        print(text[index])
        index += 1
    """   

    """
    k def my_range
    
    print(list(range(1, 10, 3)))
    
    print(my_range(1, 10, 3))
    """
    
    """
    #k def for_enumerate
    
    print(list(enumerate(['Alice', 'Bob', 'Eva'], 1)))
    print(for_enumerate(['Alice', 'Bob', 'Eva'], 1))
    print(while_enumerate(['Alice', 'Bob', 'Eva'], 1))
    """

