class Rest(object):
    def __init__(self,name,cusine_type):
        """"Tworzy instancję obiektu typu resturacja
                :param imię: str - imię
                :param rodzaj kuchni: str - rodzaj kuchni
                :param otwarty: bool - czy otwarty
                :param liczba obsłużonych - int liczba obsłużonych w danym dniu"""
        self.name = name
        self.cusine_type = cusine_type
        self.open = True
        self.number_served = 0

    def describe_rest(self):
        print(f"Restauracja {self.name.upper()} jest restauracją typu: {self.cusine_type}.")

    def open_rest(self):
        if self.open:
            self.open = True
            print(f"Restauracja {self.name.upper()} jest otwarta.")
        else:
            print(f"Restauracja {self.name.upper()} jest zamknięta.")

    def set_number_served(self):
        print(f"Restauracja obsłużyła dziś: {self.number_served} gości.")

restauracja1 = Rest("Pueblo","meksykańska")
restauracja1.describe_rest()
restauracja1.open_rest()
restauracja1.number_served = 23
restauracja1.set_number_served()

restauracja2 = Rest("Lao Thai","tajska")
restauracja2.describe_rest()
restauracja2.open_rest()

