class Silnik(object):
    """Silnik"""

    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.__spalanie = None
        self.__co2 = 0.8  #pseudoprywatna zmienna

    def podaj_emisje(self, wartosc):
        self.__co2 *= wartosc  # mam dostęp do prywatnej zmiennej wewnątrz funkcji, nie jestem wstanie się dostać poprzez obiekt
        if self.__co2 < 1:
            self.__co2 *= wartosc
        else:
            self.__co2 = wartosc * 0.8

    def emisja(self):
        if self.__co2 > 20:
            return 20
        else:
            return self.__co2

    @property  # getter mam możliwość pobrania, a nie mam możliwości zapisania -> kontrola poziomu dostępu
    def spalanie(self):
        print("jestem w property")
        if self.__spalanie != None:
            return self.__spalanie * 0,9
        else:
            return 0

    @spalanie.setter #wstawia wartość