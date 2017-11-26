rzeczy = ['doniczka','kwiatek','ziemia','woda']
print(rzeczy[1:3])
print(len(rzeczy))

imie = "Anna"
# imie[2] = 'i'  stringi są niemutowalne

rzeczy [2] = 'konewka'
print(rzeczy)
#  tu wypisz je za pomocą petli while'

rzeczy = ['doniczka','kwiatek','ziemia','woda']
rzeczy.append('konewka')
rzeczy.append('konewka')
rzeczy.append('grabie')
print(rzeczy)


if "kwiatek" in rzeczy:
    rzeczy.remove('kwiatek')
print(rzeczy)

