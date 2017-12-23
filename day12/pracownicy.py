from day12.alternatywny_konst import *

prac1 = Pracownik('adam',"kowalski",13)

prac2 = Pracownik.Pracownik("jan","nowak") #metoda klasy, metoda pola
print(prac2)

prac1.pesel = 455413114  #tworzy dynamicznie zmienne na poziomie instancji, pole dynamicznie powstało tylko w tym obiekcie

print(prac1.pesel)

print(prac1.__dict__)
print(Pracownik.__dict__)