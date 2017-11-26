#Przedmiot: pisak ma indeks nr: 0

rzeczy = ('pisak','dlugopis','szklanka', 'portfel','myszka')

# for i, rzecz in enumerate(rzeczy):
#     print(f"Przedmiot: {rzecz} ma indeks nr: {i}")


# indeks = 0
# for rzecz in rzeczy:
#     print(f"Przedmiot: {rzecz} ma indeks nr:{indeks} ")
#     indeks +=1
# print(15*"-")



indeks = 0
# nie zmienia się jej długość więc szkoda w whilu liczyć len
dlugosc = len(rzeczy)

while indeks < dlugosc:
    rzecz = rzeczy[indeks]
    print(f"Przedmiot: {rzecz} ma indeks nr:{indeks} ")
    indeks += 1

print(rzecz) # ostatni element jaki przeszedł przez pętlę while