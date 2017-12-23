class Silnik(object):
    def __init__(self,pojemnosc,paliwo):
        self.pojemnosc = pojemnosc
        self.paliwo = paliwo
        self.wlaczony = False

    def __str__(self):
        return f'{self.pojemnosc}'

