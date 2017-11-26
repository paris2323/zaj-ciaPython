# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

liczba = int(input("podaj losową liczbę: "))

lista_czerwonych = [1,3,5,7,9,12,14,16,18,19,23,25,27,30,32,34,36]

if liczba in lista_czerwonych:
    print(f"Liczba {liczba} jest czerwona")
else:
    print(f"Liczba {liczba} jest czarna")
if liczba < 18:
    print(f"Liczba {liczba} jest niska")
else:
    print(f"Liczba {liczba} jest wysoka")
if liczba % 2 == 0:
    print(f"Liczba {liczba} jest parzysta")
else:
    print(f"Liczba {liczba} jest nieparzysta")