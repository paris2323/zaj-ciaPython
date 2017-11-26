imie = "ola"
                                     # imie a imie nierówne
def wypisz_imie(imie):
    duze_imie = imie.upper()
    return duże_imie

print(imie)


imie = "ola" #globalna

def wypisz_imie(imie="Ala"): #lokalna
    duze_imie = imie.upper()
    return duże_imie

print(wypisz_imie())


imie = "ola"

def wypisz_imie():
    global imie
    duze_imie = imie.upper()
    return duże_imie

print(wypisz_imie())
