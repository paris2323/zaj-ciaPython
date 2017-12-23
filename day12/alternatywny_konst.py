class Pracownik(object):

    ilosc_instancji = 0
    roczna_podwyzka = 7


    def __init__(self,imie,nazwisko,stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        Pracownik.ilosc_instancji += 1

    # def __init__(self,imie,nazwisko):
    #     self.imie = imie
    #     self.nazwisko = nazwisko
    #     self.stawka = 13


    @classmethod
    def zmien_roczna_podwyzka(cls, nowa_wartosc):
        cls.roczna_podwyzka = nowa_wartosc

    @classmethod
    def Pracownik(cls,imie,nazwisko): #pseudokod: 1. musimy mieć instancję cls.init, 2. dostosować dane 3.return, go zwrócić
        temp_pracownik = Pracownik(imie,nazwisko,13)
        temp_pracownik.roczna_podwyzka = 10
        return temp_pracownik


    def __str__(self):
        return f"Pracownik {self.nazwisko} ma {self.stawka} PLN"

    def __del__(self): # python tuż przed usunięciem obiektu
        Pracownik.ilosc_instancji -= 1
        print(f"Pracownik {self.nazwisko} został usunięty")