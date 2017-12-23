from day10.czekolada import Czekolada
from day10.producent import Producent

prod1 = Producent("Milka","Zurych")

czeko1 = Czekolada(prod1,"z orzechemai", 400)
czeko2 = Czekolada(prod1,"z rodzynkami", 600)


print(czeko1)
print(czeko2)

print(czeko1 + czeko2)
print(czeko1 < czeko2)