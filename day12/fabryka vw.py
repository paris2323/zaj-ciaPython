from day12.silnik import *

silnik1 = Silnik(1600)

print(silnik1.__dict__)  #_Silnik__co2

silnik1.__spalanie = 3.4   # utworzy się na poziomie instancji

print(silnik1.spalanie)



