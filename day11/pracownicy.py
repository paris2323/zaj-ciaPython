from day11.pracownik import *

prac1 = Pracownik("John","Travolta",50000)
print(prac1)

prac2 = Pracownik("John", "Turturo",30000)
print(prac2)
prac3 = Pracownik("John", "rambo",90000)
print(prac3)

# print(prac1.ilosc_instancji)
# print(prac2.ilosc_instancji)
# print(prac3.ilosc_instancji)

prac1.roczna_podwyzka = 15
print("Daje podwyżkę prac1")

print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

del prac1.roczna_podwyzka
print("usuwam podwyżkę dla pracownika nr 1")
print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)