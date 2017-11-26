rzeczy = ('pisak','dlugopis','szklanka', 'portfel','myszka')
kolory = ('czerwony','zielony','niebieski','fioletowy')

# x jest koloru y

indeks = 0
dlugosc = min(len(rzeczy), len(kolory))
while indeks < dlugosc:
    print(f'{rzeczy[indeks]} jest koloru:{kolory[indeks]}')
    indeks += 1

