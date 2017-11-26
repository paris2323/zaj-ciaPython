nazwisko = input('Podaj nazwisko:\n ')

#print(type(nazwisko))
# znaki białe
naz_czyste = nazwisko.strip()
naz_czyste = naz_czyste.upper()
print(naz_czyste)


nazwisko = input('Podaj nazwisko:\n ')
if not nazwisko.isalpha(): break
    print("wpisałeś cyfrę w nazwisku")
    exit(99)
elif nazwisko[-1] == "a":
    print('to kobieta')
elif nazwisko.endswith('ski'):
    print("chyba to facet")
elif nazwisko.isupper():
    print('chyba jesteś złośliwa:/')



