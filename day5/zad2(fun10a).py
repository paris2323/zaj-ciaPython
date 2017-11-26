def dodaj_imie(imie, baza=None):

    if baza == None:
        baza = []
        """
        sprawdza
        :param"""
    imie= imie.upper()
    baza.append(imie)
    return baza