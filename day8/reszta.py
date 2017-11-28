
monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0}

wartosc_znak = 13.50
banknot = 20

reszta = banknot - wartosc_znak
print("wydaj: ", reszta)

if reszta < 0:
    print('Za mała wartość banknotu')
    guit()
elif reszta == 0:
    print('Bez reszty')
    quit()

for moneta in monety.keys():
    if reszta >= moneta:
        ilosc = reszta // moneta
        monety[moneta] = ilosc
        reszta = reszta - (moneta * ilosc) #zaokrąglić do dwóch miejsc po przecinku
        print('Tyle reszty jeszcze jest:', reszta)

for moneta, ilosc in monety.items():
    print(f"moneta: {moneta:>4} - {ilosc:>4} sztuk")