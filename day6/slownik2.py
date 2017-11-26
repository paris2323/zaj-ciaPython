
osoby = {}


rekordy = [{"imie": "Adam","nazwisko":"kowalski","wiek":32},
{"imie": "Anna","nazwisko":"nowak","wiek":32},
{"imie": "Jan","nazwisko":"nowacki","wiek":32},
{"imie": "Tomasz","nazwisko":"lato","wiek":43}]

for indeks, rekord in enumerate(rekordy):
    osoby[indeks] = rekord

print(osoby)
print(len(rekordy))