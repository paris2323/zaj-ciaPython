import day7.moj_modul.odwracacz


def czy_palindrom(wyraz):
    '''Sprawdza czy podany wyraz jest palindrom
    (str) -> bool'''

    wyraz = wyraz.upper()
    odwrocony = day7.moj_modul.odwracacz.odwroc_string(wyraz)

    if wyraz == odwrocony:
        return True
    else:
        return False
print(czy_palindrom('kajak'))