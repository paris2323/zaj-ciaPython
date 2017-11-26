
import pickle


baza = [{"imie": "Adam","nazwisko":"kowalski","wiek":32},
{"imie": "Anna","nazwisko":"nowak","wiek":32},
{"imie": "Jan","nazwisko":"nowacki","wiek":32},
{"imie": "Tomasz","nazwisko":"lato","wiek":43}]

#zapisujemy
with open("baza.pckl",'wb') as plik:
    pickle._dump(baza, plik)