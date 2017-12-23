# def dodaj_imie(imie, baza=None):
#     if baza == None:
#         baza = []
#     baza.append(imie)
#     return baza
#
#
# kobiety = dodaj_imie('anka')
# print(kobiety)
# kobiety = dodaj_imie('asia')
#
# faceci = dodaj_imie('antek')
# print(faceci)
# print(kobiety)
class Battery():
    def __init__(self,wielkosc):
        self.wielkosc = 82
    def __str__(self):
        return f"{self.wielkosc}"

class Car():
    """utworzenie klasy auto"""
    def __init__(self,marka,model,rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def opisuje_auto(self):
        print(f"{self.rok}: {self.marka} {self.model}")

class Ecar(Car):
    def __init__(self,marka,model,rok,battery):
        super().__init__(marka,model,rok)
        self.battery = 100

    def jaka_batttery(self):
        print(f"Wielkość wynosi: {self.battery}")

my_car = Car("Mazda","B3",2008)
my_tesla = Ecar("Tesla","WX",2017,70)

my_car.ecar = my_tesla
print(my_car.ecar.battery)

