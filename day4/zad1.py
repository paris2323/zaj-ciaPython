# oblicz liczby parzyste i nieparzyste w zakresie

zakres = range(23746)

parzyste = 0
nieparzyste = 0
for liczba in zakres:
    if liczba % 2 == 0:
        parzyste +=1
    else:
        nieparzyste +=1
print(f'Liczb nieparzystych{parzyste}, liczb nieparzystych {nieparzyste}')