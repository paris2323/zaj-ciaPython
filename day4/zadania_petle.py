#1 program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1

#2 Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####
#


#4 program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
zakres = range(21)

for liczba in zakres:
    if liczba % 4 == 0:
        continue
    else:
        print(liczba)

print('koniec zadania 4')

#5 program który wypisze liczby od (0 do 100) z ciągu Fibonacciego

pierwsze_liczby = (0,1)
a,b = pierwsze_liczby  # rozpakowywanie tupli

for i in range(101):
    if b < 101:
        a,b = b, a+b
        print(a)

print("koniec zadania 5")

#6 program wypisujący tabliczkę mnozenia (1 do 10) dla podanej liczby (uzyc formatowania stringow)

liczba = int(input("Podaj liczbę: "))

for mnoznik in range(1,11):
    wynik = liczba*mnoznik
    print(f"Dla {liczba} wynik mnożenia przez {mnoznik} równa się: {wynik}")

print("koniec zadania 6")

#7oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

wiek_psa = int(input("Podaj wiek psa: "))
if wiek_psa < 3:
    ludzkie_lata = wiek_psa * 10.5
    print(f"Wiek psa w ludzkich latach wynosi: {int(ludzkie_lata)} lat.")
elif wiek_psa >= 3:
    ludzkie_lata = wiek_psa * 4 + 13
    print(f"Wiek psa w ludzkich latach wynosi: {int(ludzkie_lata)} lat.")