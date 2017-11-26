if True:
    pass
if 5 == 10/2:
    print('wnętrze ifa')
    if 5 != 20:             #zagnieżdzony blok
        print('drugi if')


if 5 != 20/4:
    print('drugi if')
elif 5 == 5 and 20 % 2 ==1:
    print('drugi if,elif')
elif 45 % 3 == 12:
    print("elif modulo")
else:
    print('instrukcja domyslna')