class Ubrania(object):
    def __init__(self,rodzaj,rozmiar,kolor):
        self.rodzaj = rodzaj
        self.rozmiar = rozmiar
        self.kolor = kolor

class Buty(Ubrania):
    def __init__(self,rodzaj,wysokosc):
        self.rodzaj = rodzaj
        self.wysokosc = None


class Szpilki(Buty):
    def __init__(self,wysokosc):
        super().__init__(wysokosc)


szpilki2 = Szpilki(12)
print(szpilki2)


class Półbuty(Buty):
    pass



class OdzieżWierzchnia(Ubrania):
    pass