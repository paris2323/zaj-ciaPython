sciezka = "tekst1"


tekst = """To jest mój tekst, 
jest kolejna i kolejna"""

with open(sciezka, "w") as plik:
    print(plik.tell())
    print.write(tekst)
