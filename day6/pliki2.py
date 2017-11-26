sciezka = "tekst1"


with open(sciezka)as plik:
    print(plik.readline())
    print("kolejna linijka")
    print(plik.readline())

with open(sciezka)as plik:
    print(plik.readline())
    print("kolejna linijka")
    print(plik.read())

with open(sciezka)as plik:
    linijka = plik.readline()
    pozycja = plik.tell()

    plik.seek(3)
    print(plik.read())