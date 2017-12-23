
from day9.samochod import Samochod
from day9.silnik import Silnik

silnik_v4 = Silnik(1998, "benzyna")
print(silnik_v4)

beemka = Samochod("BMW","3") #bez specjalnej metody __str__ nie uzyskasz opisu BMW 3 tylko zapis o miejscu w pamięci
print(beemka)

beemka.silnik = silnik_v4

print(beemka.silnik)

beemka.silnik.wlaczony = True