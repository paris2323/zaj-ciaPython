sciezka = "tekst2"

with open(sciezka,"w+") as plik:
    linijka = plik.read()
    print(linijka)
    print(plik.tell())
    ntekst = plik.write("dopisz to tutaj\n")
    plik.seek(12)
    ntekst = plik.write("WWWA\n")
