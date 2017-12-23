class Samochod(object):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.jedzie = None # dobrze go tutaj zamieścić
        self.silnik = None

    def __str__(self):
        return f'{self.marka} {self.model}'

    def ruszaj(self):
        self.jedzie = True
        print(f"{self.marka} ruszyl")

    def zatrzymaj(self):
        self.jedzie = False
        print(f"{self.marka} zatrzymal sie")

