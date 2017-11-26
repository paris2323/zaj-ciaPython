# 3. czy liczba jest podzielna przez 3, 5, 7

liczba = int(input("podaj liczbę: "))
if liczba % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0:
    print(f"{liczba} podzielna przez 3,5,7")
else:
    print(f'{liczba} nie dzieli się przez 3,5,7')