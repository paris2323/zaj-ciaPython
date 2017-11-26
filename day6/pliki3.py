sciezka = "tekst1"

with open(sciezka)as plik:
    linijki = plik.readlines()

    print(linijki)

for linijka in linijki:
    print(linijka)