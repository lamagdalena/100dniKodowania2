def silnia():
    liczba = int(input("Wprowadz liczbe: "))
    wynik = 1
    for x in range(0, liczba+1):
        if x == 0:
            wynik = 1
        else:
            wynik *= x

    return wynik

print(silnia())