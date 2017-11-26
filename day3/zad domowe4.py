# 4. oblicz ocenę na podstawie progu procentowego
# Moje założenia:
# do 60procent niedostateczny
# od 60procent dopuszczający
# 70procent-85procent dobry
# 85procent-100procent b.dobry

ocena_pro = int(input('podaj procent: '))
ocena_proc = ocena_pro / 100

if ocena_proc < 0.60:
    print('ocena niedosteczna')
elif ocena_proc >=0.60 and ocena_proc < 0.70:
    print('ocena dostateczna')
elif ocena_proc >=0.70 and ocena_proc <0.85:
    print('ocena dobra')
else:
    print('bardzo dobra')