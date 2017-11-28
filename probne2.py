

def greet(name):
    print(f"witaj {name.capitalize()}")

greet('asia')


def opis_animal(name,kind):
    print(f"To jest {kind} o imieniu {name.capitalize()}.")

opis_animal(kind= "pies",name="pako")

def dane (imie, nazwisko, drugie_imie=" "):
    print(f"{imie} {drugie_imie} {nazwisko}")

dane('anka','kowalska',"jola")


def prosto (a,b):
    pole = a*b
    return pole

x = prosto
print(x(17,2))

liczby = [2,4324,25,43,4,5765,756,7,3425,325,364]

def czy_w_zakresie(liczba, zakres=range(101)):
    if liczba in zakres:
        print(f"{liczba} - Yes")
    else:
        print(f"{liczba} - Yes")

for i in liczby:
    czy_w_zakresie(i)























