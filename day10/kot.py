from day10.zwierze import Zwierze

class Kot(Zwierze):
    def __init__(self,nazwa,kolor):
        super().__init__(nazwa)
        self.kolor = kolor


    def ruszaj_sie(self):  # (override - nadpisać) mówi nam o tym, że ta klasa jest nadpisana, nadpisujemy metody
        print(f'Kotek {self.nazwa} ruszy się!')