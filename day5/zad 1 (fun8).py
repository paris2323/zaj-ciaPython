
# funkcja odwróć stringa
string = "asia"
nstring = string[::-1]
print(nstring)


#spr czy liczby w zakresie
liczby =[2,4324,25,43]
 # x - tak
 # y -nie

def czy_w_zakresie(liczba, zakres=range(100)):
    if liczba in zakres:
        print(f"{liczba} - Yes")
    else:
        print("nie")

for x in liczby:
    czy_w_zakresie(x)
